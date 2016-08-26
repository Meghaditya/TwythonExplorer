from twython import Twython, TwythonError
from io_helper import twitter_credential_prompt
from io_helper import custom_prompt

# Requires Authentication as of Twitter API v1.1
(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = twitter_credential_prompt()
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    query = custom_prompt("Query : ")
    c = custom_prompt("Count : ")
    search_results = twitter.search(q=query, count=c)
except TwythonError as e:
    print(e)

# print(search_results)

for tweet in search_results['statuses']:
    if (tweet['lang'] == 'en') :
        print('Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
        print(tweet['text'].encode('utf-8'), '\n')
    else :
        print('Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at']))
        print(tweet['lang'], '\n')
