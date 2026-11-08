def printXPattern(n):
    for i in range(n):
        row_str = ""
        for j in range(n):
            if j == i or j == n - 1 - i:
                row_str += "*"
            else:
                row_str += " "
        print(row_str)

n = int(input())
printXPattern(n)

