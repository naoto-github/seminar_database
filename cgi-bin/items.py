#!/usr/bin/env python

import sqlite3
import encode

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>商品情報</title>")
print("</head>")

print("<body>")
print("<h1>商品情報</h1>");

# データベースに接続
con = sqlite3.connect('sugiten.db')

# カーソルを取得
cur = con.cursor()

# 商品情報を取得
records = cur.execute("SELECT * FROM Items;")

# 商品情報を表示
table = "<table border=`1``>"
table += "<tr>"
table += "<th>id</th>"
table += "<th>name</th>"
table += "<th>price</th>"
table += "<th>stock</th>"
table += "</tr>"

for record in records:
    table += "<tr>"
    for column in record:
        table += "<td>"
        table += str(column)
        table += "</td>"
    table += "</tr>"
table += "</table>"
print(table)

# データベースを切断
con.close()

print("</body>")

print("</html>")
