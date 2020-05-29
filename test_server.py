from SPARQLWrapper import SPARQLWrapper, JSON

query = '''
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://iiitd.ac.in/sweb/2016102/schema#>
PREFIX data: <http://iiitd.ac.in/sweb/2016102/data#>

SELECT ?title ?co_director
WHERE
{
        OPTIONAL {
    ?listing rdf:type schema:Movie .
        ?listing rdf:type schema:TV_Show .
        } .
    ?listing schema:hasTitle ?title .
        ?listing schema:hasDirector ?director .
        FILTER regex(str(?director), "_Shetty$", "i" ).
        OPTIONAL {
    ?listing schema:hasDirector ?co_director .
        FILTER ( ?director != ?co_director )
        } .
}
'''
sparql = SPARQLWrapper("http://192.168.2.217:5001/sparql")
sparql.setQuery(query)
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

print (results)