import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.phone_number = os.environ.get("TWILIO_NUMBER")
        self.account_sid = os.environ.get("TWILIO_SID")
        self.auth_token = os.environ.get("TWILIO_TOKEN")
        self.to_phone_number = os.environ.get("TO_PHONE_NUMBER")

    def send_message(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                body=message,
                from_=self.phone_number,
                to=self.to_phone_number
            )
        print(message.status)