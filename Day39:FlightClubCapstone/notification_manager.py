import twilio
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'id'
        self.auth_token = 'token'

    def send_notification(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            from_='num',
            body=f'Hello there',
            to='yournum'
        )
        print(message.status)
        print(message.sid)
