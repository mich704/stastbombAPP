from statsbombpy import sb
import pandas as pd
from setuptools import setup, find_packages
import os
import sys
import django


from eventImageGenerator import createPassmap

sys.path.append('statsbombApp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'statsbombApp.settings'
django.setup()

from api.models import Match, Lineup, Event, PlayerMatchRaport

def sbDFtoDict(sbData, columns):
    sbData = pd.DataFrame(sbData, columns=columns)
    sbData =  sbData.to_dict(orient='records')

    return sbData


events = Event.objects.all()
matches = Match.objects.all()

for m in matches:
    homeLineup = Lineup.objects.get(match_id = m.match_id, team_name = m.home_team)
    homeLineupPlayers = homeLineup.players.all()

    awayLineup = Lineup.objects.get(match_id = m.match_id, team_name = m.away_team)
    awayLineupPlayers = awayLineup.players.all()

    for p in homeLineupPlayers:
        if PlayerMatchRaport.objects.filter(player=p, match=m, raport_type='passmap').count() == 0:
            tmp_img = createPassmap(p, m)
            playerRaport = PlayerMatchRaport.create(player=p, match=m, raport_type='passmap', tmp_img=tmp_img)
       
    for p in awayLineupPlayers:
        if PlayerMatchRaport.objects.filter(player=p, match=m, raport_type='passmap').count() == 0:
            tmp_img = createPassmap(p, m)
            playerRaport = PlayerMatchRaport.create(player=p, match=m, raport_type='passmap', tmp_img=tmp_img)
        
    

