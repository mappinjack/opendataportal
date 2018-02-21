

from flask import Flask, request, render_template, redirect
from watson_developer_cloud import ConversationV1
from keys import apiKeys
from dataDict import dataDict
#import apiKeys

app = Flask(__name__)

context = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/askWatson', methods=['POST', 'GET'])
def askWatson():
	global context
	user_input = request.args.get('jsdata')

	conversation = ConversationV1(
	username= apiKeys["username"],
	password= apiKeys["password"],
	version= apiKeys["version"])

	workspace_id = apiKeys["workspace_id"]

	#print("Context in: " + str(context))
	response = conversation.message(
		workspace_id = workspace_id,
		input = {
		'text': user_input
		},
		context = context)
	
	# Context is used to maintain the conversation between each API call
	context = response['context']
	# Output is a dict with a variety of keys, notable 'intents', 'text', 'action'
	output = response['output']
	# List of Watson identified intents
	intents = response['intents'] if response['intents'] else None
	# List of Watson identified entities
	entities = response['entities'] if response['entities'] else None

	# Print the output from dialog, if any.
	moreInfo = None
	outputText = output['text'][0] if output['text'] else "No text returned"
	action = output['action'] if 'action' in output else None

	if action == 'download':
		dataset = output['dataset']
		dlFormat = output['format']
		moreInfo = dataDict[dataset]['downloadUrls'][dlFormat]

	# This will return the response.html template with variables
	return render_template('response.html', outputText = outputText, action = action, moreInfo = moreInfo)

