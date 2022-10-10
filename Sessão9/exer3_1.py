resposta = 'S'
soma = 0 
while resposta in 'Ss':
    numero = int(input ('Digite um número: '))
    soma += numero
    resposta = input ('Quer continuar? [S ou s --> Sim / outra para sair]' )
print (f'A soma dos numeros digitados foi {soma}' )
print('Fim')
