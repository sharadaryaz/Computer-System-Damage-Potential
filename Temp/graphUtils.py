class Object:
	index = 0
	data = None
	def __init__(self, type, *args):
		self.index = Object.index
		Object.index += 1
		self.type = type
		if type == 'Data':
			self.loc = args[0]
			self.data = args[1]
		elif type == 'Proc':
			self.loc = args[0]
			self.data = args[1]
			self.clist = args[2]
			self.execute = 0
		print("\nObject with index {0}, location {1} and clist {2}".format(self.index, self.loc.index, self.clist))
	def __repr__(self):
		return ("\nObject with index {0}, location {1} and clist {2}".format(self.index, self.loc.index, self.clist))

class Vertex:
	def __init__(self, index, height, excessFlow):
		self.height = height
		self.excessRate = excessFlow
		self.index = index
		self.objList = []
	def __add__(self, other):
		if not hasattr(self, 'adjList'):
			self.adjList = []
		self.adjList.append(other)
	def __repr__(self):
		print("Vertex %d\t"%self.index)
	def addObject(self, obj):
		self.objList.append(obj)
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
	def setPid(self, pid):
		self.curProcess = pid
	def __repr__(self):
		return ("Edge [%d  %d] with capacity %d\t and rate %d\n"%(self.v0, self.v1, self.capacity, self.rate))
	def display(self):
		print("Edge [%d  %d] with capacity %d\n"%(self.v0, self.v1, self.capacity))			

class Process():
	pid = 0
	def __init__(self, obj):
		self.pid = Process.pid
		Process.pid += 1 
		self.clist = obj.clist
		self.loc = obj.loc
		self.plist = []
	def __repr__(self):
		return ("\nProcess {0} , loc - {1} , plist - {2}, clist - {3}".format(self.pid, self.loc.index, self.plist, self.clist))
	def getLocation(self):
		return self.loc
	def createProcess(self, gPtr, obj, rate, cap):
			if not obj.loc in self.loc.adjList:
				return -1
			if obj.type == 'Proc' and (obj.index, 'E') in self.clist:
				self.p = Process(obj)
				gPtr.processes.append(self.p)
				self.plist.append(self.p.pid)
				if self.loc != obj.loc:
					print("Inside createProcess: Adding Edge %d %d with %d %d"%(self.loc.index, obj.loc.index, rate, cap))
					gPtr.addEdge(rate, cap, self.loc.index, obj.loc.index)
				


