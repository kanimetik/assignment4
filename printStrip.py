n = int(input())

def printHollowSquare(n):
    for i in range(n):
        print('#', end='')
    if i == 0 or i == n - 1:
        print('#')

printHollowSquare(n)