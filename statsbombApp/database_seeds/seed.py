from statsbombpy import sb
import pandas as pd
import sqlite3
from setuptools import setup, find_packages
import os
import sys
import argparse


import django
import math
from django.forms.models import model_to_dict

sys.path.append('statsbombApp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'statsbombApp.settings'
django.setup()
global i
i=0
from api.models import Competition, Match, Player, Pass, Event


possibleSeasons = [
    # '2019/2020',
    # '2020/2021',
    # '2021/2022',
    # '2022/2023',
    '2022'
    #'2020'
]


def createEvent(player, matchModelObj, sbEventsDict):
    
    #print(player.player)
    playerEvents = [e for e in sbEventsDict if e['player_id'] == player.player_id]
    
    for playerEvent in playerEvents:
        if playerEvent['type'] == 'Pass' and \
            Event.objects.filter(event_uuid = playerEvent['id']).count() == 0:
                newEvent = Event.create(
                    event_uuid = playerEvent['id'],
                    player = player,
                    match = matchModelObj,
                    type = playerEvent['type']
                )
                newEvent.save()
                print(newEvent, i)

                newPass  = Pass.create(
                    event = newEvent,
                    location_start = playerEvent['location'],
                    location_end = playerEvent['pass_end_location'],
                    pass_outcome = playerEvent['pass_outcome']
                )

                newPass.save()
                
            


def getSbEventsDictionary(match):
    
    sbEvents = sb.events(match['match_id'])
    sbEvents = sbEvents.loc[ sbEvents['player'].isna() == False]
    #'player','type','location', 'pass_end_location', 'pass_outcome'
    #columns=['player', 'team', 'player_id', 'type','location', 'pass_end_location', 'pass_outcome']
    sbEvents = pd.DataFrame(sbEvents, columns=['player', 'team', 'player_id', 'type','location', 'pass_end_location', 'pass_outcome', 'id'])
    sbEventsDict =  sbEvents.to_dict(orient='records')
    matchModelObj = Match.objects.get(match_id=match['match_id']) 
    sbEventsDict = list(filter(lambda event: event['type'] == 'Pass', sbEventsDict))
    print(match)
    for ev in sbEventsDict:
        
        if Player.objects.filter(player_id = ev['player_id']).count() == 0:
            #print(ev['player'])
            newPlayer = Player.create(player=ev['player'], player_id=ev['player_id'] )
            newPlayer.save()     
            createEvent(newPlayer, matchModelObj, sbEventsDict)
                
        else:
            player = Player.objects.get(player_id=ev['player_id'])
            createEvent(player, matchModelObj, sbEventsDict)

    return sbEvents

def getSbCompetitionsDictionary():
    sbCompetitions = sb.competitions()
    sbCompetitions = sbCompetitions.loc[sbCompetitions['season_name'].isin(possibleSeasons)]
    sbCompetitions = sbCompetitions.loc[sbCompetitions['competition_gender'] == 'male']
    sbCompetitions = pd.DataFrame(sbCompetitions, columns = ['competition_id', 'competition_name', 'season_name', 'season_id'])     
    sbCompetitionsDict = sbCompetitions.to_dict(orient='records')

    return sbCompetitionsDict


def getSbMatchesDictionary(competition_id, season_id):
    sbMatches = sb.matches(competition_id=competition_id, season_id=season_id)
    sbMatches = pd.DataFrame(sbMatches, columns = ['match_id', 'home_team', 'away_team', 'home_score', 'away_score'])
    sbMatches = sbMatches.to_dict(orient='records')   
    
    return sbMatches


def clear_data():
    Match.objects.all().delete()
    Competition.objects.all().delete()
    Player.objects.all().delete()
    Pass.objects.all().delete()

    """Deletes all the table data"""
    print('Competition data cleared!')
    

def seedMatchModel(competition):
    matchesDict = getSbMatchesDictionary(competition.competition_id, competition.season_id)
    #sbMatchesDict = getSbMatchesDictionary()
    for match in matchesDict:
        match_id, home_team, away_team, home_score, away_score = match.values()
        if home_team == 'Poland' or away_team == 'Poland':
            if Match.objects.filter(match_id = match_id).count() == 0:
                
                newMatch = Match.create(match_id, competition, home_team, away_team, home_score, away_score)
                #print(newMatch._id)
                newMatch.save()
        
            getSbEventsDictionary(match)
        #print(eventsDict)
        #print(newMatch)


def seedCompetitionModel(competitionDict):
    print('Seeding database...')
    for competition in competitionDict:
        print(competition.values())
        competition_id, competition_name, season_name, season_id = competition.values()
        if Competition.objects.filter(competition_id = competition_id).count() == 0:
            newCompetition = Competition.create(competition_id, season_name, competition_name, season_id)
            newCompetition.save()
            seedMatchModel(newCompetition)
        else:
            compObject = Competition.objects.get(competition_id=competition_id) 
            seedMatchModel(compObject)
    print('Database seeded!')    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-clear", "--clearData", action='store_true', help="Delete all objects")
    args = parser.parse_args()
    if args.clearData:
        clear_data()
    
    sbCompetitionDict = getSbCompetitionsDictionary()
    seedCompetitionModel(sbCompetitionDict)


if __name__ == '__main__':
    main()
    import subprocess
    subprocess.Popen("seedLineups.py 1", shell=True)

