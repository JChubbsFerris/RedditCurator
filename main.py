#! python3

#Kivy used for GUI
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

#Reddit scraping
import redditScraping as rs

class PostDisplay(Widget):
	def __init__(self, post):
		super(PostDisplay, self).__init__()

		self.post = post
		self.buildLabel()

	def buildLabel(self):
		self.postLabel = Label(text = self.post.title)

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

		#add everything needed from the postDisplay
		self.add_widget(postDisplay.postLabel)


class ReaderBase(Widget):
	def __init__(self):
		super(ReaderBase, self).__init__()

		self.scraper = rs.Scraper()
		self.postManager = PostManager(orientation='vertical')

		self.generatePosts()

	def generatePosts(self):
		subreddit = self.scraper.reddit.subreddit("all")
		displayCount = 10

		for i in subreddit.hot(limit=displayCount):
			self.postManager.addPost(i)

class ReaderApp(App):
	def build(self):
		reader = ReaderBase()

		return reader.postManager

if __name__ == '__main__':
	ReaderApp().run()