import twilio
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'yourid'
        self.auth_token = 'yourauth'

    def send_notification(self, update_cheap):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            from_='youtilnumber',
            body=f'{update_cheap}',
            to='yournumbervalidated'
        )
        print(message.status)
        print(message.sid)
