# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:03:00 2022

@author: User
"""

class PriorityQueue(object):
    def __init__(self, A=[]):
        self.A = self.buildHeap(A)
        
    @staticmethod
    def heapify(A, i):
        l = 2*i
        r = 2*i+1
        if l < len(A) and A[l].value > A[i].value:
            largest = l
        else:
            largest = i
        if r < len(A) and A[r].value > A[largest].value:
            largest = r 
        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            PriorityQueue.heapify(A, largest)
        return A
    
    @staticmethod
    def buildHeap(A):
        n = len(A)
        i = (n//2)
        while i>=0:
            PriorityQueue.heapify(A,i)
            i -= 1
        return A

    def extractMax(self):
        if len(self.A) < 1:
            print("Error: Heap Overflow")
            return
        maximum = self.A[0]
        self.A[0] = self.A[len(self.A)]
        self.A.pop(0)
        self.heapify(self.A,0)
        return maximum
    
    def extractMin(self):
        m = self.A[-1]
        self.A.pop(-1)
        return m
        
    
    def heapMaximum(self):
        return self.A[0]
    
    def heapIncreaseKey(self, old, key):
        i = self.A.index(old)
        p = (i//2)
        if key < self.A[i].value:
            print("Error: Key is smaller than current key")
            return
        self.A[i].value = key 
        while i > 0 and self.A[p].value < self.A[i].value:
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p
            p=i//2
        return self.A
    
    def heapInsert(self, key):
        self.A.append(key)
        self.buildHeap(self.A)
        return self.A
    
    def heapAdd(self,key):
        self.A.append(-1)
        self.heapIncreaseKey(-1,key)
        return self.A
    
    def printQueue(self):
        for i in self.A:
            print(i)
            
    def isEmpty(self):
        return len(self.A)<1
    
    def search(self,x):
        return x in self.A
           
    @staticmethod
    def heapSort(A):
        B = []
        A = PriorityQueue.buildHeap(A)
        n = len(A)
        i=n-1
        while i!=1:
            A[0],A[i] = A[i],A[0]
            B.append(A.pop(i))
            i -= 1
            PriorityQueue.heapify(A,0)
        B.append(A[0])
        B.append(A[1])
        return B

class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, x):
        self.items.append(x)
        
    def dequeue(self):
        x = self.items[0]
        self.items.pop(0)
        return x
        
    def isEmpty(self):
        return len(self.items)<1
        
    def printQueue(self):
        for i in self.items:
            print(i)

class Stack(object):
    def __init__(self):
        self.items = []
        
    def push(self,x):
        self.items.insert(0,x)
        
    def pop(self):
        s = self.items[0]
        self.items.pop(0)
        return s
        
    def isEmpty(self):
        return len(self.items)<1

    def printStack(self):
        for i in self.items:
            print(i)

class Vertex(object):
    def __init__(self, value):
        self.value = value 
        self.parent = None 
        self.distance = 0
        self.color = 'WHITE'
        self.explored = False
        self.key = None
        
    # def __repr__(self):
    #     return self.value

class Edge(object):
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
        
    def getWeight(self,v1,v2):
        if self.v1 == v1 and self.v2 == v2:
            return self.weight
        
class Graph(object):
    time = 0
    
    def __init__(self):
        self.Edges = []
        self.Vertices = {}
        
    def addEdge(self, a, b,weight=0):
        newEdge = Edge(a,b,weight)
        self.Edges.append(newEdge)
        for i in self.Vertices:
            if i.value == a.value:
                self.Vertices[i].append(b)
                break
            
    def getEdgeWeight(self,v1,v2):
        for i in self.Edges:
            if i.v1 == v1 and i.v2 == v2:
                return i.weight
     
    def addVertex(self, v):
        self.Vertices[v]=[]
        
    def printGraph(self):
        for i in self.Vertices:
            print(i.value,end='->')
            for j in self.Vertices[i]:
                print(j.value, end='->')
            print()
            
    def BreadthFirstSearch(self,s):
        # for u in self.Vertices[s]:
        #     u.color = 'WHITE'
        #     u.distance = 100 
        #     u.parent = None
        s.color = 'GRAY'
        s.distance = 0 
        s.parent = None 
        Q = Queue()
        Q.enqueue(s)
        while not Q.isEmpty():
            u = Q.dequeue()
            # print(u.value,u.distance)
            for v in self.Vertices[u]:
                if v.color == 'WHITE':
                    v.color = 'GRAY'
                    v.distance = u.distance + 1 
                    v.parent = u
                    Q.enqueue(v)
            u.color = 'BLACK'    
            
    # Wikepedia
    def BFS(self, x, a):
        Q = Queue()
        x.explored = True 
        Q.enqueue(x)
        while not Q.isEmpty():
            v = Q.dequeue()
            if v.value == a.value:
                return True
            for u in self.Vertices:
                for v in self.Vertices[u]:
                    if v.explored == False:
                        v.explored = True
                        Q.enqueue(v)
                        
    def printPath(self,s,v):
        self.DepthFirstSearch()
        # self.mst_prim(s)
        # self.dijkstra(0, s)
        if v == s:
            print(s.value)
        elif v.parent == None:
            print('No path from',s.value,'to',v.value,'exists.')
        else:
            self.printPath(s,v.parent)
            print(v.value)
            
    # My own Depth First Search
    def mDepthFirstSearch(self,s):
        s.distance = 0
        s.color = 'GRAY'
        s.parent = None 
        S = Stack()
        S.push(s)
        while not S.isEmpty():
            u = S.pop()
            for v in self.Vertices[u]:
                if v.color == 'WHITE':
                    v.parent = u
                    v.distance = u.distance + 1
                    v.color = 'GRAY'
                    S.push(v)
            u.color = 'BLACK'
        
    def DepthFirstSearch(self):
        for u in self.Vertices:
            if u.color == 'WHITE':
                self.DepthFirstSearchVisit(u)
    
    def DepthFirstSearchVisit(self, u):
        self.time = self.time + 1
        u.distance = self.time
        u.color = 'GRAY'
        for v in self.Vertices[u]:
            if v.color == 'WHITE':
                v.parent = u
                self.DepthFirstSearchVisit(v)
        u.color = 'BLACK'
        self.time += 1
        # print(u.value,u.color,self.time)

        
        
    # Wikepedia - Recursive
    def DFS(self,s):
        s.explored = True
        for u in self.Vertices:
            for v in self.Vertices[u]:
                print(v.value)
                if v.explored == False:
                    return self.DFS(v)
                else:
                    return True
                    
    def DFS_iterative(self,s):
        S = Stack()
        S.push(s)
        while not S.isEmpty():
            v = S.pop()
            if v.explored == False:
                v.explored == True
                for u in self.Vertices[v]:
                    S.push(w)
                    
    def DFStack(self, s, x):
        found = False 
        s.explored = True
        S = Stack() 
        S.push(s)
        while not S.isEmpty():
            v = S.pop() 
            print(v.value)
            if v.value == x.value:
                found = True 
                break
            for w in self.Vertices[v]:
                if not w.explored:
                    w.explored = True 
                    S.push(w)
        return found 
    
    def bellmanFord(self, w, s):
        self.initialize(s)
        for i in range(len(self.Vertices)-1):
            for e in self.Edges:
                self.relax(e.v1,e.v2,e.weight)
        for e in self.Edges:
            if e.v1.distance > (e.v2.distance+e.weight):
                return False 
        return True       
    
    def mst_prim(self,s):
        # path = []
        # last = None
        for v in self.Vertices:
            for u in self.Vertices[v]:
                u.key = 100
                u.parent = None
        s.key = 0
        Q = PriorityQueue()
        for v in self.Vertices:
            Q.heapInsert(v)
        while not Q.isEmpty():
            u = Q.extractMin()
            print(u.value,'------')
            for v in self.Vertices[u]:
                print(v.value,v.key)
                if Q.search(v) == True and self.getEdgeWeight(u,v) < v.key:
                    # path.append(u.value)
                    v.parent = u
                    v.key = self.getEdgeWeight(v, u)
                    # last = v
        # self.printPath(s,last)
        # print(path)
        
    def initialize(self,s):
        for v in self.Vertices:
            for u in self.Vertices[v]:
                v.distance = 100
                v.parent = None 
        s.distance = 0
        
    def relax(self,u,v,w):
        if v.distance > u.distance + self.getEdgeWeight(u,v):
            v.distance = u.distance + self.getEdgeWeight(u,v)
            v.parent = u
            
    def bellman_ford(self,w,s):
        self.initialize(s)
        for i in range(len(self.Vertices)-1):
            for i in self.Edges:
                self.relax(i.v1,i.v2,w)
        for i in self.Edges:
            # print(self.getEdgeWeight(i.v1, i.v2),i.v1.value,i.v2.value,i.v1.distance,i.v2.distance)
            if i.v1.distance > i.v2.distance + self.getEdgeWeight(i.v2,i.v1):
                return False 
        return True
    
    def dijkstra(self,w,s):
        self.initialize(s)
        S = set()
        Q = PriorityQueue(list(self.Vertices.keys()))
        # print(list(self.Vertices.values()))
        # return 0
        while not Q.isEmpty():
            u = Q.extractMin()
            S = S.add(u)
            for u in self.Vertices:
                for v in self.Vertices[u]:
                    self.relax(u,u,w)
        
    



# D = DoublyLinkedList()
# a = Vertex(1)
# b = Vertex(2)
# c = Vertex(3)
# d = Vertex(4)
# e = Vertex(5)
# f = Vertex(6)

# G = Graph()
# G.addVertex(a)
# G.addVertex(b)
# G.addVertex(c)
# G.addVertex(d)
# G.addVertex(e)
# G.addVertex(f)

# G.addEdge(a,b)
# G.addEdge(a,d)
# G.addEdge(d,b)
# G.addEdge(b,e)
# G.addEdge(e,d)
# G.addEdge(c,e)
# G.addEdge(c,f)
# G.addEdge(f,f)
# G.printGraph()
# G.BreadthFirstSearch(a)


# Q = Queue()
# Q.enqueue(1)
# Q.enqueue(2)
# Q.enqueue(3)
# Q.printQueue()
# Q.dequeue()
# print('Dequeued')
# Q.printQueue()

# r = Vertex('r')
# s = Vertex('s')
# t = Vertex('t')
# u = Vertex('u')
# v = Vertex('v')
# w = Vertex('w')
# x = Vertex('x')
# y = Vertex('y')

# G = Graph()
# G.addVertex(r)
# G.addVertex(s)
# G.addVertex(t)
# G.addVertex(u)
# G.addVertex(v)
# G.addVertex(w)
# G.addVertex(x)
# G.addVertex(y)

# G.addEdge(r,s)
# G.addEdge(s,r)
# G.addEdge(s,w)
# G.addEdge(w,s)
# G.addEdge(r,v)
# G.addEdge(v,r)
# G.addEdge(w,t)
# G.addEdge(t,w)
# G.addEdge(t,x)
# G.addEdge(x,t)
# G.addEdge(w,x)
# G.addEdge(x,w)
# G.addEdge(t,u)
# G.addEdge(u,t)
# G.addEdge(x,u)
# G.addEdge(u,x)
# G.addEdge(x,y)
# G.addEdge(y,x)
# G.addEdge(u,y)
# G.addEdge(y,u)
# G.printGraph()
# G.BreadthFirstSearch(s)
# G.DepthFirstSearch()
# G.printPath(u, z)
# G.printPath(s, y)
# print(G.DFS(r))
# print(G.BFS(s, y))
# print(G.DFStack(s,y))
# S = Stack()
# S.push(1)
# S.push(2)
# S.push(3)
# S.printStack()
# S.pop()
# S.printStack()


# dallas = Vertex('Dallas')
# austin = Vertex('Austin')
# denver = Vertex('Denver')
# washington = Vertex('Washington')
# atlanta = Vertex('Atlanta')
# houston = Vertex('Houston')
# chicago = Vertex('Chicago')

# t1 = Edge(dallas,austin,200)
# t2 = Edge(austin,dallas,200)
# t3 = Edge(dallas,chicago,900)
# t4 = Edge(dallas,denver,780)
# t5 = Edge(austin,houston,160)
# t6 = Edge(denver,chicago,1000)
# t7 = Edge(denver,atlanta,1400)
# t8 = Edge(chicago,denver,1000)
# t9 = Edge(washington,atlanta,600)
# t10 = Edge(atlanta,washington,600)
# t11 = Edge(atlanta,houston,800)
# t12 = Edge(houston,atlanta,800)

# print(Edge(dallas,austin,200).weight)
# print(G.bellmanFord(w, s))
# T = Graph()
# G.mst_prim(s)

# a = Vertex('a')
# b = Vertex('b')
# c = Vertex('c')
# d = Vertex('d')
# e = Vertex('e')
# f = Vertex('f')
# g = Vertex('g')
# h = Vertex('h')
# i = Vertex('i')

# P = Graph()
# P.addVertex(a)
# P.addVertex(b)
# P.addVertex(c)
# P.addVertex(d)
# P.addVertex(e)
# P.addVertex(f)
# P.addVertex(g)
# P.addVertex(h)
# P.addVertex(i)

# P.addEdge(a,b,4)
# P.addEdge(b,a,4)
# P.addEdge(a,h,8)
# P.addEdge(h,a,8)
# P.addEdge(b,c,8)
# P.addEdge(c,b,8)
# P.addEdge(b,h,11)
# P.addEdge(h,b,11)
# P.addEdge(h,i,7)
# P.addEdge(i,h,7)
# P.addEdge(h,g,1)
# P.addEdge(g,h,1)
# P.addEdge(i,c,2)
# P.addEdge(c,i,2)
# P.addEdge(c,d,7)
# P.addEdge(d,c,7)
# P.addEdge(c,f,4)
# P.addEdge(f,c,4)
# P.addEdge(d,e,9)
# P.addEdge(e,d,9)
# P.addEdge(d,f,14)
# P.addEdge(f,d,14)
# P.addEdge(f,e,10)
# P.addEdge(e,f,10)

# P.printGraph()
# P.printPath(a,e)

# s = Vertex('s')
# t = Vertex('t')
# x = Vertex('x')
# y = Vertex('y')
# z = Vertex('z')

# T = Graph()
# T.addVertex(s)
# T.addVertex(t)
# T.addVertex(x)
# T.addVertex(y)
# T.addVertex(z)
# T.addEdge(s,t,6)
# T.addEdge(s,y,7)
# T.addEdge(t,x,5)
# T.addEdge(t,y,8)
# T.addEdge(t,z,-4)
# T.addEdge(x,t,-2)
# T.addEdge(y,z,9)
# T.addEdge(y,x,-3)
# T.addEdge(z,s,2)
# T.addEdge(z,x,7)
# T.printPath(s, t)

# D = Graph()
# s = Vertex('s')
# t = Vertex('t')
# x = Vertex('x')
# y = Vertex('y')
# z = Vertex('z')

# D.addVertex(s)
# D.addVertex(t)
# D.addVertex(x)
# D.addVertex(y)
# D.addVertex(z)

# D.addEdge(s,t,10)
# D.addEdge(s,y,5)
# D.addEdge(t,y,2)
# D.addEdge(t,x,1)
# D.addEdge(y,z,2)
# D.addEdge(y,x,9)
# D.addEdge(y,t,3)
# D.addEdge(x,z,4)
# D.addEdge(z,x,6)
# D.addEdge(z,s,7)
# D.printPath(s, x)

H = Graph()

u = Vertex('u')
v = Vertex('v')
w = Vertex('w')
x = Vertex('x')
y = Vertex('y')
z = Vertex('z')

H.addVertex(u)
H.addVertex(v)
H.addVertex(w)
H.addVertex(x)
H.addVertex(y)
H.addVertex(z)

H.addEdge(u,v)
H.addEdge(u,x)
H.addEdge(v,y)
H.addEdge(x,v)
H.addEdge(y,x)
H.addEdge(w,y)
H.addEdge(w,z)
H.addEdge(z,z)

H.printPath(u, x)
# H.DepthFirstSearch()













