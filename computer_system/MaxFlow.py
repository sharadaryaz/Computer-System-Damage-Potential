from graphUtils import Vertex, Edge, Process, Object
from math import inf
class Graph:
	edges = {}
	processes = []
	vertices = []
	height = {}
	def __init__(self, numVertex):
		"""Initializing vertices with first one being source and last one being the target"""
		self.numVertex = numVertex
		for v in range(numVertex):
			v = Vertex(v, 0, 0)
			self.vertices.append(v)

	def __repr__(self):
		print ("\nVertices: \t")
		for i in range(self.numVertex):
			(self.vertices[i])
		print ("\nEdges: \t")
		self.edges

	def display(self):
		print ("\nVertices: \t")
		for i in range(self.numVertex):
			self.vertices[i].display()
		print ("\nEdges: \t")
		print(self.edges)
		print ("\nProcesses: \t")
		for p in self.processes:
			print(p)

	def addEdge(self, rate, cap, *v):
		if not v[0] in self.edges:
			self.edges[v[0]] = {}
		self.edges[v[0]][v[1]] = Edge(rate, cap, *v)
		self.vertices[v[0]] + self.vertices[v[1]]


	def preFlow(self, s):
		print ("\nInside PreFlow \t")
		self.vertices[s].height= len(self.vertices)
		for v in self.vertices[s].adjList:
			i = v.getValue()
			self.edges[s][i].rate = self.edges[s][i].capacity
			print ("Creating edse with values %d %d %d %d"%(-self.edges[s][i].rate, 0, i, s ))
			self.vertices[i].excessRate = self.edges[s][i].capacity
			self.edges[i][s] = Edge( 0,self.edges[s][i].rate, i, s )
			self.vertices[i] + self.vertices[s]

	'''This fuction finds all the vertices with the excess rate and returns the one with the maximum height'''
	def findExcessFlow(self):
		print ("\nFind Excess Flow\n")
		#maxHeight = -inf
		excessV = None
		for v in self.vertices[1:-1]:
			if 0 < v.excessRate: 
				print ("\nFound Excess Flow with vertex %d\n"%(v.getValue()))
				return v
		return -1;
				

	
	'''This function pushes the minimum of capacity of edge and excess rate of vertex to the adjacent vertex'''
	def Push(self, u):
		print ("Inside Push of vertex %d\n"%u.getValue())
		for v in u.adjList:
			k = u.getValue()
			i = v.getValue()
			if self.edges[k][i].rate == self.edges[k][i].capacity:
				continue
			if v.height < u.height:
				rate = min(self.edges[k][i].capacity - self.edges[k][i].rate, u.excessRate)
				print ("\nMin rate is %d"%rate)
				u.excessRate -= rate
				v.excessRate += rate
				print("\nChanging rate of %d%d from %d to"%(self.edges[k][i].v0, self.edges[k][i].v1, self.edges[k][i].rate ))
				self.edges[k][i].rate += rate
				print(self.edges[k][i].rate)
				self.createRevEdge(rate, i, k)
				self.display()
				return 1
		print ("\nReturned 0 from Push")
		return 0
	
	'''This function creates a reverse edge with updated flow'''
	def createRevEdge(self, rate, i, u):
		print ("\nCreate Rev Edge\n")
		if i!=(len(self.vertices)-1):
			if u in self.edges[i].keys():
				self.edges[i][u].rate -= rate
				return
		self.addEdge(0, rate, i, u)

	'''This function relabels the height of the argument vertex according to its adjacent vertex of minimum height'''
	def Relabel(self, u):
		print ("\nInside Relabel of vertex %d\n"%u.getValue())
		minH = inf
		for v in u.adjList:
			k = u.getValue()
			i = v.getValue()
			if self.edges[k][i].rate == self.edges[k][i].capacity:
				continue 
			if minH > v.height:
				minH = v.height
				u.height = minH+1
				print("Updated height of u with vertex %d height %d + 1"%(v.getValue(), v.height ))
		self.display()

		'''This function returns the maximum rate, i.e. the excess flow of the target node, it keeps running as long as push and relabel methods returns true'''
	def maxRate(self):
		print ("\nInside MaxRate\n")
		self.preFlow(0)
		self.display()
		while self.findExcessFlow() != -1:
			u = self.findExcessFlow()
			if not self.Push(u):
				self.Relabel(u)
		return self.vertices[-1].excessRate

if __name__ == '__main__':
	pass

