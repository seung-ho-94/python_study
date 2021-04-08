# 메모리구조.py
#클래스에만 메서드 저장
class SuperClass:
    def __init__(self):
        self.x = 10 
    def printX(self):
        print(self.x)

class SubClass(SuperClass):
    #상속받아서 재정의하는 경우 반드시 부모 클래스 생성자 호출
    def __init__(self):
        #대무분은 부모 생성자 호출
        SuperClass.__init__(self)
        self.y = 20
    def printY(self):
        print(self.y)
#인스턴스에는 데이터만 저장
s = SubClass()
s.a = 30 
# print("SuperClass:", SuperClass.__dict__)
# print("SubClass:", SubClass.__dict__)
# print("s:", s.__dict__)
s.printX()
s.printY()