#!/usr/bin/env python

import sqlite3
import encode

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>購買履歴</title>")
print("</head>")

print("<body>")
print("<h1>購買履歴</h1>");

# データベースに接続
con = sqlite3.connect('sugiten.db')

# カーソルを取得
cur = con.cursor()

# 購買履歴を取得
records = cur.execute("SELECT * FROM Histories;")

# 購買履歴を表示
table = "<table border=`1``>"
table += "<tr>"
table += "<th>id</th>"
table += "<th>time</th>"
table += "<th>user_id</th>"
table += "<th>item_id</th>"
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
