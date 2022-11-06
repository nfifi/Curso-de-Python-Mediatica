from random import randint
pc = ['pedra','papel','tesoura']
while True:
    op = randint(0,2)
    while True:
        palpite = input('Introduza o seu palpite Pedra, Papel ou Tesoura: ').lower()
        if palpite in pc:
            break # interrompe o ciclo caso o palpite esteja certo
        print('Escolha errada!')
    if pc[op] == palpite:
        print(f'Jogou {palpite.upper()} e o computador jogou {pc[op].upper()}. Empate!')
    elif (pc[op] == 'pedra' and palpite == 'tesoura')or(pc[op] == 'tesoura' and palpite == 'papel')or(pc[op] == 'papel' and palpite == 'pedra'):
            print(f'Jogou {palpite.upper()} e o computador jogou {pc[op].upper()}. Ganhou o PC!')
    elif (palpite == 'pedra' and pc[op] == 'tesoura') or (palpite == 'tesoura' and pc[op] == 'papel') or( palpite == 'papel' and pc[op] == 'pedra'):
            print(f'Jogou {palpite.upper()} e o computador jogou {pc[op].upper()}. Ganhaste!')
    out = 'a'
    while out != 's' and out != 'n':
        out = input('Quer sair [S/N]: ').lower()
    if out =='s':
        print('\nFim do Programa')
        break
    print('=-'*35)        