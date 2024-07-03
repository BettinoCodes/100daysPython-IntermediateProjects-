import twilio
from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'yourid'
        self.auth_token = 'yourtoken'
        self.my_email = "youremail"
        self.password = "yourpass"

    def send_notification(self, update_cheap):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            from_='twilionumber',
            body=f'{update_cheap}',
            to='yournumber'
        )
        print(message.status)
        print(message.sid)

    def send_email_notification(self, reciever, message):
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()

        connection.login(user=self.my_email, password=self.password)
        connection.sendmail(
            from_addr=self.my_email,
            to_addrs=reciever,
            msg=f"Subject:CHEAP FLIGHT DEAL\n\n{message}\nEnjoy,\n{yourname}"
        )

        connection.close()
