class Node(object):
	def __init__(self , data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.cnt = 0

	def addHead(self , x):
		node = Node(x)
		node.next = self.head
		self.head = node
		self.cnt+=1
		print("added new node")
		

	def addTail(self , x):
		node = Node(x)

		if self.head == None:
			self.head = node

		else:
			cur = self.head
			while(cur != None):
				cur = node.next
			node.next = node
		self.cnt+=1
		print("New node inserted")

	def removeHead():
		if self.head==None:
			return

		else:
			self.head = node.next
			self.cnt-=1

	def removeTail():
		if self.head==None:
			return


	def printForward(self):
		if self.head is None:
			return

		print(self.head.data)

		while(self.head.next!=None):
			self.head = self.head.next
			print(self.head.data)
			

l1 = LinkedList()
l1.addHead(5)
l1.addHead(10)
l1.addHead(15)
l1.addTail(20)
l1.printForward()





		
		
