import sys

# helper method to create prompt for twitter credentials
# handles both Python 2.x and 3.x
#
# returns a tuple containing the credentials

def twitter_credential_prompt():
	prompt = "\nEnter Twitter Credentials (Separated by comma)\nAPP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET\n:"

	if(sys.version_info < (3,0)):
		credentials = raw_input(prompt)
	else:	
	    # For Python 3.x use: target = input("User to follow: ")
	    credentials = input(prompt)

	(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = credentials.split(",")

	print(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	APP_KEY = APP_KEY.strip()
	APP_SECRET = APP_SECRET.strip()
	OAUTH_TOKEN = OAUTH_TOKEN.strip()
	OAUTH_TOKEN_SECRET = OAUTH_TOKEN_SECRET.strip()

	return (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# helper method to create prompt for custom entries
# handles both Python 2.x and 3.x
#
# returns the input entered

def custom_prompt(prompt_text):
	if(sys.version_info < (3,0)):
    	# For Python 2.x
	    target = raw_input(prompt_text)
	else:	
	    # For Python 3.x
	    target = input(prompt_text)
	return target