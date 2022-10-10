from random import randint
pc = randint (1,6)
cont = 0
while cont < 3:
    user = int (input('Tente acertar o número: '))
    cont += 1
    if user < pc:
        print('É menor do que o gerado!')
        if cont == 3:
            print('\nForam 3 tentativas.Lamentamos!')
    elif user > pc:
        print('É maior do que o gerado!')
        if cont == 3:
            print('\nForam 3 tentativas.Lamentamos!')
    else:
        print('Parabens!Acertou!')
        break
    print('\n')