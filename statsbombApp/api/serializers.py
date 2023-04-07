from rest_framework import serializers
from .models import Competition, Match, Player, Pass

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('pk', 'competition_id', 'season_name', 'competition_name', 'season_id')


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('pk', 'match_id', 'competition', 'home_team', 'away_team', 'home_score', 'away_score')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('pk', 'player_id', 'player')


class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = (  'event_uuid', 'match', 'player',
                    'type', 'location_start_X', 'location_start_Y',
                    'location_end_X', 'location_end_Y', 'pass_outcome')