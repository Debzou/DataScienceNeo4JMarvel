from neo4j import GraphDatabase
# Load the Pandas libraries with alias 'pd' 
import pandas as pd


class Neo4j(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def readCsvCreateObject(self,path):
        cql = ""
        cql2 = ""
        cql3 = ""
        cqltot = ""
        data = pd.read_csv(path)
        #read row by row
        # create
        for i in range(len(data)) :
            # data clean
            name = data.loc[i, "name"].replace('-', '').replace(' ', '').replace('!', '').replace('.','').replace("'",'')
            publisher = str(data.loc[i, "Publisher"]).replace('-', '').replace(' ', '').replace('!', '').replace('.','').replace("'",'')
            # query in order to create hero
            cql = "CREATE (%s:hero { id: %d , name : '%s' , gender : '%s' })"%(name,
            data.loc[i, "id"],name,data.loc[i, "Gender"])
            # query in order to create publisher if not exist
            cql2 = "MERGE (%s:publisher { publisher: '%s'})"%(publisher,publisher)
            # create the realtionship
            cql3 = "CREATE (%s)-[r:RELTYPE]->(%s)"%(name,publisher)
            cqltot = cql + cql2 + cql3
            # send query
            self.sendQuery(cqltot)

        


    def sendQuery(self,query):
        
        # Execute the CQL query
        with self._driver.session() as graphDB_Session:
            # Create nodes
            graphDB_Session.run(query)

    def clear(self):
        query = "MATCH (n) DELETE n"
        # Execute the CQL query
        self.sendQuery(query)


        