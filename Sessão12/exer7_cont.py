numeros = [1,3,2,1,1,5,1,7,1,10,1,8,2,7,1,3]
print(f'Lista original: {numeros}')
cont = 0
for n in numeros:
    print(f'Termo:{n}')
    print(f'ultimo numero: {numeros[len(numeros)-1]}')
    if n >= numeros[len(numeros)-1]:
        numeros.insert(len(numeros)-1,n)
        