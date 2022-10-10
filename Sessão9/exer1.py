cont = 0
n = int(input('Digite um número para contar os seus digitos: '))
div = n
while div != 0:
    div //=10  # Divisão inteira
    cont += 1
print(n, 'tem um total de ',cont, 'digitos')

