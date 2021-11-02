n = int(input())
for i in range(1, n+1):
    s, h = input().split(' ')
    if s == 'tesoura' and h == 'papel' or s == 'papel' and h == 'pedra' or s == 'pedra' and h == 'lagarto' or s == 'lagarto' and h == 'Spock' or s == 'Spock' and h == 'tesoura' or s == 'tesoura' and h == 'lagarto' or s == 'lagarto' and h == 'papel' or s == 'papel' and h == 'Spock' or s == 'Spock' and h == 'pedra' or s == 'pedra' and h == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i))
    elif s == h:
        print('Caso #{}: De novo!'.format(i))
    else:
        print('Caso #{}: Raj trapaceou!'.format(i))
