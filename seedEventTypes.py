from statsbombpy import sb
import pandas as pd
from setuptools import setup, find_packages
import os
import sys

import django
from django.forms.models import model_to_dict

sys.path.append('statsbombApp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'statsbombApp.settings'
django.setup()

from api.models import Pass, Match, Player, Lineup


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
# events = Event.objects.all()

# sbEventsMatchesDict = []
# matches = Match.objects.all()

# for match in matches:
#     matchEvents = sb.events(match_id=match.match_id)
#     matchEvents = pd.DataFrame(matchEvents, columns=['pass_end_location', 'pass_outcome', 'id'])
#     matchEvents =  matchEvents.to_dict(orient='records')
#     toAdd = {match.match_id: matchEvents}
#     sbEventsMatchesDict.append(toAdd)


matches = Match.objects.all()
for m in matches:
    lineups = sb.lineups(match_id=m.match_id)
    home_lineup = sbDFtoDict(lineups[m.home_team], ['player_id', 'player_name'])
    home_team_players = getListOfPlayers(home_lineup)

    away_lineup = sbDFtoDict(lineups[m.away_team],  ['player_id'])
    away_team_players = getListOfPlayers(away_lineup)

    homeLineupInstance = Lineup.create(match_id = m.match_id, team_name=m.home_team)
    homeLineupInstance.save()
    homeLineupInstance.players.set(home_team_players) 

    awayLineupInstance = Lineup.create(match_id = m.match_id, team_name=m.away_team)
    awayLineupInstance.save()
    awayLineupInstance.players.set(away_team_players) 


    print(m.away_lineup)
xd = 3

xc = 1
# for ev in events:
#     sbEvents = sb.events(match_id=ev.match_id)
#     sbEvents = pd.DataFrame(sbEvents, columns=['pass_end_location', 'pass_outcome', 'id'])
#     sbEventsDict =  sbEvents.to_dict(orient='records')
#     if ev.type == 'Pass':
        

#         newPass = Pass()
