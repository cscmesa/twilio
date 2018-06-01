# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from user import AUTH_TOKEN


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACf824fa46a92b6afe417c068e17d31488'
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+18582951380',
                              to='+17607129793'
                          )

print(message.sid)
