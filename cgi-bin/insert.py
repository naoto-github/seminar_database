#!/usr/bin/env python

import sqlite3
import cgi
import encode

# フォームの取得
form = cgi.FieldStorage()

form_id = form["id"].value
form_name = form["name"].value
form_price = form["price"].value
form_stock = form["stock"].value

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

# レコードの有無の確認
sql = "SELECT * FROM Items WHERE id='" + form_id + "';"
records = cur.execute(sql)
record = records.fetchone()

# レコードの追加
sql = "INSERT OR REPLACE INTO Items VALUES('" + form_id + "', '" + form_name + "', " + form_price + ", " + form_stock + ");"
cur.execute(sql)

if record == None:
    print("<p>追加に成功しました</p>")
else:
    print("<p>更新に成功しました</p>")


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

print("<p><a href='#' onclick='window.close()'>閉じる</a></p>")

# データベースの更新の確定
con.commit()

# データベースを切断
con.close()

print("</body>")

print("</html>")
