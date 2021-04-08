# -*- 생성자와 소멸자 그리고 참조 카운트 관리  -*-
class MyClass:
    #생성자
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    #소멸자
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
#del d

print("전체 코드 실행 종료")




