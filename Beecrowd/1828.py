n = int(input())
count = 1
for i in range(3):
    a, b = map(str, input().split())
    if (a == b):
        print(f'Caso #{count}: De novo!')
        count += 1
    elif (a == 'tesoura' and b == 'papel'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'papel ' and b == 'pedra'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'pedra' and b == 'lagarto'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'lagarto' and b == 'Spock'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'Spock' and b == 'tesoura'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'tesoura' and b == 'lagarto'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'lagarto' and b == 'papel'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'papel' and b == 'Spock'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'Spock' and b == 'pedra'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    elif (a == 'pedra' and b == 'tesoura'):
        print(f'Caso #{count}: Bazinga!')
        count += 1
    else:
        print(f'Caso #{count}: Raj trapaceou!')
        count += 1
