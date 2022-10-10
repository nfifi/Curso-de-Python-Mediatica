print('*-*'*10)
print('Calculadora de Dois Números')
print('*-*'*10)
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
op = input('\nOperações:\nSoma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão (/)\nEscolha a operação pelo sinal: ')
if op == '+':
    print(f'\n{n1} + {n2} = {n1+n2}')
elif op == '-':
    print(f'\n{n1} - {n2} = {n1-n2}')
elif op == '*':
    print(f'\n{n1} * {n2} = {n1*n2}')
elif op == '/':
    if n2 == 0:
        print(f'\nO denominador é igual a {n2}.Cálculo Impossível!')
    else:
        print(f'\n{n1} / {n2} = {n1/n2:.2f}')
else:
    print('\nOperação Inválida!')