# 정적메서드.py
class MyCalc(object):
    #데코레이터(어노테이션)
    @staticmethod
    def my_add(x,y):
        return x+y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

