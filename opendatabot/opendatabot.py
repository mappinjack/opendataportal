

from flask import Flask, request, render_template, redirect
from watson_developer_cloud import ConversationV1
from keys import apiKeys
from dataDict import dataDict
import requests
import json
import requests


app = Flask(__name__)

context = {}
counter = 0

@app.route('/chat')
def chat():
    return render_template('home.html')

@app.route('/help')
def help():
	return render_template('help.html')

@app.route('/about')
def about():
	return render_template('about.html')

## Update to home page
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/askWatson', methods=['POST', 'GET'])
def askWatson():
	global context
	global counter
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
	# Counter for uIds

	# Print the output from dialog, if any.
	moreInfo = None
	outputText = output['text'][0] if output['text'] else "No text returned"
	action = output['action'] if 'action' in output else None

	# Set up downloads HTML to allow JS to handle this in-browser
	if action == 'download':
		dataset = output['dataset']
		dlFormat = output['format']
		moreInfo = dataDict[dataset]['downloadUrls'][dlFormat]

	# Call ArcGIS REST endpoint to retrieve metadata
	# TODO - make sure all formats are available for all datatypes
	elif action == 'metadata':
		dataset = output['dataset']
		metaUrl = dataDict[dataset]['metaUrl']
		r = requests.get(metaUrl)
		metadata = r.json()
		description = metadata['description']
		wkid = metadata['spatialReference']['wkid']
		return render_template('metadata.html', outputText = outputText, description = description, wkid = wkid)

	elif action == 'showOnMap':
		counter += 1
		dataset = output['dataset']
		endpoint = dataDict[dataset]['endpoint']
		popupFields = json.dumps(dataDict[dataset]['popupFields'])
		return render_template('showOnMap.html', outputText = outputText, endpoint = endpoint, popupFields = popupFields, counter = str(counter))

	# Return datasets
	elif action == 'listDatasets':
		datasetList = ''
		for key in dataDict:
			datasetList += key +', '
		outputText += ' ' + datasetList.strip(', ')

	elif action == 'attributes':
		dataset = output['dataset']
		attributesUrl = dataDict[dataset]['attributesUrl']
		r = requests.get(attributesUrl).json()
		attributes = r['layers'][0]['fields']

		return render_template('attributes.html', outputText = outputText, attributes = attributes)
	# This will return the response.html template with variables
	# Action iand moreInfo are in a hidden <p> element to allow for JavaScript processing
	return render_template('response.html', outputText = outputText, action = action, moreInfo = moreInfo)

