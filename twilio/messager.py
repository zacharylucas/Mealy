from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

account_sid = "AC754bf0a55f1e001822c1cbcd1bade051"
auth_token  = "4c92735fd0235c018ae7355022e37339"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14403966072", 
    from_="+12166665780",
    body="Hey there! It's time to start preparing you meal from Mealy! Here is the link to your recipe: https://www.allrecipes.com/recipe/31087/")

print(message.sid)