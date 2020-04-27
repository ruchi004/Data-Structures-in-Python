class stack:
	def __init__(self):
		self.lst = []
		self.idx = 0

	def push(self , x):
		self.lst.append(x)
		print("Element added")

	def pop(self):
		del self.lst[len(self.lst) - 1]
		print("Element removed")

	def Print(self):
		for i in self.lst[: :-1]:
			print(i)

	def getIndex(self , x):
		for i in self.lst:
			if i==x:
				return self.lst.index(x)

	def update(self , x , New):
		for i in self.lst:
			if i==x:
				self.idx = self.getIndex(x)
				self.lst[self.idx] = New
				print("value updated")
			else:
				continue
			break

	def peek(self):
		print(self.lst[-1])
		


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
# s.Print()
# s.update(4 , 9)
# s.Print()
s.peek()
