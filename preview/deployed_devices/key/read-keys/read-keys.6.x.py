# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

keys = client.preview.deployed_devices \
                     .fleets('FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .keys \
                     .list()

for record in keys:
    print(record.sid)
