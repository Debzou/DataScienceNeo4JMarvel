# DataScienceNeo4JMarvel

## Installion

```bash
pip install neo4j
pip3 install pandas
```

## Connect to the data base
change constant in the main.py

```python
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "test"
PATH_CSV = "heroes_information.csv"
```

## Go to http://localhost:7474/browser/
do this query in order to view which hero heros appear in publisher

```cypher
MATCH p=()-[r:RELTYPE]->() RETURN p
```

![](screen.png)
