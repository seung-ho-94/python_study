colors = ["red", "blue", "green"]
colors.append("white")
print(colors)
print(len(colors))
print(type(colors))
colors.insert(1,"yellow")
print(colors)
colors.remove("blue")
print(colors)

#딕셔너리 
food = {"햄":5, "김밥":10, "치킨":3}
print(food)
#검색
print(food["햄"])
#입력
food["햄버거"] = 30
#수정
food["햄"] = 6
#삭제
del food["김밥"]
print(food)
