letters = ['a', 'b', 'c']

# Add
letters.append("d")
letters.insert(1, '-')
print(letters)

# Remove
# letters.pop()
# print(letters)
# letters.pop(1)
# print(letters)
# letters.remove('c')
# print(letters)


letters.append('a')
print(letters)

del letters[0:1]
print(letters)
letters.clear()
print(letters)
