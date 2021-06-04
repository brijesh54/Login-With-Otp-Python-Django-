import os
from twilio.rest import Client

account_sid = 'AC9ddf07a5d433d08574f9d8354a3c80fa'
auth_token = 'b4e5103890de0aea6d12d173bfed5b85'
client = Client(account_sid, auth_token)

def send_sms(user_code,phone_number):
    message = client.messages.create(
                    body=f"Hi, Your user and verification code is{user_code}",
                    from_='+12025176718',
                    to=f'{phone_number}'
                )
    print(message.sid)        
