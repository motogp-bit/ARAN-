import numpy as np
array = [[1,2,3],[-1,3,4],[0,2,-2]]
vector = [1,1,2]
#works for any nxn array
#in theory,PermMatrix is not needed,I could just swap the rows of the initial array directly
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

    length = length(array)
    permMatrix = [[0] for i in range(length)]
    L = [[0] for i in range(length)]
    for i in range(length):
        L[i][i] = 1
    max = array[0][0]
    row = 0
    for i in range (length):
        if (array[i][0] > max):
            row = i
            max = array[i][0]
    row = 0
    for i in range(length):
        for j in range(length):               
            if i == j:
                permMatrix[i][j] = 1
            else:
                permMatrix[i][j] = 0
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

def cholesky(a):
    length = len(a)
    L = [[0] for i in range(length)]
    L[0][0] = np.sqrt(a[0][0])
    for i in range(1,length):
        L[i][0] = a[i][0] / L[0][0]

    for i in range(1,length):
        for j in range(1,length):
            if j > i:
                continue
            elif j == i:
                sum = 0
                for z in range(i):
                    sum+=L[i][z] * L[i][z]
                L[i][i] = np.sqrt(a[i][i] - sum)
            else:
                sum = 0
                for z in range(i):
                    sum +=L[i][z] * L[j][z]
                L[j][i] = (a[j][i] - sum)/L[i][i]
    return L

def gauss(n):
    A = [[0] for i in range(n)]
    for i in range(n):
        A[i][i] = 5
        if i < n-1:
            A[i+1][i] = -2
            A[i][i+1] = -2
    b = []
    b[0] = 3
    b[n-1] = 3
    for i in range(1,n-1):
        b[i] = 1
    x = [0 for i in range(n)]
    while :
        x1 = x
        for i in range(n):
            sum1 = 0
            sum2 = 0
            for j in range(i):
                sum1 = sum1 + A[i][j]*x1[j]
            for j in range(i+1,n):
                sum2 = sum2 + A[i][j]*x[j]
            x1[i] = (1/A[i][i])*(b[i] - sum1 - sum2)
        x = x1
    return x
print(gauss[10])
print(gauss[10000])

