def multiply(*numbers):
    mul = 1
    for number in numbers:
        mul *= number
    return mul


print(multiply(2, 3, 4, 5))
