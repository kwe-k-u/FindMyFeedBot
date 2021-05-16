import tweepy
from Query import Query
from os import environ
from FindMyFeed import FindMyFeedBot
from dotenv import load_dotenv

#TODO create log for all results using AA000 as a marker
#TODO the user should be able to refer to the found tweet and then have the bot refer the user to that tweet
#twitter api doesn't let user's send tweets in direct messages
#TODO multithreading; seraching, replying, logs




# loading environment variables
load_dotenv()
CONSUMER_KEY = environ.get('CONSUMER_KEY')
CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
ACCESS_KEY = environ.get('ACCESS_KEY')
ACCESS_SECRET = environ.get('ACCESS_SECRET')

# authenticating with twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


#instantiating bot
bot : FindMyFeedBot
bot = FindMyFeedBot(api)

#finding direct messages that contain search parameters
dm = api.list_direct_messages()
#TODO loop through all dms


bot.execute(dm[0])

