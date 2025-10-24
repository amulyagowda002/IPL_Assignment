from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Match, Delivery
from django.db.models import Count, Sum, F
from django.shortcuts import render
from .models import Match

@api_view(['GET'])
def matches_per_year(request):
    qs = Match.objects.values('season').annotate(count=Count('id')).order_by('season')
    return Response(list(qs))

@api_view(['GET'])
def stacked_wins(request):
    # returns wins per team per season
    qs = Match.objects.values('season','winner').annotate(wins=Count('id')).order_by('season')
    return Response(list(qs))

@api_view(['GET'])
def extra_runs_per_team(request, year):
    matches = Match.objects.filter(season=year).values_list('id', flat=True)
    qs = Delivery.objects.filter(match_id__in=matches).values('bowling_team').annotate(extra=Sum('extra_runs'))
    return Response(list(qs))

@api_view(['GET'])
def top_economical_bowlers(request, year):
    matches = Match.objects.filter(season=year).values_list('id', flat=True)
    qs = Delivery.objects.filter(match_id__in=matches).values('bowler').annotate(runs=Sum('total_runs'), balls=Count('ball')).order_by('runs')[:20]
    # crude economy: runs per over (balls/6)
    data=[]
    for r in qs:
        balls=r['balls'] or 0
        overs = balls/6 if balls>0 else 0
        econ = r['runs']/overs if overs>0 else None
        data.append({'bowler': r['bowler'], 'runs': r['runs'], 'balls': balls, 'economy': econ})
    return Response(data)

@api_view(['GET'])
def matches_played_vs_won(request, year):
    played = Match.objects.filter(season=year).values('team1').annotate(count=Count('id'))
    # For simplicity, calculate wins per team
    wins = Match.objects.filter(season=year).values('winner').annotate(wins=Count('id'))
    return Response({'played': list(played), 'wins': list(wins)})

def home(request):
    # Chart 1 — Matches per year
    matches_per_year = (
        Match.objects.values('season')
        .order_by('season')
        .annotate(total=Count('id'))
    )
    chart1_data = [['Year', 'Matches']]
    for item in matches_per_year:
        chart1_data.append([str(item['season']), item['total']])

    # Chart 2 — Wins per team
    wins_per_team = (
        Match.objects.values('winner')
        .exclude(winner__isnull=True)
        .annotate(total=Count('winner'))
        .order_by('-total')[:10]
    )
    chart2_data = [['Team', 'Wins']]
    for item in wins_per_team:
        chart2_data.append([item['winner'], item['total']])

    context = {
        'chart1_data': chart1_data,
        'chart2_data': chart2_data
    }
    return render(request, 'home.html', context)