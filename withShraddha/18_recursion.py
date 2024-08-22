def summation(n):
    if (n == 0):
        return 0
    return n + summation(n-1)


out = summation(5)
print(out)
