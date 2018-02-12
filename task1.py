from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= #***********************
consumer_secret= #**********************

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token= #*******************
access_token_secret=#*****************

# Actual OAuth Process, using he keys and tokens provided
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userList = [34373370, 26257166, 12579252]

f = open("task1.txt", "w")

for item in userList:
	user = api.get_user(item)
	sn = user.screen_name
	f.write('Screen Name: {}\n'.format(sn))
	un = user.name
	f.write('User Name: {}\n'.format(un))
	loc = user.location
	f.write('User Location: {}\n'.format(loc))
	desc = user.description
	f.write('User Description: {}\n'.format(desc))
	numFol = user.followers_count
	f.write('The Number of Followers: {}\n'.format(numFol))
	numFri = user.friends_count
	f.write('The Number of Friends: {}\n'.format(numFri))
	numStat = user.statuses_count
	f.write('The Number of Statuses: {}\n'.format(numStat))
	usURL = user.url
	f.write('User URL: {}\n'.format(usURL))
	f.write('\n')

f.close()
