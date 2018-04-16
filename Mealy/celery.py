import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mealy.settings')
 
app = Celery('Mealy')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
 
app.conf.beat_schedule = {
    'send-recipe-reminder-every-single-minute': {
        'task': 'app.tasks.send_recipe_reminder',
        'schedule': crontab(),  # crontab() with no arguments means run every minute
    },
}