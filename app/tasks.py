import logging
import json
import datetime
import pytz
from django.urls import reverse
from Mealy.celery import app

from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from . import models
 
account_sid = "AC754bf0a55f1e001822c1cbcd1bade051"
auth_token  = "4c92735fd0235c018ae7355022e37339"

@app.task
def send_recipe_reminder():
    # Get current time
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    currentTime = utc_now.astimezone(pytz.timezone("America/New_York"))
    logging.info(currentTime)

    # Get info we need from current time
    dateIndex = currentTime.weekday()
    currentHHMM = currentTime.strftime('%H:%M')
    logging.debug(currentHHMM)

    # Look at each user
    users = models.UserInfo.objects.all()
    for user in users:
        logging.debug(str(user))

        # Make sure they have a phone number
        phoneNumber = user.cell
        if not phoneNumber:
            logging.debug('User has no phone number')
            continue
        logging.debug(phoneNumber)

        # Make sure they have a meal dict
        mealDictString = str(user.mealDict)
        if not mealDictString:
            logging.debug('User has no meal dict')
            continue
        mealDict = json.loads(mealDictString) # get meal dictionary

        # Send necessary reminders
        check_for_text_reminder(phoneNumber, user.breakTime, mealDict, 'breakfasts', dateIndex, 'breakfast', currentHHMM)
        check_for_text_reminder(phoneNumber, user.lunchTime, mealDict, 'lunches', dateIndex, 'lunch', currentHHMM)
        check_for_text_reminder(phoneNumber, user.dinnerTime, mealDict, 'dinners', dateIndex, 'dinner', currentHHMM)

def check_for_text_reminder(phoneNumber, specifiedMealTime, fullMealDict, mealDictKey, dateIndex, mealName, currentHHMM):
    if specifiedMealTime and mealDictKey in fullMealDict.keys():
        specifiedMealTimeHHMM = specifiedMealTime.strftime('%H:%M')
        logging.debug('Specified ' + mealName + ' time: ' + specifiedMealTimeHHMM)
        mealDatetime = datetime.datetime.strptime(specifiedMealTimeHHMM, '%H:%M')
        mealDict = fullMealDict[mealDictKey][dateIndex]
        mealMinutes = mealDict['minutes']
        logging.debug('Ready in time: ' + str(mealMinutes))
        startCookingHHMM = (mealDatetime - datetime.timedelta(minutes=mealMinutes)).strftime('%H:%M')
        logging.debug('Time to start cooking: ' + startCookingHHMM)
        if startCookingHHMM == currentHHMM:
            logging.debug('Send a text for ' + mealName)
            send_text_message(phoneNumber, mealDict, mealName)
        else:
            logging.debug('No text to send for ' + mealName)
    else:
        logging.debug('No specified ' + mealName + ' time or meals')

def send_text_message(phoneNumber, mealDict, mealName):
    # Create new texting client
    client = Client(account_sid, auth_token)

    # Send message with meal info
    message = client.messages.create(
        to='+1' + phoneNumber, 
        from_="+12166665780",
        body="Hey there! It's time to start preparing your %s from Mealy! Here is your recipe:\n\n%s\n\nRating: %s/5\nReady in: %d min\nCals: %s\n\nIngredients:\n%s\n\nInstructions:\n%s" % (mealName, mealDict['title'], str(round(mealDict['rating'], 2)), mealDict['minutes'], mealDict['calories'], str(mealDict['ingredients']).replace('[\'','-').replace('[','-').replace('"', '').replace('\']','').replace(']','').replace("\', \'",'\n-').replace(", \'",'\n-'), mealDict['instructions'] ))