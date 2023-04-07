from statsbombpy import sb
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import time


from statsbombpy import sb
import pandas as pd
from setuptools import setup, find_packages
import os
import sys
import django
sys.path.append('statsbombApp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'statsbombApp.settings'
django.setup()

from api.models import Pass, Player, Event



def createPassmap(player, match):

    fig1, ax = plt.subplots(figsize=(13.5,8))
    fig1.set_facecolor('#22312b')
    ax.patch.set_facecolor('#22312b')
    pitch = Pitch(pitch_type='statsbomb', orientation='horizontal', pitch_color='#22312b',  line_color='white',
                figsize=(16,11), constrained_layout=True, tight_layout=False)  # optional stripes
    pitch.draw(ax=ax)
    plt.gca().invert_yaxis()

    print(player.player, match)

    player_id = player.player_id
    match_id = match.match_id

    playerMatchEvents = Event.objects.filter(player_id=player_id, match_id=match_id)
    playerMatchPasses = [Pass.objects.get(event=event) for event in playerMatchEvents]


    xd = 2


    teams = [match.home_team, match.away_team]

    
    title = plt.title("{} vs. {}\n {} passmap: ".format(teams[0], teams[1], player.player),
            fontsize=12,
            pad='2.0',
            fontstyle='italic' )


    plt.setp(title, color='w')

    for playerPass in playerMatchPasses:
        start_location = [playerPass.location_start_X, playerPass.location_start_Y]
        end_location = [playerPass.pass_end_location_X, playerPass.pass_end_location_Y]
        outcome = playerPass.pass_outcome

        print(start_location, end_location, outcome)
        if outcome != 'Incomplete':
            plt.plot((start_location[0], end_location[0]),(start_location[1], end_location[1]), color = 'green')
            plt.scatter(start_location[0], start_location[1], color='green')
        else:
            plt.plot((start_location[0], end_location[0]),(start_location[1], end_location[1]), color = 'red')
            plt.scatter(start_location[0], start_location[1], color='red')

    print(fig1)
    plt.show()
    
        

    