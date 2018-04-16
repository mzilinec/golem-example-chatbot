from django.db import models


class Reminder(models.Model):
    reminder_id = models.CharField("reminder_id", max_length=1024, primary_key=True)
    user_id = models.CharField("user_id", max_length=1024)
    chat_id = models.CharField("chat_id", max_length=1024)
    text = models.CharField("text", max_length=1024)
    when = models.DateTimeField("when")
