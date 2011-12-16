import glob, random, time
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


from settings import STATIC_ROOT, MEDIA_ROOT
from stanley_darpa.models import City, Event, Team

class Command(BaseCommand):
  args = '< >'
  help = 'Adds a random event'

  def handle(self, *args, **options):
    call_command('flush', interactive=False)
    call_command('loaddata', '/opt/bitnami/apps/django/django_projects/Project/stanley_darpa/data/cities.json')
    call_command('loaddata', '/opt/bitnami/apps/django/django_projects/Project/stanley_darpa/data/teams.json')
