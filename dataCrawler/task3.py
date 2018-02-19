from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=#*************************
consumer_secret=#*************************

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=#**************************
access_token_secret=#*********************

class keywordListener(StreamListener):
	def on_status(self, status):
#		print(status.text)
		count = 0
		while (count < 50):
			with open('task3-1.txt', 'a') as f:
				f.write(status.text.encode('utf8')+'\n')
				count = count + 1
		f.close()
		return False

	def on_error(self, status):
		print(status)

class locationListener(StreamListener):
	def on_status(self, status):
#		print(status.text)
		count = 0
		while (count < 50):
			with open('task3-2.txt', 'a') as f:
				f.write(status.text.encode('utf8')+'\n')
				count = count + 1
		f.close()
		return False

	def on_error(self, status):
		print(status)

if __name__ == '__main__':
	l = keywordListener()
	m = locationListener()

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	lstream = Stream(auth, m)
	lstream.filter(locations=[-86.33,41.63,-86.20,41.74])

	kstream = Stream(auth, l)
	kstream.filter(track=['Indiana', 'weather'])
