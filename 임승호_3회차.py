#1번문제
f = open("c:\\3test\\임승호.txt","wt")
f.write("파이썬 데이터\nabcd\n")

f.close()

f = open("c:\\3test\\임승호.txt", "rt")
print(f.read())

print("=" * 10)
f = open("c:\\3test\\임승호.txt", "a+")
f.write("추가 데이터\n")
f.close()

f = open("c:\\3test\\임승호.txt")
print(f.read())
f.close()

#2번문제
import urllib.request
from bs4 import BeautifulSoup
data = urllib.request.urlopen('https://comic.naver.com/webtoon/list.nhn?titleId=711422&weekday=fri')
soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

f = open("c:\\work2\\webtoon.txt","wt",encoding="utf-8")
for item in cartoons:
    title = item.find("a").text
    print(title.strip())
    f.write(title.strip()+"\n")
f.close()

#3번문제
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
import urllib.request
from bs4 import BeautifulSoup


form_class = uic.loadUiType("임승호Form3.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
        soup = BeautifulSoup(data, "html.parser")
        cartoons = soup.find_all("td", class_="title")
        f = open("c:\\work2\\webtoon.txt", "wt", encoding="utf-8")
        for item in cartoons:
            title = item.find("a").text 
            print(title.strip())
            f.write(title.strip() + "\n")
        f.close() 
        self.label.setText("웹툰 크롤링 종료~~")

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_() 

#4번문제
import sqlite3

con = sqlite3.connect("c:\\3test\\임승호.db")
cur = con.cursor()
cur.execute("select * from books;")
for row in cur:
    print(row)

#5번문제
import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table books (Id text, title text);")
cur.execute("insert into books values ('derick', '010-111');")
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into books values (?, ?);", (name, phoneNumber))
datalist = (("tom","010-123"), ("dsp","010-567"))
cur.executemany("insert into books values (?, ?);", datalist)

cur.execute("select * from books;")
for row in cur:
    print(row)

f = open("c:\\3test\\임승호.sql","wt")
for item in con.iterdump():
    print(item)
    f.write(item + "\n")

f.close()

with open("c:\\3test\\임승호.sql") as f:
    SQLScript = f.read()

con = sqlite3.connect("c:\\3test\\임승호.db")
cur = con.cursor()
cur.executescript(SQLScript)
con.close()

