#! python3

#Kivy used for GUI
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

#Reddit scraping
import redditScraping as rs


class PostDisplay(Widget):
	titleLabel = ObjectProperty()
	thumbImage = ObjectProperty()

	def __init__(self, post):
		super(PostDisplay, self).__init__()

		self.post = post
		self.buildDisplay()

	def buildDisplay(self):
		#text
		self.titleLabel.text = self.post.title
		
		#thumbnail
		self.thumbImage.source = self.post.thumbnail

class PostManager(BoxLayout):
	def __init__(self, **kwargs):
		super(PostManager, self).__init__(**kwargs)

		self.posts = []
		self.postDisplays = []

	def addPost(self, post):
		self.posts.append(post)
		self.addPostDisplay(PostDisplay(post))

	def addPostDisplay(self, postDisplay):
		self.postDisplays.append(postDisplay)
		self.add_widget(postDisplay)

		#add everything needed from the postDisplay
'''		#outline box
		with self.canvas:
			Color(1, 0, 0, 1)
			Rectangle(pos=postDisplay.titleLabel.pos, size=postDisplay.titleLabel.size)'''

		#label
		


class ReaderBase(FloatLayout):
	def __init__(self):
		super(ReaderBase, self).__init__()

		self.scraper = rs.Scraper()
		self.postManager = PostManager(orientation='vertical')
		self.add_widget(self.postManager)

		self.generatePosts()

	def generatePosts(self):
		subreddit = self.scraper.reddit.subreddit("all")
		displayCount = 10

		for i in subreddit.hot(limit=displayCount):
			self.postManager.addPost(i)

class ReaderApp(App):
	def build(self):
		reader = ReaderBase()

		return reader

if __name__ == '__main__':
	ReaderApp().run()