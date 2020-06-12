#!/usr/bin/env python

from SPARQLWrapper import SPARQLWrapper, JSON
import encode

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>統計LOD</title>")
print("</head>")

print("<body>")
print("<h1>統計LOD</h1>");
print("</body>")

url = "http://data.e-stat.go.jp/lod/sparql/alldata/query"
sparql = SPARQLWrapper(url)
sparql.setReturnFormat(JSON)

prefix = """
PREFIX qb: <http://purl.org/linked-data/cube#>
PREFIX g00200521-dimension-2010: <http://data.e-stat.go.jp/lod/ontology/g00200521/dimension/2010/>
PREFIX g00200521-code-2010: <http://data.e-stat.go.jp/lod/ontology/g00200521/code/2010/>
PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX estat-measure: <http://data.e-stat.go.jp/lod/ontology/measure/>
PREFIX cd-dimension: <http://data.e-stat.go.jp/lod/ontology/crossDomain/dimension/>
PREFIX cd-code: <http://data.e-stat.go.jp/lod/ontology/crossDomain/code/>
"""

query = """
SELECT ?url ?label ?population ?year WHERE{
  ?url qb:dataSet <http://data.e-stat.go.jp/lod/dataset/g00200521/d0003041389>;
       g00200521-dimension-2010:area g00200521-code-2010:area-all;
       sdmx-dimension:refArea [
         rdfs:label ?label
       ];
       estat-measure:population ?population;
       cd-dimension:timePeriod ?year;
       cd-dimension:sex cd-code:sex-all;
       cd-dimension:nationality cd-code:nationality-japan;
       cd-dimension:age cd-code:age-all.
       FILTER(
          CONTAINS(str(?label), "愛知県") ||
          CONTAINS(str(?label), "岐阜県") ||
          CONTAINS(str(?label), "三重県")
       )
}
"""

sparql.setQuery(prefix + query)
results = sparql.query().convert()

table = "<table border=`1``>"
table += "<tr>"
table += "<th>label</th>"
table += "<th>population</th>"
table += "<th>year</th>"
table += "</tr>"

for result in results["results"]["bindings"]:

    url = result['url']['value']
    label = result['label']['value']
    population = result['population']['value']
    year = result['year']['value']

    table += "<tr>"
    table += f"<td><a href={url}>{label}</a></td>"
    table += f"<td>{population}</td>"
    table += f"<td>{year}</td>"
    table += "</tr>"

print(table)

print("</html>")

