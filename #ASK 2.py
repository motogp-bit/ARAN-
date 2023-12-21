#ASK 2
import numpy as np
import math
import time
import random
error = 0.00001
def f(x):
    return 54*(x**6) +45*(x**5)-102*(x**4)-69*(x**3)+35*(x**2) +16*x -4
def df(x):
    return 324*(x**5) + 225*(x**4) - 408*(x**3) - 207*(x**2) + 70*x + 16
def ddf(x):
    return (df(x+error) - df(x)) / error
def new(x0,count):
    if abs(f(x0)) - error > 0:
        count+=1
        return new(x0 - 1/((df(x0)/f(x0))-(ddf(x0)/(2*df(x0)))),count)
    else:
        #print(count)
        return round(x0,5)
i = -2
set1 = set({})
while (i < 2):
    set1.add(new(i,0))
    i+=2/3
#for i in set1:
 #   print(i)
#print("Newton over")
def bis(a,b):
    count = 0
    c = (b-a) * abs(math.sin(time.time())) + a
    while abs(f(c)) - error > 0 and a!=b:
        if (f(c) < 0):
            b = c
        else:
            a = c     
        c = (b-a) * abs(math.sin(time.time())) + a
        count+=1
    #print(count)
    return round(c,5)            
set2 = set({})
i = -2
while i+2/3<2:
    set2.add(bis(i,i+2/3))
    i+=2/3
#for i in set2:
    #print(i)   

a = -2 
b = -1
#running bisection 20 times on [-2,-1] to compare convergence

c = (b-a) * random.random() + a
counts = 0
while abs(f(c)) - error > 0 and a!=b:
    if (f(c) < 0):
        b = c
    else:
        a = c     
    c = (b-a) * random.random() + a
    counts+=1
#print(counts)
#print("Secant method")
def sec(a,b,c,count):
    if abs(f(c)) - error > 0:
        r = f(c) / f(b)
        q = f(a) / f(b)
        s = f(c) / f(a)
        count+=1
        return sec(b,c,c - (r*(r-q)*(c-b) + (1-r)*s*(c-a))/((q-1)*(r-1)*(s-1)),count)
    else:
        #print(count)
        return round(c,5)
set3 = set({})
i = -2
while (i+2/3<2):
    set3.add(sec(i,i+1/3,i+2/3,0))
    i+=(1/3)
#for i in set3:
 #   print(i)  