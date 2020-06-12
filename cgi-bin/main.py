#!/usr/bin/env python

import sqlite3
import cgi
import encode

# フォームの取得
form = cgi.FieldStorage()

form_id = form["id"].value
form_pw = form["password"].value

# データベースに接続
con = sqlite3.connect('sugiten.db')

# カーソルを取得
cur = con.cursor()

# ユーザ情報の検索・表示
def showUserInfo(id):
    sql = "SELECT name,tel,mail FROM Users WHERE id='" + id + "';"
    records = cur.execute(sql)
    record = records.fetchone()
    name = record[0]
    tel = record[1]
    mail = record[2]

    print("<p>氏名: " + name + "</p>")
    print("<p>電話番号: " + tel + "</p>")
    print("<p>メールアドレス: " + mail + "</p>")

# ユーザの購買履歴の検索・表示
def showUserHistory(id):
    sql = "SELECT time,name,price FROM Histories INNER JOIN Items ON Histories.item_id=Items.id WHERE user_id='" + id + "'";
    records = cur.execute(sql)

    print("<h2>購買履歴</h2>")

    table = "<table border=`1``>"
    table += "<tr>"
    table += "<th>time</th>"
    table += "<th>name</th>"
    table += "<th>price</th>"
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

# 商品情報の表示
def showItems(user_id):
    sql = "SELECT * from Items;"
    records = cur.execute(sql)

    print("<h2>商品一覧</h2>")

    table = "<table border=`1``>"
    table += "<tr>"
    table += "<th>name</th>"
    table += "<th>price</th>"
    table += "<th>stock</th>"
    table += "<th>buy</th>"
    table += "</tr>"

    for record in records:
        table += "<tr>"

        item_id = record[0]
        name = record[1]
        price = record[2]
        stock = record[3]

        table += "<td>"
        table += str(name)
        table += "</td>"

        table += "<td>"
        table += str(price)
        table += "</td>"

        table += "<td>"
        table += str(stock)
        table += "</td>"

        form = "<form method='post' target='_blank' action='buy.py'>"
        form += "<input type='hidden' name='user' value='" + user_id + "'>"
        form += "<input type='hidden' name='item' value='" + item_id + "'>"
        form += "<input type='submit' value='購入'></form>"

        table += "<td>"
        table += form
        table += "</td>"

        table += "</tr>"
    table += "</table>"
    print(table)

# Idに一致するpasswordを取得
sql = "SELECT password FROM Users WHERE id='" + form_id + "';"
records = cur.execute(sql)
pw = records.fetchone()

print ("Content-type:text/html\n\n")

print("<!DOCTYPE html>")
print("<html>")

print("<head>")
print("<meta charset='utf-8'>")
print("<title>メイン</title>")
print("</head>")

print("<body>")
print("<h1>メイン</h1>");

if pw == None:
    print("<p>IDが存在しません</p>")
    print("<p><a href='../login.html'>戻る</a></p>")
else:
    if form_pw == pw[0]:
        print("<p>ログインに成功しました</p>")

        # ユーザ情報の検索・表示
        showUserInfo(form_id)

        # ユーザの購買履歴の検索・表示
        showUserHistory(form_id)

        # 商品情報の表示
        showItems(form_id)

    else:
        print("<p>パスワードが一致しません</p>")
        print("<p><a href='../login.html'>戻る</a></p>")

# データベースを切断
con.close()

print("</body>")

print("</html>")
