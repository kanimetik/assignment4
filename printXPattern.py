def transofrmDigits(n):
    s = str(n)
    result_str = ""
    for i in s:
        digit = int(i)
        if digit % 2 == 0:
            digit += 1
        else:
            digit -= 1
        result_str += str(digit)

    return int(result_str)

n = int(input())
print(transofrmDigits(n))

