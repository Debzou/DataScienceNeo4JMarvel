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
        data = pd.read_csv(path)
        #read row by row
        
        # create Male and female
        cql = "CREATE (Male:gender { gender : 'Male'})"
        
        self.sendQuery(cql)
        cql=""
        for i in range(len(data)) :
            # data clean
            name = data.loc[i, "name"].replace('-', '').replace(' ', '').replace('!', '').replace('.','').replace("'",'')
            publisher = str(data.loc[i, "Publisher"]).replace('-', '').replace(' ', '').replace('!', '').replace('.','').replace("'",'')
            # query in order to create hero
            cql = "CREATE (%s:hero { id: %d , name : '%s' , gender : '%s' })"%(name,
            data.loc[i, "id"],name,data.loc[i, "Gender"])
            # query in order to create publisher if not exist
            cql += "MERGE (%s:publisher { publisher: '%s'})"%(publisher,publisher)
            # create a realtionship hero and publisher
            cql += "CREATE (%s)-[r:APPEARED]->(%s)"%(name,publisher)    
            
            # create a relationship between hero and gender
            if (data.loc[i, "Gender"]=="Male" or data.loc[i, "Gender"] =="Female"):
                # query create sexe (male female and why not other)
                cql += "MERGE (%s:gender { gender : '%s'})"%(data.loc[i, "Gender"],data.loc[i, "Gender"])
                cql += "CREATE (%s)-[p:BE]->(%s)"%(name,data.loc[i, "Gender"])  
            else:   
                cql += "MERGE (other:gender { gender : 'other'})"
                cql += "CREATE (%s)-[p:BE]->(other)"%(name)  
            # send query
            self.sendQuery(cql)
            cql=""

        


    def sendQuery(self,query):
        
        # Execute the CQL query
        with self._driver.session() as graphDB_Session:
            # Create nodes
            graphDB_Session.run(query)

    def clear(self):
        query = "MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r"
        # Execute the CQL query
        self.sendQuery(query)


        