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
from django.db.models import ImageField
from django.core.files.images import ImageFile

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
        tmp_img = createPassmap(p, m)
        
        # imgField = ImageField(img, upload_to=f'events/passmaps/match_{m.match_id}/player_{p.player_id}.png')
        # img.save()
        playerRaport = PlayerMatchRaport.create(player=p, match=m, raport_type='passmap', tmp_img=tmp_img)
        playerRaport.save()
        xd =1
        

    for p in awayLineupPlayers:
        
        tmp_img = createPassmap(p, m)
        playerRaport = PlayerMatchRaport.create(player=p, match=m, raport_type='passmap', tmp_img=tmp_img)
        playerRaport.save()
    

