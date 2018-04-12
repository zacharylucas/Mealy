import logging
 
from django.urls import reverse
from Mealy.celery import app

from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from . import models
 

@app.task
def send_recipe_reminder():
    try:
        #will need to make a for loop over all users
        account_sid = "AC754bf0a55f1e001822c1cbcd1bade051"
        auth_token  = "4c92735fd0235c018ae7355022e37339"

        client = Client(account_sid, auth_token)

        users = models.UserInfo.objects.all()

        message = client.messages.create(
            to='+14403966072', 
            from_="+12166665780",
            body="Hey there! It's time to start preparing you meal from Mealy! Here is your recipe:\n\n")
    except:
        logging.warning("Tried to send text message user but failed")