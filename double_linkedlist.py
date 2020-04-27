class Node:
	def __init__(self , data):
		self.data = data
		self.next = None
		self.prev = None

class Dll:
	def __init__(self):
		self.head = None
		self.cnt = 0

	def addHead(self , x):
		node = Node(x)
		if self.head == None:
			self.head = node
		
		else:
			node.next = self.head
			self.head = node
			node.next.prev = node
		print("Added head")
		self.cnt+=1

	def addTail(self , x):
		node = Node(x)
		if self.head == None:
			self.head = node

		else:
			cur = self.head
			while(cur.next != None):
				cur = cur.next
			cur.next = node
			node.prev = cur
		print("added tail")
		self.cnt+=1

	def removehead(self):
		if self.head == None:
			return "nothing to delete"

		else:
			cur = self.head
			self.head = cur.next
			cur.next.prev = None
		print("Removed head")
		self.cnt-=1

	def printForward(self):
		if self.head == None:
			print("Nothing to print")

		else:
			cur = self.head
			while(cur.next != None):
				print(cur.data)
				cur = cur.next
			print(cur.data)

	def printReverse(self):
		if self.head == None:
			print("Nothing to print")

		else:
			cur = self.head
			while(cur.next != None):
				cur = cur.next
			print(cur.data)
			while(cur.prev != None):
				print(cur.prev.data)
				cur = cur.prev

	def countNodes(self):
		print("No of nodes are : " , self.cnt)



l1 = Dll()
l1.addHead(1)
l1.addHead(2)
l1.addHead(3)
l1.addTail(4)
# l1.removehead()
# l1.printForward()
# l1.printReverse()
# l1.countNodes()




