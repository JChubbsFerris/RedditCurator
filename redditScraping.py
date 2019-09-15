#! python3

import praw
#import panda
#import datetime

import requests

#Class for handling reddit scraping
class Scraper:
	def __init__(self):
		self.reddit = praw.Reddit(client_id='ex4ZpcDjayCTWg', client_secret=None, user_agent='ML Reader', redirect_uri='http://localhost:8080')
		self.authenticate()

	def authenticate(self):
		pass
		#TODO: allow users to sign in (allows activity such as commenting and voting)

		'''
		#TODO: listen to localhost:8080 to retrieve code for auth
		#generate access url
		scopes = ["identity"]
		state = "test"
		accessUrl = self.reddit.auth.url(scopes, state, duration='temporary')

		#open url
		import webbrowser
		webbrowser.open_new(accessUrl)
		'''
