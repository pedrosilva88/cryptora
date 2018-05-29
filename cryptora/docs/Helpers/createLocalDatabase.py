#!/usr/bin/env python
from subprocess import call
import os

os.chdir('../../cryptora')
os.system('./manage.py dumpdata > ../docs/Helpers/db.json')
os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
os.system('find . -path "*/migrations/*.pyc" -delete')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('./manage.py loaddata ../docs/Helpers/db.json')
