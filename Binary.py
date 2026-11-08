def isArmstrong(n):
    temp = n
    sum_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp //= 10
    return sum_cubes == n

print("Output:", end=" ")
for num in range(100, 1000):
    if isArmstrong(num):
        print(num, end=" ")