#!/usr/bin/env python

import sqlite3

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>ユーザ情報</title>")
print("</head>")

print("<body>")
print("<h1>ユーザ情報</h1>");

# データベースに接続
con = sqlite3.connect('sugiten.db')

# カーソルを取得
cur = con.cursor()

# ユーザ情報を取得
records = cur.execute("SELECT * FROM Users;")

# ユーザ情報を表示
table = "<table border=`1``>"
table += "<tr>"
table += "<th>id</th>"
table += "<th>password</th>"
table += "<th>name</th>"
table += "<th>tel</th>"
table += "<th>mail</th>"
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
