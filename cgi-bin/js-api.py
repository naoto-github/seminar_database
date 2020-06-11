#!/usr/bin/env python

import requests
import json

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>ジャパンサーチ 簡易Web API</title>")
print("</head>")

print("<body>")
print("<h1>ジャパンサーチ 簡易Web API</h1>");

keyword = "織田信長"
size = 5
url = f"https://jpsearch.go.jp/api/item/search/jps-cross?keyword={keyword}&size={size}"

r = requests.get(url)

data = json.loads(r.text)

table = "<table border=`1``>"
table += "<tr>"
table += "<th>id</th>"
table += "<th>title</th>"
table += "<th>thumbnail</th>"
table += "</tr>"

for record in data["list"]:
    id = record["id"]
    title = record["common"]["title"]
    link = record["common"]["linkUrl"]
    thumbnail = record["common"]["thumbnailUrl"]

    table += "<tr>"
    table += f"<td>{id}</td>"
    table += f"<td><a href='{link}'>{title}</a></td>"
    table += f"<td><img src='{thumbnail}'></td>"
    table += "</tr>"

print(table)

print("</body>")

print("</html>")
