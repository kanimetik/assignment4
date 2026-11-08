n = int(input())

def printInvertedPiramid(n):
    for i in range(n, 0, -1):
        num_stars = (2 * i - 1)
        print('*'*num_stars)


printInvertedPiramid(n)