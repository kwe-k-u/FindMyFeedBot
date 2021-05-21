from logger import Logger

if __name__ == "__main__":
    log = Logger()

    #updating last indexes
    log.writeIndex("654654651")
    log.writeIndex( "654654652")
    log.writeIndex( "654654653")
    log.writeIndex("654654654")

    #updating tweet ids
    log.writeLastId("15445")
    log.writeLastId("25446")
    log.writeLastId("35447")
    log.writeLastId("45448")
    log.writeLastId("55449")

    #

    #mixing updates and indexes
    log.writeLastId("65410")
    log.writeIndex("65465465411")
    log.writeLastId("7544412")
    log.writeIndex("65465465413")
    log.writeLastId("8544414")

