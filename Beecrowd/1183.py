T = input()
M = []
for i in range(12):
    row = []
    for j in range(12):
        n = float(input())
        row.append(n)
    M.append(row)

upper_elements = []
count = 0
for row in M:
    for i in range(count, 12):
        upper_elements.append(row[i])
    count += 1

summation = sum(upper_elements)
total_elements = len(upper_elements)
if (T == 'S'):
    print(f'{summation:.1f}')
if (T == 'M'):
    avg = summation/total_elements
    print(f'{avg:.1f}')
