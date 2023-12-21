#ASK 1
import numpy as np
import math
error = 0.00001
def f(x):
    return 12 - 26*x +20*(x**2)-7*(x**3) -12*(math.exp(x-2)) +14*x*(math.exp(x-2))
#numerical derivative 
def numdiff(x):
    return (f(x+error) - f(x))/error
#hand computed derivative
def exdiff(x):
    return -26 + 40*x - 21*(x**2) + 2*(math.exp(x-2)) + 14*x*(math.exp(x-2))
def bis(a,b):
    c = (a+b)/2.0
    count = 0
    while abs(f(c)) - error > 0:
        count+=1
        if (f(c) < 0):
            b = c
        else:
            a = c
        c = (a+b)/2.0
    #print("Number of iterations:",count)
    return round(c,5)
#f(0) > 0,f(1) < 0,f(3) > 0
#print(bis(0,1))
#print(bis(1,3))
def nnew(x0,count):
    if abs(f(x0)) - error > 0:
        count+=1
        return nnew(x0 - (f(x0)/numdiff(f(x0))),count)
    else:
        #print("Number of iterations:",count)
        return round(x0,5)
#print("Newton method on with initial guesses 1 and 2.5 respectively,numerical derivative.")
#print(nnew(1,0))
#print(nnew(2.5,0))
def dnew(x0,count):
    if abs(f(x0)) - error > 0:
        count+=1
        return dnew(x0 - (f(x0)/exdiff(f(x0))),count)
    else:
        #print("Number of iterations:",count)
        return round(x0,5)
#print("Newton method with initial guesses 1 and 2.5 respectively,exact derivative.")
#print(dnew(1,0))
#print(dnew(2.5,0))

def sec(x0,x1,count):
    if abs(f(x1)) - error > 0:
        count+=1
        return sec(x1,x1 - f(x1) * (x1-x0)/(f(x1) - f(x0)),count)
    else:
        print("Number of iterations:",count)
        return round(x1,5)
#print("Secant method with initial guesses (0,1),(2.5,3) respectively.")
#print(sec(1,0,0))
#print(sec(3,2.5,0))
