import sys
import time
from twython import Twython, TwythonError
from io_helper import twitter_credential_prompt

# Requires Authentication as of Twitter API v1.1
(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = twitter_credential_prompt()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# All the available places for trends query
places = twitter.get_available_trends()
country_list = ['India']
places_of_interest = 0
trends_of_ineterest = set([])
places_list = []

for place in places:
	if (place['country'] in country_list) :
		print('Name: ', place['name'])
		print('-----------------------')
		places_of_interest += 1
		places_list.append(place)

print('places of interest count - ', len(places_list))

for place in places_list:
	trends_for_place = twitter.get_place_trends(id=place['woeid'])
	print('Got the trends for ', place['name'])
	trends_list = []
	i = 10
	for trend in trends_for_place[0]['trends']:
		trends_list.append(trend['name'])
		i -= 1
		if (i == 0) :
			break
	print(trends_list)		
	trends_of_ineterest |= set(trends_list)
	print(trends_of_ineterest)			
	time.sleep(60)