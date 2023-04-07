from django.db import models
import uuid

# Create your models here.

class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    season_name = models.CharField(max_length=10)

    @classmethod
    def create(cls, competition_id, season_name, competition_name):
        competition = cls(
            competition_id=competition_id,
            season_name=season_name,
            competition_name=competition_name
        )
        return competition
    


class Competition(models.Model):
    competition_id = models.IntegerField(primary_key=True)
    season_name = models.CharField(max_length=10)
    competition_name = models.CharField(max_length=20)
    season_id = models.IntegerField()

    @classmethod
    def create(cls, competition_id, season_name, competition_name, season_id):
        competition = cls(
            competition_id=competition_id,
            season_name=season_name,
            competition_name=competition_name,
            season_id = season_id
        )
        return competition

    def __str__(self):
        return self.competition_name
    

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player = models.CharField(max_length=30)
    
    @classmethod
    def create(cls, player_id, player):
        newPlayer = cls(
            player_id = player_id,
            player = player
        )
        return newPlayer
    
    def __str__(self):
        return self.player.encode('utf-8')


class Lineup(models.Model):
    match_id = models.IntegerField()
    team_name = models.CharField(max_length=20)
    players = models.ManyToManyField(Player)

    @classmethod
    def create(cls, match_id, team_name):
        newLineup = cls(
            match_id = match_id,
            team_name = team_name
        )
        return newLineup

class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, db_constraint=False)
    home_team = models.CharField(max_length=20)
    home_lineup = models.OneToOneField(Lineup,on_delete=models.CASCADE, null=True, related_name='home_lineup')
   
    away_team = models.CharField(max_length=20)
    away_lineup = models.OneToOneField(Lineup, on_delete=models.CASCADE, null=True, related_name='away_lineup')

    home_score = models.IntegerField()
    away_score = models.IntegerField()

    
    @classmethod
    def create(cls, match_id, competition, home_team, away_team, home_score, away_score):
        match = cls(
            match_id=match_id,
            competition=competition,
            home_team = home_team,
            away_team = away_team,
            home_score = home_score,
            away_score = away_score
        )
        return  match

    # @property
    # def home_team(self):
        
    #     return self.home_team

    def __str__(self):
        return "{home_team} {home_score} - {away_score} {away_team}".format(
            home_team = self.home_team,
            away_team = self.away_team,
            home_score = self.home_score,
            away_score = self.away_score
        )
    

class Event(models.Model):
    event_uuid = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)

    @classmethod
    def create(cls, event_uuid, player, match, type):
        newEvent = cls(
            event_uuid = event_uuid,
            match = match,
            player = player,
            type = type
        )
      
        return newEvent


    def __str__(self):
        return f"{self.type} {self.player_id}"


class Pass(models.Model):
    event = models.OneToOneField(Event, parent_link=True, on_delete=models.PROTECT)
    location_start_X = models.FloatField(default=-1)
    location_start_Y = models.FloatField(default=-1)
    pass_end_location_X = models.FloatField(default=-1)
    pass_end_location_Y = models.FloatField(default=-1)
    pass_outcome = models.CharField(max_length=30)

    @classmethod
    def create(cls, event, location_start, location_end, pass_outcome):
        
        newEvent = cls(
            event = event,
            location_start_X = location_start[0],
            location_start_Y = location_start[1],
            pass_end_location_X = location_end[0],
            pass_end_location_Y = location_end[1],
            pass_outcome = pass_outcome
        )
        
        return newEvent

    def pass_end_location(self):
        return [self.pass_end_location_X, self.pass_end_location_Y]
    
    def __str__(self):
        return f"{self.type} {self.player.player} {self.pass_end_location_X} {self.pass_end_location_Y}"
    

class EventImage(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, null=True, related_name='away_lineup')
    image = models.ImageField(upload_to ='uploads/')
# class Shot(Event):
#     event = models.OneToOneField(Event, parent_link=True, on_delete=models.PROTECT)
#     goal = models.BooleanField()



