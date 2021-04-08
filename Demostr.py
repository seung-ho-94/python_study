strA = "python is powerpul"
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))
print("문자열 길이 : ", len(strA))

print("숫자와 알파벳 구분")
print("MBC2580".isalnum())
print("MBC2580".isalnum())
print("2580".isdecimal())

print("====끝부분 체크====")
print("demo.ppt".endswith("ppt"))
u = " spam and ham "
print(u)
result = u.strip("<> ")
print(result)
#문자열을 치환
result2 = result.replace("spam", "spam and egg")
print(result2)
# 다시 하나의 문자열로 합치기
result3 = " ".join(result2)
print(result3)