cities = ["dhaka", "chandpur", "gazipur"]
heores = ["thor", 'ironman', 'black widow', "hulk"]


def avg(a, b, c):
    return ((a+b+c)/3)


print(avg(1, 2, 3))


def length(list):
    print(len(list))


length(cities)
length(heores)


def print_list(list):
    for i in list:
        print(i, end=" ")


print_list(cities)
