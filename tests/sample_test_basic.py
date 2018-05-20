import sys
sys.path.insert(0, '/Users/sharadsharad/Documents/Research Topics/Python_Implementation/computer_system')
from MaxFlow import Graph
from graphUtils import Vertex, Edge, Process, Object
G = Graph(4)
G.vertices[0] + G.vertices[1]
G.vertices[1] + G.vertices[2]
G.vertices[2] + G.vertices[3]
G.vertices[0].addObject(Object('Proc', G.vertices[0], 'Data0', [(1, 'E')]))
G.vertices[1].addObject(Object('Proc', G.vertices[1], 'Data1', [(2, 'E')]))
G.vertices[2].addObject(Object('Proc', G.vertices[2], 'Data2', [(3, 'E')]))
G.vertices[3].addObject(Object('Proc', G.vertices[3], 'Data2', []))
print("The first object  is %d"%G.vertices[0].objList[0].index)
G.processes.append(Process(G.vertices[0].objList[0]))
G.processes[0].createProcess(G, G.vertices[1].objList[0], 0, 3)
G.processes[1].createProcess(G, G.vertices[2].objList[0], 0, 1)
G.processes[2].createProcess(G, G.vertices[3].objList[0], 0, 2)
G.display()
print("\nMaximum Rate = %d"%G.maxRate())