import numpy as np
def PALU(array,vector):
    def upptsub(arr,vector):
        length = len(arr)
        returnedVector = [0 for i in range(length)]
        for i in range(length -1,-1,-1):
            if arr[i][i] == 0:
                continue
            sum = 0
            for j in range(length -1,i,-1):
                sum+=arr[i][j] * returnedVector[j]
            returnedVector[i] = (vector[i] - sum) / arr[i][i] 
        return returnedVector
    
    def lowtsub(arr,vector):
        length = len(array)
        returnedVector = [0 for i in range(length)]
        for i in range(length):
            if array[i][i] == 0:
                continue
            sum = 0
            for j in range(i):
                sum+=arr[i][j] * returnedVector[j]
            returnedVector[i] = (vector[i] - sum) / array[i][i] 
        return returnedVector

    length = len(array)
    L = []
    for i in range(length):
        temp = []
        for j in range(length):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        L.append(temp)
    max = array[0][0]
    row = 0
    for i in range(length):
        if (array[i][0] > max):
            row = i
            max = array[i][0]
    permMatrix = []
    for i in range(length):
        temp = []
        for j in range(length):     
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        permMatrix.append(temp)
    permMatrix[row][row] = 0
    permMatrix[0][0] = 0
    permMatrix[0][row] = 1
    permMatrix[row][0] = 1
    array = np.matmul(permMatrix,array)
    z = 0
    for i in range(z+1,length):
        for j in range(length):
            array[i][j] = array[i][j] - (array[i][z] * array[z][j] / array[z][z])
        L[i][z] = array[i][z] / array[z][z]
        z+=1

    return upptsub(array,lowtsub(L,vector))

A = [[4,-1,1],[-1,5,2],[1,2,6]]

def cholesky(a):
    length = len(a)
    L = [[0 for i in range(length)] for j in range(length)]
    L[0][0] = np.sqrt(a[0][0])
    for i in range(1,length):
        L[i][0] = a[i][0] / L[0][0]

    for i in range(1,length):
        for j in range(i+1):
            sum = 0
            if j == i:
                for z in range(j):
                    sum+=L[j][z] * L[j][z]
                L[i][i] = np.sqrt(a[i][i] - sum)
            else:
                for z in range(j):
                    sum +=L[i][z] * L[j][z]
                if (L[j][j] > 0):
                    L[i][j] = (a[j][i] - sum)/L[j][j]
    return L

def gauss(n):
    A = []
    k = 0
    for i in range(n):
        temp = [0 for k in range(n)]
        for j in range(n):
            if j == i:
                temp[j] = 5
                if i != n-1:
                    temp[j+1] = -2
                if i!= 0:
                    temp[j-1] = -2
            else:
                temp[j] = 0
        A.append(temp)
    b = []
    b.append(3)
    for i in range(n-2):
        b.append(1)
    b.append(3)
    x = [0 for i in range(n)]
    def iterate(x):
        x1 = x
        for i in range(n):
            sum1 = 0
            sum2 = 0
            for j in range(i):
                sum1 = sum1 + A[i][j]*x1[j]
            for j in range(i+1,n):
                sum2 = sum2 + A[i][j]*x[j]
            x1[i] = (1/A[i][i])*(b[i] - sum1 - sum2)
        return x1

    while(True):
        x1 = iterate(x)
        r = [x1[i] - x[i] for i in range(n)]
        if np.linalg.norm(r,np.inf) < 0.0001:
            return x
        x = x1

