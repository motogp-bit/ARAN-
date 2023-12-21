import numpy as np
q = 0.15
n = 15

def makeG(A,q):
    for i in range(n):
        for j in range(n):
            if A[j][i] == 0:
                G[i][j] = 1/100 #q/n
            else:
                sum = 0
                for z in range(n):
                   sum+=A[j][z]
                G[i][j] = 1/100 + 0.85/sum
    return G
G = [[0]*n]*n
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


G = makeG(A,q)

def findEigenvector(G):
    b = [1] * n
    for i in range(15):
        b = np.dot(G,b)
        norm = np.linalg.norm(b)
        b = [i/norm for i in b]
    return b
print(findEigenvector(G))

#Θα βελτιωσουμε τη σημαντικοτητα της πρωτης σελιδας
A[0] = [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0]
G = makeG(A,q)
print(findEigenvector(G))
#Η σημαντικοτητα της σχεδον διπλασιαστηκε

q = 0.02
G = makeG(A,q)
print(findEigenvector(G))
q = 0.6
G = makeG(A,q)
print(findEigenvector(G))


A[7][10] = 3
A[11][11] = 3
q = 0.15
G = makeG(A,q)
print(findEigenvector(G))

arr = np.delete(A,9,axis = 0)
arr = np.delete(arr,[0],axis = 9)
G = makeG(A,q)
print(findEigenvector(G))