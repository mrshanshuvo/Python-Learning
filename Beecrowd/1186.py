M = []
T = input()

for i in range(12):
    row = []
    for j in range(12):
        n = float(input())
        row.append(n)
    M.append(row)

index = 11
sec_dia_elements = []
for row in M:
    for i in range(12):
        if (i > index):
            sec_dia_elements.append(row[i])
    index -= 1

summation = sum(sec_dia_elements)
total_elements = len(sec_dia_elements)
if (T == 'S'):
    print(f'{summation:.1f}')
if (T == 'M'):
    avg = summation/total_elements
    print(f'{avg:.1f}')
