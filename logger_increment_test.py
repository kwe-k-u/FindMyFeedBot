from logger import  Logger

log = Logger()


index = 0;
# index = 1627598;
# log.last_id = 'ZAA99'

while True:
    print(log.last_id)
    log.next_id()
    index +=1
    if log.last_id == "AZZ99" or index >1757600:
    # if (not log.last_id[0].isalpha()) or index >1757600:
        input("pause")
    print(index)
    # input("wait")