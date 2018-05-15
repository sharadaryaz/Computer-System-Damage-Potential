from graphUtils import Vertex, Edges, Objects

class Graph:
	edges = [][]
	vertices = []
	height = {}
	def addEdge(self, cap, *v):
		edges.append(Edge(cap, *v))
	def preFlow(self, s):
		height[vertices[s]]= len(vertices)
	 	for i in range(len(edges))
			edges[i].rate = 0
			height[vertices[i]] = 0
		for v in adj(vertices[s]):
			i = v.getVal()
			edges[s][i].rate = edges[s][i].cap
			edges[i].append(edge(edges[s][i].rate, i, s ))
			vertices[i].excess_rate = edges[s][i].rate
	
	def findExcessFlow(self):
		'''This fuction finds all the vertices with the excess rate and returns the one with the maximum height'''
	 	maxHeight = float('-inf')
		for v in vertices:
			if 0 < v.excess_rate and maxHeight < height[v]:
				excessV = v
				maxHeight = height[v]
		return excessV
	
	def Push(self, u):
		'''This function pushes the minimum of capacity of edge and excess rate of vertex to the adjacent vertex'''
		for v in adj(u):
			if v.height < u.height:
				i = v.getVal()
				rate = min(edge[u][i].cap, u.excess_rate)
				edge[u][i].rate = rate
				v.excess_rate = rate
				createRevEdge(flow, i, u)
	
	def createRevEdge(self, flow, i, u):
		'''This function creates a reverse edge with updated flow'''
		edge[u][i].flow -= flow
		addEdge(flow, i, u)
	
	def Relabel(u):
		'''This function relabels the height of the argument vertex according to its adjacent vertex of minimum height'''
		minH = float(inf)
		for v in adj(u):
			if minH > height[v]:
				min = height[v]
		height[u] = min+1

	def maxRate():
		'''This function returns the maximum rate, i.e. the excess flow of the target node, it keeps running as long as push and relabel methods returns true'''
		while u = findExcessFlow():
			if not Push(u):
				Relabel(u)
			return vertices[-1]

	if main 
		









 
