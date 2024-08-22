numbers = [1, 2, 3, 4, 4, 5, 5, 5]
first = set(numbers)
print(first)

second = {1, 9}
# second.add(5)
# second.remove(4)
# len(second)

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
