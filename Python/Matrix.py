# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:53:30 2022

@author: User
"""
import Vectors as V

class Matrix(object):
    def __init__(self, data):
        self.row = len(data)
        self.column = len(data[0])
        self.data = data
        
    def print_matrix(self):
        for i in range(self.column):
            for j in range(self.row):
                c=self.data[j][i]
                if type(c) == int:
                    print(self.data[j][i],end="\t")
                else:
                    if(abs(c)>0.0001):
                        print("{:5.3}".format(self.data[j][i]),end="\t")
                    else:
                        c = 0.0
                        print("{:5.3}".format(c),end="\t")
            print()
        return 
            
    def add(self,m):
        new_data = [[0 for i in range(self.column)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                new_data[i][j] = self.data[i][j] + m.data[i][j]
                
        new_matrix = Matrix(new_data)#,self.row,self.column)
        return new_matrix
    
    def sub(self,m):
        new_data = [[0 for i in range(self.column)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.column):
                new_data[i][j] = self.data[i][j] - m.data[i][j]
                
        new_matrix = Matrix(new_data)#,self.row,self.column)
        return new_matrix
    
    def mult(self,m):
        if(self.column==m.row):
            new_data = [[0 for i in range(self.column)] for j in range(m.row)]
            for i in range(self.column):
                for j in range(m.row):
                    s = 0
                    for k in range(m.column):
                        # print(s,self.data[i][k], m.data[k][j])
                        s += self.data[k][j] * m.data[i][k]
                    new_data[i][j] = s
                    
            new_matrix = Matrix(new_data)#,self.row,self.column)
            return new_matrix
        else:
            print("Sorry cannot multiply matrices")
    
    def transpose(self):
        new_data = [[self.data[j][i] for j in range(self.row)] for i in range(self.column)]
        return Matrix(new_data)
        
        
    
    def Q(self):
        x1 = V.Vector(self.data[0])
        x2 = V.Vector(self.data[1])
        x3 = V.Vector(self.data[2])
        
        v1 = x1
        
        p2 = v1.dot(x2)/v1.dot(v1)
        pp2 = v1.mult(p2)
        v2 = x2.minus(pp2)
        v2p = v2.mult(2)
        
        p31 = v1.dot(x3)/v1.dot(v1)
        pp31 = v1.mult(p31)
        p32 = v2p.dot(x3)/v2p.dot(v2p)
        pp32 = v2p.mult(p32)
        v3 = x3.minus(pp31)
        v3 = v3.minus(pp32)
        v3p = v3.mult(2)
        
        q1 = v1.normalize()
        q2 = v2p.normalize()
        q3 = v3p.normalize()
        # print(list((q1.coordinates)))
        
        q = Matrix([list(q1.coordinates),list(q2.coordinates),list(q3.coordinates)])
        return q
    
    def R(self):
        a = Matrix(self.data)
        q = self.Q()
        t = q.transpose()
        r = t.mult(a)
        return r
    
    # def LU(self):
    #     for r in range(self.row):
    #         a = True
    #         for c in range(self.column):
    #             if(self.data[r][c]) != 0:
    
    

l = [[1,-1,-1,1],[2,1,0,1],[2,2,1,2]]
w = [[1,0,2,-1],[-1,1,0,1],[2,0,0,-2]]
r = [[1,2,-1],[-1,0,1],[2,0,-2],[0,1,0]]
a = [[1,3],[2,4]]
b = [[5,7],[6,8]]
c = [[1,4],[2,5],[3,6]]
d = [[7,9,11],[8,10,12]]
e = [[4,5,6]]
f = [[1],[2],[3]]
g = [[1,-1,3],[3,1,4],[3,2,5]]
# h = [[1,-1,3],[3,1,4],[3,2,5]]
# k = [[10,11,12],[13,14,15],[16,17,18]]
# print(k[0][1])
# m1 = Matrix(l)
# m1.print_matrix()
# print()
# m2 = Matrix(r)
# m2.print_matrix()
# print()
# m1.mult(m2).print_matrix()
# m1.print_matrix()
# print()
# m2.print_matrix()
# print()
# # m1.add(m2).print_matrix()
# m1.mult(m2).print_matrix()
# q = m1.q()
# print(q.print_matrix())

m3 = Matrix(g)
m3.Q().print_matrix()
print()
m3.R().print_matrix()
# m3.print_matrix()
# print()
# m3.transpose().print_matrix()
# print()
# m3.R().print_matrix()
# mT = m3.transpose()
# mT.mult(m3).print_matrix()

# Row echelon form abrreviated
# function ToReducedRowEchelonForm(Matrix M) is
#     lead := 0
#     rowCount := the number of rows in M
#     columnCount := the number of columns in M
#     for 0 ≤ r < rowCount do
#         if columnCount ≤ lead then
#             stop function
#         end if
#         i = r
#         while M[i, lead] = 0 do
#             i = i + 1
#             if rowCount = i then
#                 i = r
#                 lead = lead + 1
#                 if columnCount = lead then
#                     stop function
#                 end if
#             end if
#         end while
#         if i ≠ r then Swap rows i and r
#         Divide row r by M[r, lead]
#         for 0 ≤ j < rowCount do
#             if j ≠ r do
#                 Subtract M[j, lead] multiplied by row r from row j
#             end if
#         end for
#         lead = lead + 1
#     end for
# end function

# Row Echelon form detailed
# function ToRowEchelonForm(Matrix M) is
#     nr := number of rows in M
#     nc := number of columns in M
    
#     for 0 ≤ r < nr do
#         allZeros := true
#         for 0 ≤ c < nc do
#             if M[r, c] != 0 then
#                 allZeros := false
#                 exit for
#             end if
#         end for
#         if allZeros = true then
#             In M, swap row r with row nr
#             nr := nr - 1
#         end if
#     end for
    
#     p := 0
#     while p < nr and p < nc do
#         label nextPivot:
#             r := 1
#             while M[p, p] = 0 do 
#                 if (p + r) <= nr then
#                     p := p + 1
#                     goto nextPivot
#                 end if
#                 In M, swap row p with row (p + r)
#                 r := r + 1
#             end while
#             for 1 ≤ r < (nr - p) do 
#                 if M[p + r, p] != 0 then
#                     x := -M[p + r, p] / M[p, p]
#                     for p ≤ c < nc do
#                         M[p + r, c] := M[p , c] * x + M[p + r, c]
#                     end for
#                 end if
#             end for
#             p := p + 1
#     end while
# end function
                