class Object:
	index = 0
	data = None
	def __init__(self, type, *args):
		index+=1
		self.type = type
		if type == 'Data':
			self.data = args[0]
		elif type == 'Proc':
			self.clist = args[0]
			self.execute = 0

class Vertex:
	def addObject(self, obj):
		self.objList.append(obj)
	def __init__(self, index, height, excessFlow):
		self.height = height
		self.excessRate = excessFlow
		self.index = index
	def __add__(self, other):
		if not hasattr(self, 'adjList'):
			self.adjList = []
		self.adjList.append(other)
	def __repr__(self):
		print("Vertex %d\t"%self.index)
	def getValue(self):
		return self.index
	def display(self):
		print("Vertex %d with height %d and ExcessRate %d"%(self.index, self.height, self.excessRate))
		if hasattr(self, 'adjList'):
			print([i.index for i in self.adjList])

class Edge:
	def __init__(self, rate, cap, *v):
		self.v0 = v[0]
		self.v1 = v[1]
		self.capacity = cap
		self.rate = rate
	def addRate(self, rate):
		if 0 <= rate:
			self.rate += rate
	def __repr__(self):
		return ("Edge [%d  %d] with capacity %d\t and rate %d\n"%(self.v0, self.v1, self.capacity, self.rate))
	def display(self):
		print("Edge [%d  %d] with capacity %d\n"%(self.v0, self.v1, self.capacity))			

class Process(Object):
	pass
	
		
	 
			
		
		
	

