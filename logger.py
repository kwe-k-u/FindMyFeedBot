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


        #if any of the index place values has reached an end, perform neccessary adjustments
        if self.last_id.__contains__("9") and self.last_id.__contains__("Z"):
            if self.last_id.endswith("9"):
                if self.last_id.endswith("99"): #if number space is full, increase letter
                    if not self.last_id.endswith("Z99"): #if last letter marker is not at end increase letter and reset numbers
                        self.last_id = self.last_id[:3] + "00"
                    else:
                        self.last_id = self.last_id[:-2]

        # if no place value is at end, increase smallest place value by 1
        else:
            self.last_id = self.last_id[:-1] + increaseChar(self.last_id[-1])



