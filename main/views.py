from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect

from main.forms import *
# Create your views here.
def home(request):
    tournaments = Tournament.objects.all()
    return render(request, 'home.html', {
        'tournaments': tournaments, 
    })

def signUp(request):
    if request.method == 'POST':
        form = UserFormSignUp(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserFormSignUp()
    return render(request, 'signUp.html', {
        'formset': form,
    })


def signIn(request):
    if request.method == 'POST':
        form = UserFormSignIn(request.POST)
        try:
            us = User.objects.get(login=form.data['login'], password=form.data['password'])
        except:
            return redirect('/signIn')
        request.session.set_expiry(3600) # ustawienie czasu trwania sesji na 1h
        request.session['user'] = us.id
        request.session['login'] = us.login
        request.session['type'] = us.type
        return redirect('/')
    else:
        form = UserFormSignIn()
        return render_to_response('signIn.html', RequestContext(request, {'formset': form}))


def logout(request):
    del request.session["user"]
    del request.session["login"]
    del request.session["type"]
    request.session.modified = True
    return redirect('/')
