import os
from dotenv import load_dotenv


class Logger:
    last_id : str



    #initialise logger and access save file path
    def __init__(self):
        self.last_id = 'AAA00'



    def read(self):
        print()

    def write(self):
        print()

    def next_id(self):

        #increases the passed character by 1
        def increaseChar(c):
            return chr( ord(c)+1 )


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
            self.last_id = self.last_id[:-1] + increaseChar(self.last_id[-1])



