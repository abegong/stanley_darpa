from django.db import models


def calc_team_scores():
  #Not working yet
#  T = Team.objects.all()
#  C = City.objects.all()
  E = Event.objects.all()

  #Arrange by city
  cities = {}
  for e in E:
    if e.city.name in cities: cities[e.city.name].append(e)
    else: cities[e.city.name] = [e]
#  print cities
#  print len(cities)

  #Remove duplicate team-cities, keeping on_campus events when conflicts occur
  for c in cities:
    t = {}
    for e in cities[c]:
      if not e.team in t: t[e.team] = e
      else:
        if e.on_campus and not t[e.team].on_campus:
          t[e.team] = e
    c = t.values()
#  print cities
#  print len(cities)

  #Tally total points for each team.
  scores = {}
  for t in Team.objects.all():
    scores[t.id] = 0
  for c in cities:
    for e in cities[c]:
#      print e.city, e.team, e.on_campus

      if e.on_campus == 1: scores[e.team.id] += 3
      else: scores[e.team.id] += 1
      
      if len(cities[c]) == 1:
        if e.on_campus == 1: scores[e.team.id] += 3
        else: scores[e.team.id] += 1
  print scores

  return scores

  #Search for cities without duplicates. Award bonus points to teams with singletons.

#  "cities": [ {"name":city.name, "event_count":Event.objects.filter(city=city.id).count()} for city in City.objects.all()],
#  for e in E:
#    pass    
  


# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=100)
	state = models.CharField(max_length=20)
	population = models.IntegerField()
	class Admin:
		list_display   = ('name', 'state', 'population')
		list_filter    = ('state')
		ordering       = ('-name',)
		search_fields  = ('name',)

	class Meta:
		ordering = ["name"]

	def __unicode__(self):
		return self.name

class Event(models.Model):
	time = models.DateTimeField( auto_now_add=True )

	team = models.ForeignKey('Team')
	city = models.ForeignKey('City')

	pic_file = models.FileField(upload_to='photos/')#stanley_darpa/static/photos')

	on_campus = models.IntegerField()
	uniqname = models.CharField(max_length=20)
	story = models.TextField(max_length=20)

	class Meta:
	        ordering = ["-time"]
		pass

	class Admin:
		list_display   = ('team', 'city', 'time')


class Team(models.Model):
	name = models.CharField(max_length=100)

	class Admin:
	        pass

	def __unicode__(self):
		return self.name

############### Forms ##########################################

from django.forms import ModelForm, Textarea

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('pic_file','city','on_campus','team','uniqname','story',)

#		required = ('pic_file','city','on_campus','team','uniqname','story',)
#		required = ('pic_file','city','on_campus','team',)
	        widgets = {
	            'story': Textarea(attrs={'cols': 40, 'rows': 5}),
	        }
"""

from django import forms

class EventForm(forms.Form):
    pic_file = forms.FileField(label="Upload picture")#models.FileField(upload_to='photos')
    city = forms.ForeignKey('City')
    on_campus = forms.BooleanField()
    team = forms.ForeignKey('Team')
    uniqname = forms.CharField(max_length=20)
    story = forms.Textarea(max_length=20)



    subject = forms.CharField(label="Uploadasdfpicture", max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

"""





