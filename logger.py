def increaseChar(c):
    return chr( ord(c)+1 )


class Logger:
    last_id : str #the last id(marker for query results) used
    file = [None,None] #reading to 0, writing to 1



    #initialise logger and access save file path
    def __init__(self):
        self.last_id = 'AAA00'
        self.read()




    def read(self):
        # read the content of the log file and update logger last_id

        try:
            self.file[0] = open("log.txt","r")
            self.last_id = self.file[0].readlines()[-1].split("-")[0].replace("\n","")
            self.file[0].close()
        except FileNotFoundError:
            self.writeLastId(" ")
            self.read()




       #log the assigned index to the last query result(tweet id)
    def writeIndex(self, content):
        #ensure writer is open
        if self.file[1] is None or self.file[1].closed:
            self.file[1] = open('log.txt', 'a')

        #if content is given, write it as an index
        if content is not None:
            self.file[1].write("\n" + self.last_id + "-" + content)
            self.next_id()

        self.file[1].close()


    #log the id for last query(DM)
    def writeLastId(self, tweet_id):

        # #if content is given, write it as an index
        if tweet_id is not None:
            #retrieving current content of file (removing last tweet id)
            temp = open("log.txt", 'r')
            temp.readline()
            prev = "\n" + "".join(temp.readlines())
            print(prev)

            temp.close()

            # #ensure writer is open
            if self.file[1] is None or self.file[1].closed:
                self.file[1] = open('log.txt', 'w')

            #if the file contains a history of logs
            self.file[1].write(tweet_id)
            self.file[1].write( prev)

            self.next_id()

        self.file[1].close()


    #increases the passed character by 1
    #generate the next search result index
    def next_id(self):



        #if any of the index place values has reached an end, perform necessary adjustments
        if self.last_id.__contains__("9"):
            if self.last_id.endswith("9"):
                if self.last_id.endswith("99"):
                    if self.last_id.__contains__("Z"):
                        if self.last_id[2:3] == "Z":
                            if self.last_id[1:3] == "ZZ":
                                if self.last_id[0:3] == "ZZZ":
                                    print("reached indexing limit")
                                    input("Bot haulted. Awaiting code improvements")
                                else:
                                    self.last_id = increaseChar(self.last_id[0])+ "AA00"
                            else:
                                self.last_id = self.last_id[0]+ increaseChar(self.last_id[1]) + "A00"
                        else:
                            self.last_id = self.last_id[0:2] + increaseChar(self.last_id[2]) + "00"
                    else:
                        self.last_id = self.last_id[0] + self.last_id[1] + increaseChar(self.last_id[2]) + "00"
                else:
                    self.last_id = self.last_id[:-2] + increaseChar(self.last_id[-2]) + "0"
            else:
                self.last_id = self.last_id[:-1] + increaseChar(self.last_id[-1])



        # if no place value is at end, increase smallest place value by 1
        else:
            self.last_id = self.last_id[0:4] + increaseChar(self.last_id[4])



