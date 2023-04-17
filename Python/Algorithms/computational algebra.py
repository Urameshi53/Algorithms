# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:20:45 2022

@author: User
"""

def absolute_error(a,b):
    return abs(a-b)

def relative_error(a,b):
    r = absolute_error(a,b)/a
    return round(r,4)

# def bisection_search()

# print(relative_error(0.00347,0.0035))

# Horner's Algorithm for nested multiplication
def nested(arr,x):
    p=arr[-1]
    i=len(arr)-1
    while i >= 0:
        p = arr[i]+x*p
        i -= 1
    return p

# arr=[5,3,-7,2]
# print(nested(arr,'x'))
'''
First
Nested Multiplication Pseudocode
integer i,n; real p,x
real array (ai)0:n
p = a(n)
for i = n-1 to 0
    p = a(i)+xp
end for

Second
Synthetic division pseudocode
integer i,n; real r
real array a(i)0:n, b(i)0:n-1
b(n-1) = a(n)
for i = n - 1 to 0
    b(i-1) = a(i) + rb(i)
end for

Third
integer i,n; real p,r
real array a(i)0:n, b(i)0:n-1
A = a(n); B=0
for i=n-1 to 0
    B = A + rB
    A = a(i) + rA
    
Fourth
Complete Horner's Algorithm Pseudocode
integer n,k,j
real r; real array a(i)0:n
for k=0 to n-1
    for j=n-1 to k
        a(j)=a(j)+ra(j+1)
    endfor
endfor
'''

'''
Algorithm for finding the derivative of a function
integer i,imin, n = 30
real error,y,x=0.5,h=1,emin=1
for i=1 to n
    h = 0.25h
    y = [sin(x+h)-sin(x)]/h
    error = abs(cos(x)-y)
    output i,h,y,error
    if error < emin then
        emin = error; imin = i
    endif
endfor
output imin,emin
'''

'''
Forward Elimination Algorithm
integer i,j,k; real array a(i,j)1:nx1:n, b(i)1:n
for k=1 to n-1
    for i=k+1 to n
        for j=k to n
            a(i,j) = a(i,j) - [a(i,k)/a(k,k)]*a(k,j) # Key Step
        endfor
        b(i) = b(i)-[a(i,k)/a(k,k)]*b(k)
    endfor
endfor

Improved Forward Elimination Pseudocode
integer i,j,k; real xmult; real array a(i,j)1:nx1:n, b(i)1:n
for k=1 to n-1
    for i=k+1 to n
        xmult = a(i,k)/a(k,k)
        a(i,k) = xmult
        for j=k+1 to n
            a(i,j)=a(i,j)-(xmult)*a(k,j)
        endfor
        b(i) = b(i) - (xmult)*b(k)
    endfor
endfor

Back Substitution Pseudocode
integer i,j,n; real sum; real array a(i,j)1:nx1:n, x(i)1:n, b(i)1:n
x(n) = b(n)/a(n,n)
for i=n-1 to 1
    sum = b(i)
    for j=i+1 to n
        sum = sum - a(i,j)*x(j)
    endfor
    x(i) = sum/a(i,i)
endfor

Naive_Gauss Pseudocode
procedure Naive_Gauss(n,a(i,j),b(i),x(i))
integer i,j,k,n;  real sum, xmult
real array a(i,j)1:nx1:n, b(i)1:n, x(i)1:n
for k = 1 to n-1
    for i=k+1 to n
        xmult = a(i,k)/a(k,k)
        a(i,k) = xmult
        for j=k+1 to n
            a(i,j)=a(i,j)-(xmult)*a(k,j)
        endfor
        b(i)=b(i)-(xmult)*b(k)
    endfor
endfor
x(n) = b(n)/a(n,n)
for i=n-1 to 1
    sum = b(i)
    for j=i+1 to n
        sum = sum - a(i,j)*x(j)
    endfor
    x(i) = sum/a(i,i)
endfor
endprocedure Naive_Gauss

Bisection Method
procedure Bisection(f,a,b,nmax,e)
integer n,nmax; real a,b,c,fa,fb,fc,error
fa=f(a)
fb=f(b)
if sign(fa) = sign(fb) then
    output a,b,fa,fb
    output "Function has same signs at a and b"
    return
endif
error = b - a
for n=0 to nmax
    error = error/2
    c = a + error
    fc = f(c)
    output n,c,fc,error
    if abs(error) < e then
        output "Convergence"
        return 
    endif
    if sign(fa) != sign(fc) then
        b = c
        fb = fc
    else
        a = c
        fa = fc
    endif
endfor
endprocedure Bisection

'''

