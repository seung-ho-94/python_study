# 화면단(DemoForm3.ui)  + 로직단(DemoForm3.py)
import sys 
#Qt패키지 로딩: 패키지명.모듈명
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버에 요청
import urllib.request
#크롤링에 필요
from bs4 import BeautifulSoup


#미리 만든 화면을 로딩(두번째 화면)
form_class = uic.loadUiType("DemoForm3.ui")[0]

#다이알로그를 상속받아서 폼클래스를 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #시그널(이벤트)을 처리하는 슬롯메서드 
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

#직접 이 모듈을 실행했는지 진입점(Entry Point)체크
if __name__ == "__main__":
    #실행 프로세스를 실행(python.exe)
    app = QApplication(sys.argv)
    #위에 있는 클래스의 인스턴스를 생성 
    demoWindow = DemoForm()
    #창을 보여달라~~
    demoWindow.show()
    #지속적으로 실행(이벤트 루프)
    app.exec_() 