import glob, random
from django.core.management.base import BaseCommand, CommandError

from settings import STATIC_URL
from stanley_darpa.models import City, Event, Team


class Command(BaseCommand):
  args = '< >'
  help = 'Adds a random event'

  def handle(self, *args, **options):
    cities = City.objects.all()
    teams = Team.objects.all()

    print STATIC_URL+'media/stock_photos/*'
    f = glob.glob( STATIC_URL+'media/stock_photos/*' )
    print f

    e = Event(
        pic_file='stock_photos/'+random.choice(['A.jpg','B.jpg','C.jpg','D.jpg','E.png','F.png','G.jpg']),
        city=cities[random.randint(0,len(cities)-1)],
        team=teams[random.randint(0,len(teams)-1)],
        on_campus=random.randint(0,1),
    )
    print e
    
    e.save()
#    return HttpResponse("Event added!")

    self.stdout.write('Successfully added event "' + e.team.name + ' got ' + e.city.name + '"\n')

