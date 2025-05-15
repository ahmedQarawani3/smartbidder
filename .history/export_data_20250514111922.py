 
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartbidder.settings')
django.setup()

from django.core.management import call_command

with open("full_data.json", "w", encoding="utf-8") as f:
    call_command('dumpdata',
                 exclude=['contenttypes', 'auth.Permission'],
                 indent=2,
                 stdout=f)
