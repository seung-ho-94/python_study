#SQLite를 사용하는 데모 (로컬데이터베이스)
import sqlite3

#처음에는 데이터베이스파일(또는 메모리)를 생성
con = sqlite3.connect("c:\\work2\\sample.db")
#SQL구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()
#저장소(테이블)을 만들기
cur.execute("create table PhoneBook (Name text, PhoneNume text);")
#1건 입력
cur.execute("insert into Phonebook values ('derick', '010-111');")

#입력 파라미터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#다중의 레코드(행, row)를 입력받는 경우
datalist = (("tom", "010-123"), ("dsp", "010-567"))
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#검색
cur.execute("select * from PhoneBook")

for row in cur:
    print(row)

#커밋(작업을 정상적으로 완료 log -> db에도 기록)
#데이터를 변경(입력, 수정, 삭제)
con.commit()