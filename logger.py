
class Logger:
    last_id : str
    file = [None,None] #reading to 0, writing to 1
    file_content = None



    #initialise logger and access save file path
    def __init__(self):
        self.last_id = 'AAA00'
        self.read()

    #deconstructor: close the log file
    def __del__(self):
        try:
            if self.file[0]:
                print("reader destruct")
                self.file[0].close()
        except Exception:
            pass
        finally:
            if self.file[1]:
                print("writer destruct")
                self.file[1].close();


    def read(self):
        try:
            self.file[0] = open("log.txt","r")
            self.file_content = self.file[0].readlines()
            self.file[0].close()
        except FileNotFoundError:
            self.write()
            self.read()

    def write(self, content = None, index = True):
        if self.file[1] is None or self.file[1].closed:
            self.file[1] = open('log.txt', 'w')
        if content is None:
            self.write(self.last_id)
            self.file[1].close()
        else:
            if index:
                self.file[1].write(content + "\n"+ "\n".join(self.file_content)) #update the query results
            else:
                self.file[1].write(content + "\n".join(self.file_content[1:])) #update last request counter



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



