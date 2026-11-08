n = int(input())
m = int(input())
lastInteger = m * n

def printMatrix(n, m):
    for i in range(1, lastInteger + 1):
        if i % 3 == 0:
            print(i, end=" ")
            print()  
        else:
            print(i, end=" ")



printMatrix(n, m)