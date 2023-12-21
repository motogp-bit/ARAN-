#ASK 2
import numpy as np
import random
error = 0.00001
def f(x):
    return 54*(x**6) +45*(x**5)-102*(x**4)-69*(x**3)+35*(x**2) +16*x -4
def df(x):
    return 324*(x**5) + 225*(x**4) - 408*(x**3) - 207*(x**2) + 70*x + 16
def ddf(x):
    return (df(x+error) - df(x)) / error
def new(x0):
    if abs(f(x0)) - error > 0:
        return new(x0 - 1/((df(x0)/f(x0))-(ddf(x0)/(2*df(x0)))))
    else:
        return round(x0,5)
i = -2
set1 = set({})
#function has at most 6 real solutions,so we split our search into 6 equal subsets of length (2-(-2))/6 = 4/6 = 2/3
#this way we have better odds of finding the solutions
while (i < 2):
    set1.add(new(i))
    i+=2/3
for i in set1:
    print(i)

def bis(a,b):
    c = (b-a) * random.random() + a
    while abs(f(c)) - error > 0 and a!=b:
        if (f(c) < 0):
            b = c
        else:
            a = c     
        c = (b-a) * random.random() + a
    return round(c,5)            
set2 = set({})
i = -2
while i+1<2:
    set2.add(bis(i,i+1))
    i+=1
for i in set2:
    print(i)   

#running bisection 20 times on [-2,-1] to compare convergence
for j in range(20):
    c = (b-a) * random.random() + a
    counts = 0
    while abs(f(c)) - error > 0 and a!=b:
        if (f(c) < 0):
            b = c
        else:
            a = c     
        c = (b-a) * random.random() + a
        counts+=1
    print(counts)
    
def sec(a,b,c):
    if abs(f(c)) - error > 0:
        r = f(c) / f(b)
        q = f(a) / f(b)
        s = f(c) / f(a)
        return sec(b,c,c - (r*(r-q)*(c-b) + (1-r)*s*(c-a))/((q-1)*(r-1)*(s-1)))
    else:
        return round(c,5)
set3 = set({})
i = -2
while (i+2/3<2):
    set3.add(sec(i,i+1/3,i+2/3))
    i+=(1/3)
for i in set3:
    print(i)  