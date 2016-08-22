#!/usr/bin/env python

try:
	import RPi.GPIO as GPIO
except:
	import sys
	print "You're not on a Raspberry Pi, exiting now"
	sys.exit(1)

try:
	import requests
except:
	print "Please run `pip install -r requirements.txt`"

import json
import os

# SLACK SETTINGS

SLACK_URL = "https://hooks.slack.com/services/XXXXXXX"
SLACK_CHANNEL = "#yourchannelname"

# RASPBERRY SETTINGS
BUTTON = 15 	# the pin the button is connected to

def start_pi():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(BUTTON, GPIO.IN, GPIO.PUD_UP)
	while True:
		if GPIO.input(BUTTON) == False:
			notify_slack()
	GPIO.cleanup()

def notify_slack():
	payload = {
		"username": "Slackbell",
		"icon_emoji": ":bellhop_bell:",
		"text": "Knock, Knock! There's someone at the door @channel",
		"channel": SLACK_CHANNEL
	}
	print "Attempting to post to Slack..."
	r = requests.post(SLACK_URL, data=json.dumps(payload))
	if r.status_code == requests.codes.ok:
		print "Successfully posted to Slack!"
		return True
	else:
		print "Oops! There was a problem posting to Slack:"
		print r.text
		return False

def main():
	print "Slack Doorbell activated"
	start_pi()

if __name__ == "__main__":
	main()