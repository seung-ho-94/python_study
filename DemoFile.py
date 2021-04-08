#Demofile
#파일객체를 리턴받기
f = open("c:\\work\\demo.txt","wt")
#newline을 직접 코딩
f.write("한글을 출력\n")
f.write("abcd\n1234\n")
f.close()

#파일을 읽기
f = open("c:\\work\\demo.txt", "rt")
#read()는 전체 라인을 읽어서 str로 리턴
print(f.read())
#위치를 변경
print(f.tell())
f.seek(0)
print(f.readline())
print(f.readline())
#위치를 알려준다.
print(f.tell())
#리셋(처음으로 돌아가~)
f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())
#전체를 리스트로 받기
f.seek(0)
lst = f.readlines()
for item in lst:
    print(item, end="") #줄바꿈 안할거임

f.close
print(f.closed)

#기존 파일에 첨부르 하는 경우
print("=" * 10)
f = open("c:\\work\\demo.txt", "a+")
f.write("새로운 내용 추가\n")
f.write("write로 파일에 내용을 입력한다.\n파일 입출력 부분도 자바보다 간편하다\n")
f.close()

f = open("c:\\work\\demo.txt")
print(f.read())
f.close()