print('*-*'*10)
print('Calculadora de Dois Números')
print('*-*'*10)
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
op = input('\nOperações:\nSoma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão (/)\nEscolha a operação pelo sinal: ')
match op:
    case "+":
        print(f'\n{n1} + {n2} = {n1+n2}')
    case "-":
        print(f'\n{n1} - {n2} = {n1-n2}')
    case "*":
        print(f'\n{n1} * {n2} = {n1*n2}')
    case "/":
        print(f'\nO denominador é igual a {n2}.Cálculo Impossível!') if n2 == 0 else print(f'\n{n1} / {n2} = {n1/n2}')
    case _:
        print('\nOperação Inválida!')