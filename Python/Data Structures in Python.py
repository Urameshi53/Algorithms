# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:59:15 2021

@author: User
""

import sys

'''Recursion'''
'''Binary strings with n bits'''
def begin(x,l):
    return [str(x)+str(i) for i in l]

# print(begin(5,[1,2,3]))

def bitString(n):
    if n == 0:
        return []
    elif n == 1:
        return ['0','1']
    else:
        return (begin(0,bitString(n-1))+begin(1,bitString(n-1)))
    
# print(bitString(7))

'''All the strings of length n from 0....k - 1'''
def r(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result

def strings(n,k):
    if n == 0:
        return []
    if n == 1:
        return r(k)
    return [d+bit for d in strings(1,k) for bit in strings(n-1,k)]

# print(strings(4,3))


'''Graphs'''
'''Adjacency Matrix''
class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False
    
    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)
        
    def getConnections(self,G):
        return G.adjMatrix[self.id]
    
    def getVertexID(self):
        return self.id
    
    def setVertexID(self, id):
        self.id = id
        
    def setVisited(self):
        self.visited = True
    
    def __str__(self):
        return str(self.id)
        
class Graph:
    def __init__(self, numVertices, cost=0):
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)
        
        def setVertex(self, vtx, id):
            if 0<=vtx < self.numVertices:
                self.vertices[vtx].setVertexID(id)
        
        def getVertex(self, n):
            for vertxin in range(0, self.numVertices):
                if n == self.vertices[vertxin].getVertexID():
                    return vertxin
            else:
                return -1
            
        def addEdge(self, frm, to, cost=0):
            if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
                self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
                self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost
            
        def getVertices(self):
            vertices = []
            for vertxin in range(0, self.numVertices):
                vertices.append(self.vertices[vertxin].getVertexID())
            return vertices
        
        def printMatrix(self):
            for u in range(0, self.numVertices):
                row = []
                for v in range(0, self.numVertices):
                    row.append(self.adjMatrix[u][v])
                print(row)
        
        def getEdges(self):
            edges = []
            for v in range(0, self.numVertices):
                for u in range(0, self.numVertices):
                    if self.adjMatrix[u][v] != -1:
                        vid = self.vertices[v].getVertexID()
                        wid = self.vertices[u].getVertexID()
                        edges.append((vid, wid, self.adjMatrix[u][v]))
            return edges
        
if __name__ == '__main__':
    G = Graph(5)
    G.setVertex(0,'a')
    G.setVertex(1,'b')
    G.setVertex(2,'c')
    G.setVertex(3,'d')
    G.setVertex(4,'e')
    print('Graph data:')
    G.addEdge('a','e',10)
    G.addEdge('a','c',20)
    G.addEdge('c','b',30)
    G.addEdge('b','e',40)
    G.addEdge('e','d',50)
    G.addEdge('f','e',60)
    print(G.printMatrix())
    print(G.getEdges())
'''


# '''
# Adjacency List
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = 10000000000
        self.visited = False
        self.previous = None
        self.inDegree = 0
        self.outDegree = 0
        
    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
        
    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertexID(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    
    def setDistance(self, dist):
        self.distance = dist
        
    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev
        
    def setVisited(self):
        self.visited = True
        
    def __str__(self):
        return str(self.id)+' adjacent: '+str([x.id for x in self.adjacent])

        
        
class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0
        
    def __iter__(self):
        return iter(self.vertDictionary.values())
    
    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None
        
    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)
        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)
        
    def getVertices(self):
        return self.vertDictionary.keys()
    
    def setPrevious(self, current):
        self.previous = current
        
    def getPrevious(self, current):
        return self.previous
    
    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a','b',4)
    G.addEdge('a','c',1)
    G.addEdge('c','b',2)
    G.addEdge('b','e',4)
    G.addEdge('c','d',4)
    G.addEdge('d','e',4)
    # print('Graph Data')
    # print(G.getEdges())
# '''

def dfs(G, currentVert, visited):
    visited[currentVert] = True
    print('Traversal: ' + str(currentVert.getVertexID()))
    for nbr in currentVert.getConnections():
        if nbr not in visited:
            dfs(G, nbr, visited)
            
