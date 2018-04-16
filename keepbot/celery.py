import os
from celery import Celery

from golem.tasks import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'keepbot.settings')

redis_url = settings.GOLEM_CONFIG.get("REDIS_URL")
print("Redis URL is", redis_url)

app = Celery('keepbot', backend='redis', broker=redis_url)
app.conf.update(BROKER_URL=redis_url,
                CELERY_RESULT_BACKEND=redis_url)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, reminder_loop.s(), name='check and send reminders every 60 seconds')


@app.task()
def reminder_loop():
    from keepbot.reminder import fire_reminders
    fire_reminders()
