# Create your views here.

from django.http import HttpResponse
from django import template
from django.shortcuts import render_to_response
from django.core import serializers
from django.template import RequestContext

from stanley_darpa.models import Team, City, Event, EventForm, calc_team_scores
import random, glob

def index(request):
    t = template.loader.get_template("splash.html")
    c = template.Context()
    return HttpResponse(t.render(c))

def rules(request):
    t = template.loader.get_template("rules.html")
    c = template.Context({})
    return HttpResponse(t.render(c))

def submit(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
             form.save()
             form = EventForm()
             success = 'Successfully submitted!'

        else:
             success = 'Submission failed. Did you forget a field?'

    else:
        success = ''
        form = EventForm()

    return render_to_response('submit.html', {'form': form, 'success':success})

def countdown(request):
    t = template.loader.get_template("countdown.html")
    c = template.Context({
      "cities": [ {"name":city.name, "event_count":Event.objects.filter(city=city.id).count()} for city in City.objects.all()],
      "teams":Team.objects.all(),#[team.name for team in Team.objects.all()],
#      "events": Event.objects.all()[:10],
    })
#    return HttpResponse(t.render(c))
    return render_to_response('countdown.html', {
      'events': Event.objects.all(),
#      "cities": City.objects.all(),
      "cities":[ {"name":city.name, "event_count":Event.objects.filter(city=city.id).count()} for city in City.objects.all()],
      "teams": Team.objects.all(),#[team.name for team in Team.objects.all()],
      "scores": calc_team_scores(),
      'deadline':{'year':2011,'month':11,'day':7,'hour':13,'min':0},
    })

"""
def teamDetail(request):
#    t = template.loader.get_template("team_detail.html")
#    c = template.Context({})
#    return HttpResponse(t.render(c))
    team = Team.objects.get(pk=request.GET["id"])
    return render_to_response('team_detail.html', {
      'team':team,
      'events': Event.objects.filter(team=team)
    } )
"""

def cities(request):
#    calc_team_scores()
    return render_to_response('cities.html', {'teams':Team.objects.all(), 'cities':City.objects.all(), 'events': Event.objects.all()} )
#    t = template.loader.get_template("city_grid.html")
#    c = template.Context({})
#    return HttpResponse(t.render(c))

#def allEvents(request):
#    return render_to_response('all_events.html', {'events': Event.objects.all()} )

#AJAX handlers

def addRandomEvent(request):
    return HttpResponse("Random events disabled")

    #Add random event
    cities = City.objects.all()
    teams = Team.objects.all()
    e = Event(
        pic_file='stock_photos/'+random.choice(['A.jpg','B.jpg','C.jpg','D.jpg','E.png','F.png','G.jpg']),
        city=cities[random.randint(0,len(cities))],
        team=teams[random.randint(0,len(teams))],
        on_campus=random.randint(0,1),
    )
    e.save()
    return HttpResponse("Event added!")

def getEvents(request):
    if "sinceId" in request.GET: events = Event.objects.filter(id__gt=request.GET["sinceId"])[:50]
    else: events = Event.objects.all()[:10]
    return render_to_response('events.html', {'events': events}, context_instance=RequestContext(request))

#    data = serializers.serialize('json', events)
#    return HttpResponse(data,'application/javascript')


