# numbers = [1, 2, 3]

# first, second, third = numbers

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# first, second, *others = numbers

# print(numbers)
# print(others)

first, *others, last = numbers

print(numbers)
print(first)
print(others)
print(last)
