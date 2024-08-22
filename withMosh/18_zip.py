list1 = [1, 2, 3]
list2 = [10, 20, 30]

list3 = zip(list1, list2)
print(list3)

for i in list3:
    print(i)

list4 = list(zip(list1, list2))
print(list4)

list4 = list(zip("abc", list1, list2))
print(list4)
