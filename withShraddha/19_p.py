def print_list(list, idx):
    if (idx < 0):
        return
    print(list[idx])
    print_list(list, idx - 1)


list = [1, 2, 3, 4, 5]
idx = 4
print_list(list, idx)
