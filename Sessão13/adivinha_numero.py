from random import randint
pc = randint(1,10)
cont = 3
user = 0
print('='*60)
print(f"{'ADIVINHAR NÚMERO SECRETO':^60}")
print('='*60)
while True:
    user = (int(input(f'Tente adivinhar um número entre 1 e 10.Tens {cont} tentativas!\nDigite aqui: ')))
    while user < 1 or user > 10:#Validação do número para que esteja dentro do intervalo solicitado
        user = (int(input(f'\nO número tem de ser entre 1 e 10.Tens {cont} tentativas!\nDigite aqui: ')))
    cont -= 1
    if user == pc :
        print('Parabéns!A C E R T O U')
        jogar = input('\nQuer jogar novamente [S/N]: ').strip().upper()
        cont = 3
        if jogar in 'Nn':
            print('\nFim do jogo!Obrigada')
            break
        print('\n')
    elif pc < user:
        print('o número secreto é menor!')
    else:
        print('O número secreto é maior!')
    if cont == 0:#Fim das tentativas
        print(f'O número secreto era {pc}!Boa sorte para a proxima!')
        jogar = input('\nQuer jogar novamente [S/N]: ').strip().upper()
        cont = 3
        if jogar in 'Nn':
            print('\nFim do jogo!Obrigada')
            break
        print('\n')



