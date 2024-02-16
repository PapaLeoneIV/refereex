from django.shortcuts import render
from .models import League, Team

def get_leagues(request):
    all_leagues= League.objects.all()
    context= {
        'leagues': all_leagues
    }
    return render(request, 'core/leaguelist.html', context)

def get_teams(request, pk):
    league= League.objects.get(pk=pk)
    teams= Team.objects.filter(league=league)
    inter = teams.filter(name='Inter')
    context= {
        'league': league,
        'teams': teams,
    }
    return render(request, 'core/league_detail.html', context)