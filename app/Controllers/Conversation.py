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

def sendInitialMessage():
    inputMessage = {'text': ''}
    response = conversation.message(workspace_id = workspace_id, input = inputMessage)
    #context = response['context']
    #print(response)
    return response

def sendMessage(message, context):
    message = re.sub('[\r\t\n]', '', message)
    inputMessage = {'text': message}
    response = conversation.message(workspace_id = workspace_id, input = inputMessage, context = context)
    #print(response)
    return response

'''
context = sendInitialMessage()
while(True):
    message = input("")
    context = sendMessage(message, context = context)
'''
