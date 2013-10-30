from twilio.rest import TwilioRestClient
from django.http import HttpResponse

# Your Account Sid and Auth Token from twilio.com/user/account

def twilio(request):
    account_sid = "AC23c4932bf583f5006bb48d22342d1702"
    auth_token  = "ceb45f66b539b6e07be1933fbdaa1c8a"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.sms.messages.create(body="Testing Testing 1,2,3",
        to="+15104592120",    # Replace with your phone number
        from_="+15108580626") # Replace with your Twilio number
    print message.sid

    return HttpResponse('yo')