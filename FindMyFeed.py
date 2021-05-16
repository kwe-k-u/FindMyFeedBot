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


# parses the dm request by breaking it into its components
# def parseDM(message):
#     query: str
#     query = message.message_create['message_data']['text']  # get the text in the message
#     # index key
#     # 0 -> query type '#search'
#     # 1 -> query keywords
#     # 2 -> user who sent the tweet
#     # 3 -> mulitmedia should be included? 'include pictures'
#
#     return query.strip().split("\n")

#searches the user's feed looking for messages that have the passed keywords
def search(query :Query):

    # searching a user's feed
    status: tweepy.models.Status
    for status in tweepy.Cursor(api.user_timeline, id=query.sending_user, tweet_mode="extended").items():
        if query.query in status.full_text:  # remove the split in production
            print(status)
            break


#connecting to twitter api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#finding direct messages that contain search parameters
dm = api.list_direct_messages()
# print("dms ")
# print(dm)
# print("Features")
# print(dm[0].__dict__.keys())
# searchQuery = api.search("@feed_find")
# print(searchQuery[0].__dict__.keys())

#parsing text
#TODO loop through all dms
params : Query
params = Query(dm[0])
#searching a user's feed

status : tweepy.models.Status
for status in tweepy.Cursor(api.user_timeline, id=params.sending_user, tweet_mode="extended").items():
    if params.query in status.full_text: # remove the split in production
        print(status)
        break



