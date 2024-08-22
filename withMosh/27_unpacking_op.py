numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)

numbers = list(range(5))

print(numbers)

values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
values = [*first, 'a', second, *"Hello"]
print(values)


first = {'x': 1}
second = {'x': 10, 'a': 2}

combined = {**first, **second, 'z': 32}
print(combined)
