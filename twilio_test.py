# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC01287885945fe655e9803cc97fa59494"
auth_token = "58be1b286f4aad6bfbbb674f1160f9d6"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+18182749253",
                                             from_="+16506811977",
                                             body="I can! They're awful!")