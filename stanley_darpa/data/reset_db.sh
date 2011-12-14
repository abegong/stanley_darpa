#!/bin/bash
cd /opt/bitnami/apps/django/django_projects/Project
python manage.py reset stanley_darpa --noinput
python manage.py loaddata stanley_darpa/data/cities.json 
python manage.py loaddata stanley_darpa/data/teams.json 
python manage.py syncdb

