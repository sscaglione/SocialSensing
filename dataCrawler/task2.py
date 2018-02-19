from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=#**********************
consumer_secret=#*********************

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=#**********************
access_token_secret=#*****************

# Actual OAuth Process, using he keys and tokens provided
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userList = [34373370, 26257166, 12579252]

f = open("task2.txt", "w")

for item in userList:
	user = api.get_user(item)
	sn = user.screen_name
	f.write('{}\n\n'.format(sn))
	f.write('The Friends List:\n\n')
	for friend in user.friends():
		fsn = friend.screen_name
		f.write('{}\n'.format(fsn))
	f.write('\n')
	f.write('The Followers List:\n\n')
	for follower in user.followers():
		fsn = follower.screen_name
		f.write('{}\n'.format(fsn))
	f.write('\n\n\n')
	
f.close()
