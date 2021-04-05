#From 패키지명 import 모듈명
from bs4 import BeautifulSoup

#페이지 로딩(HTML문서를 읽어와~ 유니코드)
page = open("c:\\work3\\test01.html", "rt",encoding="utf-8").read()

#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
#<p>를 모두 검색해! 리스트 형식으로 리턴
# print(soup.find_all("p"))
#첫번째 <p>를 검색
print(soup.find("p"))