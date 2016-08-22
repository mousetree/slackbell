Slack Doorbell
==============

Get a Slack notification when someone rings the doorbell.

[See it in action!](https://www.youtube.com/watch?v=91ABZbnGqrY).

## Requirements

* Raspberry Pi
* SSH access enabled on RPi

## Install

Copy the code onto the Raspberry Pi:

	ssh pi@192.168.1.x "mkdir -p /home/pi/slackbell"
	scp -r pi@192.168.1.x:/home/pi/slackbell ../slackbell

On the Raspberry Pi, install the requirements:

	pip install -r requirements.txt
	

## Usage

To manually startup the script run:

	python slackbell.py

To have the script startup automatically when the Pi turns on:

	sudo cp slackbell /etc/init.d/slackbell
	sudo chmod +x /etc/init.d/slackbell
	sudo update-rc.d /etc/init.d/slackbell defaults

You can then test the above by running:

	sudo /etc/init.d/slackbell start
	sudo /etc/init.d/slackbell stop

Also, make sure you're booting directly to the CLI by running:
	
	sudo raspi-config

