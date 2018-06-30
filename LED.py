#queries for TSLA

import requests #imports for API
import json
import pprint

import time #imports for LED functionality
import RPi.GPIO as GPIO


url = "https://www.alphavantage.co/query" #API

function = "TIME_SERIES_DAILY" #specifies daily queries
symbol = "TSLA" #Tesla
api_key = "2CA60174FYOCPHAM"

data = { "function": function, 
         "symbol": symbol, 
         "apikey": api_key }

page = requests.get(url, params = data) #gets data from API
results = page.json() #stores as json
today = results.get('Meta Data').get('3. Last Refreshed') #stores the most recent date of accessing API
info = results.get('Time Series (Daily)').get(today) #stores open, high, low, close, and volume

#sets up GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT) #red light
GPIO.setup(15, GPIO.OUT) #green light

def isUp(): #checks if stock closed higher than it opened
	if float(info.get('1. open')) > float(info.get('4. close')):
		return False
	else:
		return True

def LED():
	if isUp():
		GPIO.output(15, True)
	else:
		GPIO.output(3,True)	
