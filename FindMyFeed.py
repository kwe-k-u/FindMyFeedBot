import tweepy
from Query import Query
from logger import  Logger
from time import time


class FindMyFeedBot:
    #attributes
    api : tweepy.API #twitter api object
    query : Query #object for the search requests sent via the bots DM
    results : tweepy.cursor.Cursor #all the tweets on  timeline that match the search query
    logger : Logger
    bot_id : str

    #constructor
    def __init__(self, ap : tweepy.API, bot_id ):
        self.api = ap
        self.logger = Logger()
        self.bot_id = bot_id

    #runs for only 20 seconds
    #searches the user's feed for tweets that have the same keyword as the DM's query
    def search(self):
        start_time = time()
        print("searching..")#TODO send to user's dm?
        status: tweepy.models.Status
        for status in tweepy.Cursor(self.api.user_timeline, id= self.query.sending_user, tweet_mode="extended").items():

            #breaking search if it's run for longer than 20 seconds
            if time() - start_time > 20:
                break
            #found tweet matching query
            if self.query.query in status.full_text:
                self.logger.writeLastId(self.query.id) #log the tweet id
                self.logger.writeIndex(status.id_str)
                self.replyWithTweet(status) #reply user with the tweet

        print("search complete") #TODO send to user's dm?

    #replies the sender of a DM with the response for their search
    def replyWithTweet(self, response : tweepy.models.Status):
        print("replying tweet")
        message = self.logger.last_id + "\nFound a tweet matching your query\n\nSent by @" + response.author.screen_name + "\n\nTweet content\n" + response.full_text
        self.api.send_direct_message(recipient_id= self.query.sending_user, text=message)
        print('reply successful')
        self.logger.next_id()

    def deleteRequest(self):
        print("deleting request " + self.query.id)
        self.api.destroy_direct_message(self.query.id)
        print('delete successful')

    #executes the search of a query
    def execute (self, dm : tweepy.DirectMessage):

        #parse query
        self.query = Query(dm)
        print("sending user:" + self.query.sending_user + " "+ str(self.query.sending_user != self.bot_id))
        if self.query.sending_user != self.bot_id: #run if the dm isn't from the bot
            # self.logger.write(content= self.query.id, index= False)
            self.search()
        else:
            self.logger.writeLastId(self.query.id)#log the id of the message the bot sent to reduce repetition
        #log
        # self.deleteRequest() TODO activate:: is it still relevant? logger solves duplication issue




