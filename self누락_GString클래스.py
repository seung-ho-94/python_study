#전역변수(이름충돌)
str = "Not Class Member"
class GString:
    #초기화를 담당(생성자 메서드)
    def __init__(self):
        #인스턴스 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str) #해결~~

g = GString()
g.set("First Message")
g.print()
