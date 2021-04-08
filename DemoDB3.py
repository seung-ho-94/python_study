# DemoDB2.py 
#SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

#처음에는 데이터베이스파일에 저장
con = sqlite3.connect(":memory:")
#SQL구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()
#저장소(테이블)을 만들기: 테이블 스키마(뼈대)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#입력 파라메터 처리(python format {0},{1})
#텍스트박스(GUI, Web Page)에서 입력을 받아서 처리 
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#다중의 레코드(행, row)를 입력받는 경우: 2차원 행열데이터 
datalist = (("tom","010-123"), ("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)

#백업받기(덤프)
#파일로 저장
f = open("c:\\work2\\dump.sql","wt")
for item in con.iterdump():
    print(item)
    f.write(item + "\n")

f.close()

#복구하기
with open("c:\\work2\\dump.sql") as f:
    SQLScript = f.read()

#구문 실행하기 위해
con = sqlite3.connect("c:\\work2\\Demo.db")
cur = con.cursor()
cur.executescript(SQLScript)
con.close()

#다중라인으로된 sQL배치파일
