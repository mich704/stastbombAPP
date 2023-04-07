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

from api.models import Pass, Match, Player, Lineup, Event

def sbDFtoDict(sbData, columns):
    sbData = pd.DataFrame(sbData, columns=columns)
    sbData =  sbData.to_dict(orient='records')

    return sbData


events = Event.objects.all()
matches = Match.objects.all()

for m in matches:
    homeLineup = Lineup.objects.get(match_id = m.match_id, team_name = m.home_team)
    homeLineupPlayers = homeLineup.players.all()
    for p in homeLineupPlayers:
        createPassmap(p, m)
    

