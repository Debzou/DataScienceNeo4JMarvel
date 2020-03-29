import useful as us

# constant
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "test"
PATH_CSV = "heroes_information.csv"

# main define
def main():
    # connect to the data base
    neo4j = us.Neo4j(URI,USER,PASSWORD)
    # clear data base
    neo4j.clear()
    # read CSV file
    neo4j.readCsvCreateObject(PATH_CSV)
    # close data base
    neo4j.close()

# thow main    
if __name__ == "__main__":
    main()