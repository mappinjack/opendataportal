

from flask import Flask, request, render_template
from watson_developer_cloud import ConversationV1
from keys import apiKeys
#import apiKeys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/askWatson', methods=['POST', 'GET'])
def askWatson():
	user_input = request.args.get('jsdata')

	conversation = ConversationV1(
	username= apiKeys["username"],
	password= apiKeys["password"],
	version= apiKeys["version"])

	workspace_id = apiKeys["workspace_id"]
	context = {}

	response = conversation.message(
		workspace_id = workspace_id,
		input = {
		'text': user_input
		},
		context = context)

	# If an intent was detected, print it to the console.
	if response['intents']:
		print('Detected intent: #' + response['intents'][0]['intent'])

	# Print the output from dialog, if any.
	if response['output']['text']:
		processed_text = response['output']['text'][0]
	
	# Update the stored context with the latest received from the dialog.
	context = response['context']
	print('Detected entities: ' + str(response['entities']))
	#print 'Intents: ' + str(response['intents'])
	#print response
	# Prompt for next round of input.
	# processed_text = text.upper()
	return '<p>'+processed_text+'</p>' 
