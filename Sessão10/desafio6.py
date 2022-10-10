from random import randint
soma = 0
numeros = [randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50)]
print(f'O maior de {numeros} é o {max(numeros)}')
print(f'O menor de {numeros} é o {min(numeros)}')
for num in numeros:
    soma += num
media = soma/len(numeros)
print(f'A media é igual a {media:.2f}')