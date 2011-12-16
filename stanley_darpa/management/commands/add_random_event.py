import glob, random, time, datetime
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from settings import STATIC_ROOT, MEDIA_ROOT
from stanley_darpa.models import City, Event, Team

class Command(BaseCommand):
  args = '< >'
  help = 'Adds a random event'

  def handle(self, *args, **options):

    #Reset the game on the hour
    now = datetime.datetime.now()
    if now.minute == 0:
      call_command('flush', interactive=False)
      call_command('loaddata', '/opt/bitnami/apps/django/django_projects/Project/stanley_darpa/data/cities.json')
      call_command('loaddata', '/opt/bitnami/apps/django/django_projects/Project/stanley_darpa/data/teams.json')
      self.stdout.write('Reset the game\n')


    cities = City.objects.all()
    teams = Team.objects.all()

    F = glob.glob( MEDIA_ROOT+'tmp/*' )
    G = ['/'.join(f.split('/')[-2:]) for f in F ]
#    print G

    for a in range(8):
      e = Event(
          pic_file=random.choice(G),#'stock_photos/'+random.choice(['A.jpg','B.jpg','C.jpg','D.jpg','E.png','F.png','G.jpg']),
          city=cities[random.randint(0,len(cities)-1)],
          team=teams[random.randint(0,len(teams)-1)],
          on_campus=random.randint(0,1),
      )
      time.sleep(random.randint(3,9))
#    print e
      e.save()

    self.stdout.write('Successfully added event "' + e.team.name + ' got ' + e.city.name + '"\n')

