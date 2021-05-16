import tweepy
from Query import Query
import os
from dotenv import load_dotenv

#constants
load_dotenv() #getting the keys from the .env file
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")



#searches the user's feed looking for messages that have the passed keywords
def search(query :Query):
    print("searching...")
    # searching a user's feed
    status: tweepy.models.Status
    for status in tweepy.Cursor(api.user_timeline, id= query.sending_user, tweet_mode="extended").items():
        if query.query in status.full_text:  # remove the split in production
            replyWithTweet(status)
    print('search complete')



#replies the sender of the tweet with a response for their search
def replyWithTweet(response: tweepy.models.Status):
    print("replying tweet")
    message = "2 Found a tweet matching your query\nSent by @" + response.author.screen_name + "\nTweet content" + response.full_text
    api.send_direct_message( recipient_id= params.sending_user, text= message)
    print('reply successful')
#TODO create log for all results using AA000 as a marker

def deleteRequest():
    print('delete request ' + params.id)
    api.destroy_direct_message(params.id)
    print('success')






#connecting to twitter api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#finding direct messages that contain search parameters
dm = api.list_direct_messages()

#parsing text
#TODO loop through all dms
params : Query
params = Query(dm[0])
#searching a user's feed
search(params)
#
# status : tweepy.models.Status
# for status in tweepy.Cursor(api.user_timeline, id=params.sending_user, tweet_mode="extended").items():
#     if params.query in status.full_text: # remove the split in production
#         replyWithTweet(status)


#delete dm to prevent duplication of search
# deleteRequest()

#TODO the user should be able to refer to the found tweet and then have the bot refer the user to that tweet
#twitter api doesn't let user's send tweets in direct messages


