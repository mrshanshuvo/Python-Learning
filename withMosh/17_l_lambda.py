items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


prices = list(map(lambda item: item[1], items))

print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))

print(filtered)

# Best Practice for above two situation
# [epression for item in items]
# [epression for item in items if item[1] >= 10]

prices = [item[1] for item in items]

print(prices)


filtered = [item for item in items if item[1] >= 10]
print(filtered)
