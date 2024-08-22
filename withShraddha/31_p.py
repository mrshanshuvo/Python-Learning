def checkEven():
    with open("practice.txt", 'r') as f:
        data = f.read()
        numbers = []
        num = ''
        for i in range(len(data)):
            if (data[i] == ','):
                n = int(num)
                numbers.append(n)
                num = ''
            else:
                num += data[i]
        return numbers


numbers = checkEven()
print(numbers)
count = 0
for i in numbers:
    i = int(i)
    if (i % 2 == 0):
        count += 1

print("Even numbers are: ", count)
