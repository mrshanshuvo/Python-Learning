def print_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


print_fact(5)


def print_fact(n):
    if (n == 1):
        return 1
    else:
        return n * print_fact(n-1)


output = print_fact(10)
print(output)
