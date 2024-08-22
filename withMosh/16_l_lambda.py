items = [
    ("product1", 10),
    ("product2", 20),
    ("product3", 6),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
