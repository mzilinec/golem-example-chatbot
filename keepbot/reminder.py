import logging
import uuid
from datetime import datetime, timedelta


def create_reminder(uid, text, dt):
    from keepbot.models import Reminder
    reminder_id = uuid.uuid4().hex
    reminder = Reminder(reminder_id=reminder_id, text=text, when=dt, user_id=uid, chat_id=uid)
    reminder.save()
    return reminder_id


def cancel_reminder(uid, reminder_id):
    from keepbot.models import Reminder
    try:
        reminder = Reminder.objects.get(reminder_id__exact=reminder_id, user_id__exact=uid)
        reminder.delete()
        return True
    except Reminder.DoesNotExist:
        return False


def get_reminder(uid, reminder_id):
    from keepbot.models import Reminder
    return Reminder.objects.get(reminder_id__exact=reminder_id, user_id__exact=uid)


def fire_reminders():
    try:
        from keepbot.models import Reminder
        from golem.tasks import fake_move_to_state
        now = datetime.now()
        Reminder.objects.filter(when__lte=now - timedelta(days=1)).delete()  # delete old objects
        past = Reminder.objects.filter(when__lte=now).all()
        for reminder in past:
            ents = (("reminder_id", reminder.reminder_id), ("reminder_text", reminder.text))
            chat_id = reminder.chat_id
            fake_move_to_state(chat_id, state="remind.fire:", entities=ents)
    except:
        logging.exception("Exception while firing events")
