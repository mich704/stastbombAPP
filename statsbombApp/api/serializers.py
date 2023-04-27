from rest_framework import serializers
from .models import Competition, Match, Player, Pass, Lineup, PlayerMatchRaport

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('pk', 'competition_id', 'season_name', 'competition_name', 'season_id')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('pk', 'player_id', 'player')


class LineupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lineup
        fields = ('match_id', 'team_name', 'players') 
        depth = 1


class MatchSerializer(serializers.ModelSerializer):
    home_lineup = LineupSerializer()
    away_lineup = LineupSerializer()
    class Meta:
        model = Match
        fields = (  'pk', 'match_id', 'competition',
                    'home_team', 'away_team', 'home_score',
                    'away_score', 'home_lineup', 'away_lineup')
        depth  = 2 
        
    # def create(self, validated_data):
    #     home_lineup = validated_data.get('home_lineup')
    #     away_lineup = validated_data.get('away_lineup')

    #     match_obj = None

    #     home_lineup_obj = Lineup.objects.create(home_lineup)
    #     away_lineup_obj = Lineup.objects.create(away_lineup)

    #     if home_lineup_obj and away_lineup_obj:
            

    #         match_obj = Match.objects.create(home_lineup = home_lineup_obj, away_lineup = away_lineup_obj, **validated_data)

    #     return match_obj
    

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = (  'event_uuid', 'match', 'player',
                    'type', 'location_start_X', 'location_start_Y',
                    'location_end_X', 'location_end_Y', 'pass_outcome')
        

class PlayerMatchRaportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMatchRaport
        fields = ('id', 'raport_type', 'match_id', 'player_id', 'image')
