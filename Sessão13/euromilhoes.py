from random import sample
numeros_user = list()
estrelas_user = list()
print('SORTEIO EUROMILHÕES [5 NÚMEROS + 2 ESTRELAS]')
while True:
    numeros_pc = sample(range(1,50),5)
    estrelas_pc = sample(range(1,12),2)
    cont_s = cont_n = 0
    op = input('Quer aposta manual ou automatica [M/A]: ').strip().upper()
    while op != 'M' and op != 'A':
        print('Opção não válida!')
        op = input('Quer aposta manual ou automatica [M/A]: ').strip().upper()
    match op:
        case 'M':
            for n in range(5):
                num = int(input(f'Digite o {n+1}º número do Euromilhões: '))
                while num < 1 or num > 50 or numeros_user.count(num)== 1: 
                    print('Número Inválido ou Já foi introduzido!',end=' ')
                    num = int(input(f'Digite o {n+1}º número do Euromilhões: '))
                numeros_user.append(num)
            for s in range(2):
                star = int(input(f'Digite a {s+1}º estrela do Euromilhões: '))
                while star < 1 or star > 12 or estrelas_user.count(star)== 1: 
                    print('Estrela Inválido ou Já foi introduzido!',end=' ')
                    star = int(input(f'Digite a {s+1}º estrela do Euromilhões: '))
                estrelas_user.append(star)
        case 'A':
            numeros_user = sample(range(1,50),5)
            estrelas_user = sample(range(1,12),2)
    #Verificar se exiStem números iguais
    for n in numeros_pc:
        if n in numeros_user:
            cont_n+=1
    for s in estrelas_pc:
        if s in estrelas_user:
            cont_s+=1
    print(f'\nA sua aposta ordenada no euromilhões é: {sorted(numeros_user)} + {sorted(estrelas_user)}')
    print(f'A chave do euromilhões ordenada é: {sorted(numeros_pc)} + {sorted(estrelas_pc)}')
    print(f'Acertou em {cont_n} numeros e {cont_s} estrelas!')
    #Output dos Premios
    if cont_n == 5:
        if cont_s == 2:
            print('Parabens!Ganhou o 1ºPremio!')
        elif cont_s == 1:
            print('Parabens!Ganhou o 2ºPremio!')
        elif cont_s == 0:
            print('Parabens!Ganhou o 3ºPremio!')
    elif cont_n == 4:
        if cont_s == 2:
            print('Parabens!Ganhou o 4ºPremio!')
        elif cont_s == 1:
            print('Parabens!Ganhou o 5ºPremio!')
        elif cont_s == 0:
            print('Parabens!Ganhou o 7ºPremio!')
    elif cont_n == 3:
        if cont_s == 2:
            print('Parabens!Ganhou o 6ºPremio!')
        elif cont_s == 1:
            print('Parabens!Ganhou o 9ºPremio!')
        elif cont_s == 0:
            print('Parabens!Ganhou o 10ºPremio!')
    elif cont_n == 2:
        if cont_s == 2:
            print('Parabens!Ganhou o 8ºPremio!')
        elif cont_s == 1:
            print('Parabens!Ganhou o 12ºPremio!')
        elif cont_s == 0:
            print('Parabens!Ganhou o 13ºPremio!')
    elif cont_n == 1 and cont_s == 2:
            print('Parabens!Ganhou o 11ºPremio!')
    else:
        print('Não tem prémio! Tente novamente!')
    jogar = input('Quer tentar novamente [S/N]: ').strip().upper()
    while jogar != 'S' and jogar != 'N':
        jogar = input('Quer tentar novamente [S/N]: ').strip().upper()
    if jogar == 'N':
        print(f"{'Fim do Jogo!':-^10}")
        break