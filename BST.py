class Node:
	def __init__(self , data):
		self.data = data
		self.left = None
		self.right = None


class BST:
	def __init__(self):
		self.root = None

	def addNode(self , x):
		node = Node(x)
		if self.root==None:
			self.root = node
			print("root added")
			return self.root

		ptr = self.root

		if node.data < self.root.data:
			while(ptr.left != None ):
				ptr = ptr.left
			if(ptr.left is None and node.data < ptr.data):
				ptr.left = node
				print(ptr.left.data , "added l of l")
			elif(ptr.right is None and node.data > ptr.data):
				ptr.right = node
				print(ptr.right.data , "added r of l")
		else:
			while(ptr.right != None):
				ptr = ptr.right
			if(ptr.right is None and node.data>ptr.data):
				ptr.right = node
				print(ptr.right.data , "added r of r")
			elif(ptr.left is None and node.data<ptr.data):
				ptr.left = node
				print(ptr.left.data , "added l of r")

	def InorderPrint(self , root):                           #left , root , right
		if not root:
			return 
		self.InorderPrint(root.left)
		print root.data
		self.InorderPrint(root.right)

	def pre_order_print(self , root):                 #root , left ,right
	    if not root:
	        return        
	    print root.data
	    self.pre_order_print(root.left)
	    self.pre_order_print(root.right)



# b = BST()
# r = b.addNode(10)
# b.addNode(6)
# b.addNode(15)
# b.addNode(11)
# b.addNode(17)
# b.addNode(3)
# b.addNode(7)
# # b.Print(r)
# b.pre_order_print(r)

