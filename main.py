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

class PostManager(RecycleView):
	layout = ObjectProperty()
	rv_data = ListProperty()

	currSub = "all"

	def __init__(self, scraper):
		super(PostManager, self).__init__()

		self.posts = []
		self.scraper = scraper
		self.subreddit = self.scraper.reddit.subreddit(self.currSub)
		self.currPost = iter(self.subreddit.hot(limit=None))

		#generate initial 50 posts
		self.generatePosts(50)

	def generatePosts(self, postN):
		for i in range(postN):
			self.addPost(next(self.currPost))

	def addPost(self, post):
		self.posts.append(post)
		self.addPostDisplay(post)

	def addPostDisplay(self, post):
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
		self.postManager = PostManager(self.scraper)
		self.add_widget(self.postManager)

class ReaderApp(App):
	def build(self):
		reader = ReaderBase()
		return reader

if __name__ == '__main__':
	ReaderApp().run()