#!/usr/bin/env python

from SPARQLWrapper import SPARQLWrapper, JSON

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>ジャパンサーチ SPARQL</title>")
print("</head>")

print("<body>")
print("<h1>ジャパンサーチ SPARQL</h1>");

url = "https://jpsearch.go.jp/rdf/sparql"
sparql = SPARQLWrapper(url)
sparql.setReturnFormat(JSON)

prefix = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <http://schema.org/>
PREFIX place: <https://jpsearch.go.jp/entity/place/>
PREFIX type: <https://jpsearch.go.jp/term/type/>
"""

query = """
SELECT ?url ?label ?thumbnail WHERE{
  ?url rdf:type type:絵画;
       rdfs:label ?label;
       schema:image ?thumbnail.
}
LIMIT 5
"""

sparql.setQuery(prefix + query)
results = sparql.query().convert()

table = "<table border=`1``>"
table += "<tr>"
table += "<th>label</th>"
table += "<th>thumbnail</th>"
table += "</tr>"

for result in results["results"]["bindings"]:

    url = result['url']['value']
    label = result['label']['value']
    thumbnail = result['thumbnail']['value']
    
    table += "<tr>"
    table += f"<td><a href='{url}'>{label}</a></td>"
    table += f"<td><img src='{thumbnail}'></td>"
    table += "</tr>"

print(table)

print("</body>")

print("</html>")
