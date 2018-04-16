from golem.core.responses.buttons import PayloadButton
from golem.core.responses.responses import TextMessage

from keepbot.reminder import create_reminder, cancel_reminder, get_reminder


def set_reminder(dialog):
    dt = dialog.context.date_interval.last()[0]
    dt_formatted = dt.strftime("%H:%M %y/%m/%d")
    remind_text = dialog.context.reminder.last()
    dialog.context.clear(["datetime", "reminder"])
    msg = TextMessage("Cool! I will remind you to {} @ {} :)".format(remind_text, dt_formatted))
    reminder_id = create_reminder(dialog.uid, remind_text, dt)
    msg.add_button(
        PayloadButton(title="Cancel", payload={"_state": "remind.cancel:accept", "reminder_id": reminder_id}))
    dialog.send_response(msg, next='default.root')


def on_cancel(dialog):
    reminder_id = dialog.context.reminder_id.get()
    if cancel_reminder(dialog.uid, reminder_id):
        dialog.send_response("Reminder cancelled!", 'default.root', run_next=False)
    else:
        dialog.send_response("Sorry, that reminder doesn't exist anymore.", 'default.root')


def send_reminder(dialog):
    reminder_id = dialog.context.reminder_id.last()
    reminder = get_reminder(dialog.uid, reminder_id)
    text = "Reminder: {}".format(reminder.text)
    msg = TextMessage(text)
    msg.set_message_tag("NON_PROMOTIONAL_SUBSCRIPTION")
    reminder.delete()
    dialog.send_response(msg, 'default.root')
