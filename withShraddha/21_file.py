a, b, c = map(int, input().split())

num = []
num.append(a)
num.append(b)
num.append(c)
num.sort()

for i in num:
    print(i)
print(f'\n{a}\n{b}\n{c}')
