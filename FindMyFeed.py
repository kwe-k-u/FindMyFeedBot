import tweepy
from Query import Query



class FindMyFeedBot:
    #attributes
    api : tweepy.API #twitter api object
    query : Query #object for the search requests sent via the bots DM
    results : tweepy.cursor.Cursor #all the tweets on  timeline that match the search query


    #constructor
    def __init__(self, ap : tweepy.API):
        self.api = ap

    #seraches the user's feed for tweets that have the same keywork as the DM's query
    def search(self):
        print("searching..")

        status: tweepy.models.Status
        for status in tweepy.Cursor(self.api.user_timeline, id= self.query.sending_user, tweet_mode="extended").items():
            if self.query.query in status.full_text:
                self.replyWithTweet(status)

        print("search complete") #TODO send to user's dm?

    #replies the sender of a DM with the response for their search
    def replyWithTweet(self, response : tweepy.models.Status):
        print("replying tweet")
        message = "2 Found a tweet matching your query\nSent by @" + response.author.screen_name + "\nTweet content" + response.full_text
        self.api.send_direct_message(recipient_id= self.query.sending_user, text=message)
        print('reply successful')

    def deleteRequest(self):
        print("deleting request " + self.query.id)
        self.api.destroy_direct_message(self.query.id)
        print('delete successful')

    def execute (self, dm : tweepy.DirectMessage):
        #parse query
        self.query = Query(dm)
        self.search()
        #log
        # self.deleteRequest() TODO activate
        print()

