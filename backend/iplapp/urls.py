from django.urls import path
from . import views

urlpatterns = [
    path('matches_per_year/', views.matches_per_year),
    path('stacked_wins/', views.stacked_wins),
    path('extra_runs/<int:year>/', views.extra_runs_per_team),
    path('top_bowlers/<int:year>/', views.top_economical_bowlers),
    path('played_vs_won/<int:year>/', views.matches_played_vs_won),
]