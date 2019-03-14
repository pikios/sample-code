# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACedb3b56153753f02d574b13a580e9cc7'
auth_token = 'bf595497196f4a948fcba2af185e7e1c'
client = Client(ACedb3b56153753f02d574b13a580e9cc7, bf595497196f4a948fcba2af185e7e1c)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+61488843000',
                     to='+61409351632'
                 )

print(message.sid)
