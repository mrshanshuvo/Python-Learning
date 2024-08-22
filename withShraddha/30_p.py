with open("practice.txt", 'r') as f:
    data = f.read()

num = ''
for i in range(len(data)):
    if (data[i] == ','):
        print(num)
        num = ''
    else:
        if (data[i] != ' '):
            num += data[i]
