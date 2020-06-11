#!/usr/bin/env python

from SPARQLWrapper import SPARQLWrapper, JSON

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>DBPedia</title>")
print("</head>")

print("<body>")
print("<h1>DBPedia</h1>");

url = "http://ja.dbpedia.org/sparql"
sparql = SPARQLWrapper(url)
sparql.setReturnFormat(JSON)

prefix = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpedia-owl:  <http://dbpedia.org/ontology/>
PREFIX dbpedia-ja: <http://ja.dbpedia.org/resource/>
PREFIX category-ja: <http://ja.dbpedia.org/resource/Category:>
"""

query = """
SELECT ?url ?name ?abstract ?origin WHERE{
  ?url dbpedia-owl:genre dbpedia-ja:J-POP;
       foaf:name ?name;
       dbpedia-owl:abstract ?abstract;
       prop-ja:origin ?origin.
       FILTER(CONTAINS(str(?origin), "愛知県"))
}
"""

sparql.setQuery(prefix + query)
results = sparql.query().convert()

table = "<table border=`1``>"
table += "<tr>"
table += "<th>name</th>"
table += "<th>abstract</th>"
table += "</tr>"

for result in results["results"]["bindings"]:

    url = result['url']['value']
    name = result['name']['value']
    abstract = result['abstract']['value']
    origin = result['origin']['value']    
    
    table += "<tr>"
    table += f"<td><a href={url}>{name}</a></td>"
    table += f"<td>{abstract}</td>"
    # table += f"<td>{origin}</td>"            
    table += "</tr>"

print(table)

print("</body>")

print("</html>")
