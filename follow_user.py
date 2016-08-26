import sys
from twython import Twython, TwythonError
from io_helper import twitter_credential_prompt
from io_helper import custom_prompt

# Optionally accept user data from the command line (or elsewhere).
#
# Usage:  follow_user.py ryanmcgrath

(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = twitter_credential_prompt()

prompt = "User to follow: "

if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    target = custom_prompt(prompt)

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    twitter.create_friendship(screen_name=target, follow="true")
except TwythonError as e:
    print(e)
