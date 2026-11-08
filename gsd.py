def gsd (a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a*b) // gsd(a, b)

a = int(input())
b = int(input())
print(lcm(a, b))
