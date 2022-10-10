numeros = [1, 3, 2, 1, 1, 5, 1, 7, 1, 10, 1, 8, 2, 7, 1, 3]
nova_lista = list()
for num in numeros:
        if nova_lista.count(num) == 0:
            nova_lista.append(num)
print(nova_lista)