def DFSTraversal(G):
    visited = {}
    for currentVert in G:
        if currentVert not in visited:
            dfs(G, currentVert, visited)

# print(DFSTraversal(G))

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
        
    def enQueue(self, item):
        self.items.append(item)
        self.size += 1
    
    def deQueue(self):
        self.items.pop(0)
        self.size -= 1
        
Q = Queue()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(10)
# print(Q.size)
        
        

def BFSTraversal(G,s):
    start = G.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(start)
    while (vertQueue.size > 0):
        currentVert = vertQueue.deQueue
        print(currentVert.getVertexID())
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)
            currentVert.setColor('black')
            
def BFS(G):
    for v in G:
        if (v.getColor() == 'white'):
            BFSTraversal(G,v.getVertexID())
        

def topologicalSort(G):
    topologicalList = []
    topologicalQueue = []
    remainingDegree = {}
    
    nodes = G.getVertices()
    for v in G:
        indegree = v.getInDegree()
        if indegree == 0:
            topologicalQueue.append(v)
        else:
            remainingDegree[v] = indegree
    while len(topologicalQueue):
        node = topologicalQueue.pop(0)
        topologicalList.append(node)
        
        for son in node.getConnections():
            son.setInDegree(son.getInDegree()-1)
            if son.getInDegree() == 0:
                topologicalQueue.append(son)
                
    if len(topologicalList)!=len(nodes):
        raise #GraphTopologicalException(topologicalList)
    while len(topologicalList):
        node = topologicalList.pop(0)
        print(node.getVertexID())

# L = Graph()
# print(topologicalSort(L))


'''
Hashing
'''
def FirstRepeatedChar(s):
    size = len(s)
    count = [0]*(256)
    for i in range(size):
        if(count[ord(s[i])]==1):
            print(s[i])
            break
        else:
            count[ord(s[i])] += 1
    if(i==size):
        print('No repeated Characters')
    print(count)
    return 0

print(FirstRepeatedChar(['c','a','r','e','e','r','m','o','n','k']))
"""

'''
Dynamic Programming
'''
'''
Fibonacci Series
'''

# Method 1
def fib1(n):
    fibTable = [0,1]
    for i in range(2,n+1):
        fibTable.append(fibTable[i-1]+fibTable[i-2])
    return fibTable[n]

# print(fib1(10))

# Method 2
fibTable = {1:1, 2:1}
def fib2(n):
    if n <= 2:
        return 1
    if n in fibTable:
        return fibTable[n]
    else:
        fibTable[n] = fib2(n-1) + fib2(n-2)
        return fibTable[n]

# print(fib2(10))

# Method 3
def fib3(n):
    a,b = 0,1
    for i in range(n):
        a,b=b,a+b
    return a

# print(fib3(10))
    
'''
Factorial of a number
'''
# fact(n)
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
# print(fact(10))


factTable = {}
def factorial(n):
    try:
        return factTable[n]
    except KeyError:
        if n == 0:
            factTable[0] = 1
            return 1
        else:
            factTable[n] = n * factorial(n-1)
            return factTable[n]
        
# print(factorial(10))


'''
Longest Common Subsequence
'''
# def LCSLength(X,Y):
#     if not X or not Y:
#         return ""
#     x,m,y,n = X[0],X[1:],Y[0],Y[1:]
#     if x == y:
#         return x + LCSLength(m,n)
#     else:
#         return max(LCSLength(X,n),LCSLength(m,Y), key=len)

# print(LCSLength('thisisatest','testingLCS123testing'))


'''
DP Solution
'''
def LCSLength(X,Y):
    Table = [[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(X):
        for j,y in enumerate(Y):
            if x == y:
                Table[i+1][j+1] = Table[i][j]+1
            else:
                Table[i+1][j+1] = max(Table[i+1][j], Table[i][j+1])
    
    result = ""
    x,y = len(X), len(Y)
    while x != 0 and y != 0:
        if Table[x][y] == Table[x-1][y]:
            x-= 1
        elif Table[x][y] == Table[x][y-1]:
            y-=1
        else:
            assert X[x-1] == Y[y-1]
            result = X[x-1] + result
            x-=1
            y-=1
    return result

print(LCSLength('thisisatest','testingLCS123testing'))

