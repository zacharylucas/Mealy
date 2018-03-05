from watson_developer_cloud import ConversationV1
import json
import re

conversation = ConversationV1(
    username = '722ba9a0-4ccc-400e-bc30-648d073cbb80',
    password = 'zXHJrakgKtw1',
    version = '2018-02-16'
)

workspace_name = 'Chatbot'
workspace_id = '0053d8c4-64cc-4f83-b0b3-39be8c6e5a0f'

def sendMessage(message):
    message = re.sub('[\r\t\n]', '', message)
    inputMessage = {'text': message}
    response = conversation.message(workspace_id = workspace_id, input = inputMessage)
    print(response)

print("Talk to bot")
while(True):
    message = input("")
    sendMessage(message)
