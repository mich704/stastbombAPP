from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CompetitionSerializer, MatchSerializer, PlayerMatchRaportSerializer
from .models import Competition, Match, PlayerMatchRaport
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


class CompetitionView(viewsets.ViewSet):
    def get_queryset(self, *args, **kwargs):
        competitions = Competition.objects.all()
        return competitions

    
    def get(self, request, *args, **kwargs):     
        # id = request.query_params["id"]
        try:
            competition_id = self.kwargs["competition_id"]
            if competition_id != None:
                competition_object = Competition.objects.get(competition_id=competition_id)
                serializer = CompetitionSerializer(competition_object)
        except:
            competitions = self.get_queryset()
            serializer = CompetitionSerializer(competitions, many=True)
  
        return Response(serializer.data)
    
    def get_competition_matches(self, request, *args, **kwargs):
        
        try:
            competition_id = self.kwargs["competition_id"]
            if competition_id != None:
                matches_object = Match.objects.filter(competition =  competition_id)
                print('get_competition_matches',competition_id)
                serializer = MatchSerializer(matches_object, many=True)  #many- important
        except:
            return Response("No matches")
  
        return Response(serializer.data)   

class MatchView(APIView):
    serializer_class = MatchSerializer
    
    def get_queryset(self, *args, **kwargs):
        matches = Match.objects.all()
        return matches

    def get(self, request, *args, **kwargs):     
        print(self.kwargs)
        # id = request.query_params["id"]
        try:
            match_id = self.kwargs["match_id"]
            if match_id != None:
                match_object = Match.objects.get(match_id=match_id)
                serializer = MatchSerializer(match_object)
                
        except:
            matches = self.get_queryset()
            serializer = MatchSerializer(matches, many=True)

        return Response(serializer.data)

class PlayerMatchRaportView(APIView):
    def get(self, request, *args, **kwargs):     
        # id = request.query_params["id"]
        print(self.kwargs)
        try:
            match_id = self.kwargs["match_id"]
            player_id = self.kwargs["player_id"]
           
            if match_id != None and player_id != None:
                raport_object = PlayerMatchRaport.objects.get(match_id=match_id, player_id=player_id, raport_type='passmap')
                serializer = PlayerMatchRaportSerializer(raport_object)
                return Response(serializer.data)
            else:
                return Response({})
            
        except:
            return Response({})
  
       
