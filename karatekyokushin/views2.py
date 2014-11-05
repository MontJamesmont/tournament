from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect

from karatekyokushin.forms import *


# Create your views here.

def KarateKyokushinMain(request):
    template = loader.get_template('main.html')
#    latest_seasons = Season.objects.order_by('-id')[:10]
#    latest_rounds = Round.objects.order_by('-id')[:10]
#    latest_matchday = Matchday.objects.order_by('-id')[:10]
#    latest_matches = Match.objects.order_by('-id')[:10]
    context = RequestContext(request, {
#       'latest_matches': latest_matches,
#       'latest_seasons': latest_seasons,
#       'latest_rounds': latest_rounds,
#        'latest_matchday': latest_matchday,
    })
    return HttpResponse(template.render(context))

def KarateKyokushinCreate(request):
    
#    if request.method == 'POST':
#        form = CreateTournamentForm(request.POST)
#        if form.is_valid():
#            form.save()
#    else:
#        form = CreateTournamentForm()
#    return render(request, 'createtournament.html', {
#        'form': form, 
#    })
    
    template = loader.get_template('createtournament.html')
    
    if request.method == 'POST':
        form = CreateTournamentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateTournamentForm()
    
#    latest_seasons = Season.objects.order_by('-id')[:10]
#    latest_rounds = Round.objects.order_by('-id')[:10]
#    latest_matchday = Matchday.objects.order_by('-id')[:10]
#    latest_matches = Match.objects.order_by('-id')[:10]
    context = RequestContext(request, {
        'form': form,
#       'latest_matches': latest_matches,
#       'latest_seasons': latest_seasons,
#       'latest_rounds': latest_rounds,
#        'latest_matchday': latest_matchday,
    })
    return HttpResponse(template.render(context))
def tournament(request, tournament_id):
    template = loader.get_template('tournament.html')
    teams = Team.objects.all()
    tournament = Tournament.objects.get(id=tournament_id)
    players = tournament.users.filter(type="PLR")
    context = RequestContext(request, {'tournament': tournament, 'teams': teams, 'players':players, })
    return HttpResponse(template.render(context))

