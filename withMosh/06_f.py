def multiply(*numbers):
    mul = 1
    for number in numbers:
        mul *= number
    return mul


print("Start")
print(multiply(1, 2, 3))
