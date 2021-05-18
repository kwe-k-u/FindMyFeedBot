import tweepy
from os import environ
from FindMyFeed import FindMyFeedBot
from dotenv import load_dotenv
import time


#TODO create log for all results using AA000 as a marker
#TODO the user should be able to refer to the found tweet and then have the bot refer the user to that tweet
#twitter api doesn't let user's send tweets in direct messages
#TODO multithreading; searching, replying, logs, timer to keep bot within 50 seconds of operation
#TODO allow for querying of text from images
#TODO allow for querying of text from videos
#TODO filter searches to ones with and ones without images
#TODO find a way to include links to tweets/ tag user under the tweet and delete after a couple minutes


def main():
    # loading environment variables
    load_dotenv()
    CONSUMER_KEY = environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = environ.get('CONSUMER_SECRET')
    ACCESS_KEY = environ.get('ACCESS_KEY')
    ACCESS_SECRET = environ.get('ACCESS_SECRET')
    BOT_ID = environ.get('BOT_ID')


    while True:
        # time_check = time.time();
        print("Running program")
        # authenticating with twitter
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)


        #instantiating bot
        bot : FindMyFeedBot
        bot = FindMyFeedBot(ap= api,bot_id= str(BOT_ID))

        #finding direct messages that contain search parameters
        dm_list = api.list_direct_messages()
        for dm in dm_list:
            # if time.time() - time_check  > 50:
            #        pass
            bot.execute(dm)
        print("program end")
        time.sleep(2)

try:
    main()
except:
    main()