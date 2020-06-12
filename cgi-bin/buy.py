#!/usr/bin/env python

import sqlite3
import cgi
import datetime
import encode

# フォームの取得
form = cgi.FieldStorage()

form_user = form["user"].value
form_item = form["item"].value

# データベースに接続
con = sqlite3.connect('sugiten.db')

# カーソルを取得
cur = con.cursor()

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>購入確認</title>")
print("</head>")

print("<body>")
print("<h1>購入確認</h1>");

# 在庫数の取得
sql = "SELECT stock FROM Items where id='" + form_item + "';"
records = cur.execute(sql)
record = records.fetchone()
stock = int(record[0])

# 在庫があるとき
if stock >= 1:

    print("<p>購入に成功しました</p>")

    # 在庫数を減らす
    sql = "UPDATE Items SET Stock=" + str(stock-1) + " where id='" + form_item + "';"
    cur.execute(sql)

    # 購買履歴を記録
    dt = datetime.datetime.now()
    time = dt.strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO Histories(time, user_id, item_id) VALUES('" + time + "', '" + form_user + "', '" + form_item  + "');"
    cur.execute(sql)

else:
    print("<p>購入に失敗しました</p>")

print("<p><a href='#' onclick='window.close()'>閉じる</a></p>")

# データベースの更新の確定
con.commit()

# データベースを切断
con.close()

print("</body>")

print("</html>")
