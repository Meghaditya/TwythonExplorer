from twython import TwythonStreamer
from io_helper import twitter_credential_prompt
from io_helper import custom_prompt

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)

# Requires Authentication as of Twitter API v1.1
(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) \
			= twitter_credential_prompt()
stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
track_keyword = custom_prompt('Stream keyword : ')

stream.statuses.filter(track=track_keyword)
# stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
# stream.site(follow='twitter')