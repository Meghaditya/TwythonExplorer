from twython import Twython, TwythonError
from io_helper import twitter_credential_prompt
from io_helper import custom_prompt

# Requires Authentication as of Twitter API v1.1
(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) \
			= twitter_credential_prompt()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    twitter.update_status(status='See how easy this was?')
except TwythonError as e:
    print(e)
