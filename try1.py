#try1.py
#함수정의
def divide(a,b):
    return a/b

#호출
try:
    result = divide(5,0)
except TypeError:
    print("숫자여야 합니다")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
else:
    print("연산결과 :{0}".format(result))
finally:
    print("무조건 실행")

print("전체코드실행종료")


