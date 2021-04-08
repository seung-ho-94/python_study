#연산자 오버라이드 
class NumBox:
	def __init__(self, num):
		self.Num = num
	# def __add__(self, num):
	# 	self.Num += num
	# def __sub__(self, num):
	# 	self.Num -= num
	def add(self, num):
		self.Num += num
	def remove(self, num):
		self.Num -= num


#인스턴스 생성
n = NumBox(40)
# n + 100 
n.add(100)
print(n.Num)
# n - 110 
n.remove(50)
print(n.Num)

#어우 이거 못쓰겠는데
