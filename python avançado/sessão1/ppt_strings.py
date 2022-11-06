#importar a biblioteca para gerar números aleatórios
from random import randint
print(f"{'Pedra, Papel e Tesoura':^60}")
print('=-'*35)
while True:
    op = randint(1,3)
    match op:
        case 1:
            pc = 'pedra'
        case 2:
            pc = 'papel'
        case 3:
            pc = 'tesoura'
    while True:
        palpite = input('Introduza o seu palpite Pedra, Papel ou Tesoura: ').lower()
        if palpite == 'pedra' or palpite == 'papel' or palpite == 'tesoura':
            break # interrompe o ciclo caso o palpite esteja certo
        print('Escolha errada!')
    if pc == palpite:
        print(f'Jogou {palpite} e o computador jogou {pc}. Empate!')
    elif (pc == 'pedra' and palpite == 'tesoura') or (pc == 'tesoura' and palpite == 'papel') or (pc == 'papel' and palpite == 'pedra'):
            print(f'Jogou {palpite.upper()} e o computador jogou {pc.upper()}. Ganhou o PC!')
    elif (palpite == 'pedra' and pc == 'tesoura') or (palpite == 'tesoura' and pc == 'papel') or( palpite == 'papel' and pc == 'pedra'):
            print(f'Jogou {palpite.upper()} e o computador jogou {pc.upper()}. Ganhaste!')
    out = 'a'
    while out != 's' and out != 'n':
        out = input('Quer sair [S/N]: ').lower()
    if out =='s':
        print('\nFim do Programa')
        break
    print('=-'*35)