from logger import Logger


log = Logger()

#writing normal entries
log.write(content= "AAA00=654654654")
log.write(content= "BAA00=654654654")
log.write(content= "CAA00=654654654")
log.write(content= "DAA00=654654654")

#updating
log.write(content= "15444", index= False)
log.write(content= "25444", index= False)
log.write(content= "35444", index= False)
log.write(content= "45444", index= False)
log.write(content= "55444", index= False)



#mixing updates and indexes
log.write(content= "65444", index= False)
log.write(content= "EAA00=654654654")
log.write(content= "75444", index= False)
log.write(content= "FAA00=654654654")
log.write(content= "85444", index= False)