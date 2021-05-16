import tweepy

#template for the queries sent to the bot via DM
class Query:
    query_type :str #the type of the query 'search'
    query :str #keywords that are to be searched
    sending_user :str #the user sending the query


    #constructor
    def __init__(self, dm: tweepy.DirectMessage):

        # parses the dm request by breaking it into its components
        def parseDM(message):
            query: str
            query = message.message_create['message_data']['text']  # get the text in the message
            # index key
            # 0 -> query type '#search'
            # 1 -> query keywords
            # 2 -> user who sent the tweet
            # 3 -> mulitmedia should be included? 'include pictures'

            return query.strip().split("\n")


        params = parseDM(dm)
        self.query = params[1]
        self.query_type = params[0].replace("#","")
        self.sending_user = dm.message_create['sender_id']

