import numpy as np

def makeG(A,q,n):
    G = []
    for i in range(n):
        temp = []
        for j in range(n):
            sum = 0
            for k in range(n):
                sum+= A[j][k]
            temp.append((q/n) + (A[j][i]*(1-q) / sum))
        G.append(temp)
    return G
A = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

def findEigenvector(G,n):
    b = [1] * n
    for i in range(20):
        b = np.dot(G,b)
        norm = np.linalg.norm(b)
        b = [i/norm for i in b]
    sum = 0
    for i in b:
        sum+=i
    u = [j/sum for j in b]
    return u
    
G = makeG(A,0.15,15) 
o = findEigenvector(G,15)
#print(o)

A[0] = [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0]
G = makeG(A,0.15,15)
#print(findEigenvector(G,15))


L = makeG(A,0.02,15)
#print(findEigenvector(L,15))
U = makeG(A,0.6,15)
#print(findEigenvector(U,15))
Z = [findEigenvector(G,15)[j] - findEigenvector(L,15)[j] for j in range(15)]
#print(Z)
Z = [findEigenvector(G,15)[j] - findEigenvector(U,15)[j] for j in range(15)]
#print(Z)

A[0] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] 
#reverting to original 
A[7][10] = 3
A[11][10] = 3
G = makeG(A,0.15,15)
#print(findEigenvector(G,15))

newA = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]
I = makeG(newA,0.15,14)
k = findEigenvector(I,14)
F = [o[j] - k[j] for j in range(14)]
#print(F)