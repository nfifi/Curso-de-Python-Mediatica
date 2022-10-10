cont = 1
soma = 0
while True:
    n = int(input(f'Informe o {cont}º número: '))
    cont += 1
    soma += n
    continuar = input('Quer continuar [S/N]:').strip().upper()[0]
    if continuar == 'N':
        print(f'A soma dos números digitados foi {soma}.\nFim')
        break
