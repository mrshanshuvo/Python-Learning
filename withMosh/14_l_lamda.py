items = [
    ("product1", 10),
    ("product2", 20),
    ("product3", 6),
]


# def sort_item(item):
#     return item[1]


items.sort(key=lambda item: item[1])
print(items)
