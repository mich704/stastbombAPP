from django.urls import path
from .views import CompetitionView, MatchView

urlpatterns = [
    path('', CompetitionView.as_view({'get': 'get'})),
    path('competitions/', CompetitionView.as_view({'get': 'get'})),
    path('competitions/<int:competition_id>/', CompetitionView.as_view({'get': 'get'})), 
    path('competitions/<int:competition_id>/matches/', CompetitionView.as_view({'get': 'get_competition_matches'})),
    path('competitions/<int:competition_id>/matches/<int:match_id>/', MatchView.as_view()), 
    path('matches/', MatchView.as_view()),
    path('matches/<int:match_id>/', MatchView.as_view())
]
