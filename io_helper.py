import sys
import json

# helper method to create input for twitter credentials
# handles both Python 2.x and 3.x
# parses the data from a file for avoiding repeated prompts
# file format is chosen as json for quick parsing
#
# returns a tuple containing the credentials
def twitter_credential_prompt():
	f = open('creds.json','r')
	x = json.load(f)
	return (x['APP_KEY'], x['APP_SECRET'], x['OAUTH_TOKEN'], x['OAUTH_TOKEN_SECRET'])

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