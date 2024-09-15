pa, pb, g1, g2 = map(float, input().split())

pa, pb = int(pa), int(pb)

count = 0
while True:
    pa = pa + round(pa * g1/100)
    pb = pb + round(pb * g2/100)
    count += 1
    if (pa > pb):
        break

print(f'{count} anos.')
