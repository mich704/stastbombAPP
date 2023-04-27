from statsbombpy import sb
import pandas as pd
from setuptools import setup, find_packages
import os
import sys
import django

sys.path.append('statsbombApp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'statsbombApp.settings'
django.setup()

from api.models import Match, Player, Lineup

def sbDFtoDict(sbData, columns):
    sbData = pd.DataFrame(sbData, columns=columns)
    sbData =  sbData.to_dict(orient='records')
    return sbData

def getListOfPlayers(lineupList):
    lineupList = [player['player_id'] for player in lineupList if 'player_id' in player]
    team_players = []

    for p_id in lineupList:
        try:
           team_players.append(Player.objects.get(player_id = p_id))
        except:
            pass


    return team_players


def createLineups(matches):
    for m in matches:
        lineups = sb.lineups(match_id=m.match_id)
        home_lineup = sbDFtoDict(lineups[m.home_team], ['player_id', 'player_name'])
        home_team_players = getListOfPlayers(home_lineup)

        away_lineup = sbDFtoDict(lineups[m.away_team],  ['player_id'])
        away_team_players = getListOfPlayers(away_lineup)

        if not Lineup.objects.filter(match_id = m.match_id, team_name=m.home_team).exists():
            homeLineupInstance = Lineup.create(match_id = m.match_id, team_name=m.home_team)
            homeLineupInstance.save()
            homeLineupInstance.players.set(home_team_players) 
            m.home_lineup = homeLineupInstance

        if not Lineup.objects.filter(match_id = m.match_id, team_name=m.away_team):
            awayLineupInstance = Lineup.create(match_id = m.match_id, team_name=m.away_team)
            awayLineupInstance.save()
            awayLineupInstance.players.set(away_team_players) 
            m.away_lineup = awayLineupInstance

        m.save()
    

def main():
    matches = Match.objects.all()
    createLineups(matches)


if __name__ == '__main__':
    main()



