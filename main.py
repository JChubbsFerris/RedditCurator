#! python3

#Kivy used for GUI
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock

#Reddit scraping
import redditScraping as rs


class PostDisplay(Widget):
	pass
'''
	titleLabel = ObjectProperty()
	scoreLabel = ObjectProperty()
	authLabel = ObjectProperty()
	subLabel = ObjectProperty()
	thumbImage = ObjectProperty()

	def __init__(self, post):
		super(PostDisplay, self).__init__()

		self.post = post
		#self.buildDisplay()

	def buildDisplay(self):
		#title
		#self.titleLabel.text = self.post.title

		#score
		#self.scoreLabel.text = str(self.post.score)

		#author
		#self.authLabel.text = self.post.author.name

		#subreddit
		#self.subLabel.text = "on r/" + self.post.subreddit.display_name


		#thumbnail
		thumb = self.post.thumbnail
		if 'https' in thumb:
			self.thumbImage.source = self.post.thumbnail
		else:
			self.thumbImage.source = None
			self.thumbImage.opacity = 0

		prod = {'title': {'text': self.post.title}, 'score': {'text': (self.post.score)}, 'author': {'text': self.post.author.name}}

		return prod'''

class PostManager(RecycleView):
	layout = ObjectProperty()
	rv_data = ListProperty()

	def __init__(self):
		super(PostManager, self).__init__()

		self.posts = []
		self.postDisplays = []

	def addPost(self, post):
		self.posts.append(post)
		self.addPostDisplay(post)

	def addPostDisplay(self, post):
		self.postDisplays.append(post)
		newDisplay = {}
		newDisplay['titleText'] = post.title
		newDisplay['scoreText'] = str(post.score)
		newDisplay['authText'] = post.author.name
		newDisplay['subText'] = "on r/" + post.subreddit.display_name
		#thumbnail
		thumb = post.thumbnail
		if 'https' in thumb:
			thumbSource = post.thumbnail
		else:
			thumbSource = ''
			thumbOpacity = 0
		newDisplay['thumbSource'] = thumbSource

		self.rv_data.append(newDisplay)


class ReaderBase(FloatLayout):
	def __init__(self):
		super(ReaderBase, self).__init__()

		self.scraper = rs.Scraper()
		self.postManager = PostManager()
		self.add_widget(self.postManager)

		self.generatePosts()

	def generatePosts(self):
		subreddit = self.scraper.reddit.subreddit("all")
		displayCount = 100

		for i in subreddit.hot(limit=displayCount):
			self.postManager.addPost(i)

class ReaderApp(App):
	def build(self):
		reader = ReaderBase()

		return reader

if __name__ == '__main__':
	ReaderApp().run()