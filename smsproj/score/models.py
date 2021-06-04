from django.db import models
from twilio.rest import Client

# Create your models here.


class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'AC9ddf07a5d433d08574f9d8354a3c80fa'
            auth_token = 'b4e5103890de0aea6d12d173bfed5b85'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"The Currnt result is bad - {self.result}",
                from_='+12025176718',
                to='+917069153857'
            )
            print(message.sid)
        return super().save(*args, **kwargs)
