from twython import Twython, TwythonError
from io_helper import twitter_credential_prompt
from io_helper import custom_prompt

# Requires Authentication as of Twitter API v1.1
(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)= twitter_credential_prompt()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    screen_name_input = custom_prompt("Screen name: ")
    count_input = custom_prompt("Count: ")
    user_timeline = twitter.get_user_timeline(screen_name=screen_name_input, count=count_input)
except TwythonError as e:
    print(e)

for tweet in user_timeline:
    print('\(id)=%s \n%s\n' % (tweet['id'],tweet['text']))
    
