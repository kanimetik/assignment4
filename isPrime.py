def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def countPrimesInRange(a, b):
    count = 0
    for num in range(a, b + 1):
        if isPrime(num):
            count += 1
    return count

a = int(input())
b = int(input())
result = countPrimesInRange(a, b)
print(result)

