lista_numeros = [1,2,5,9,8,23,15,4,18,15,7,6,90,100,18,24]
v = int(input(f'Qual o valor a remover da lista {lista_numeros}: '))
if lista_numeros.count(v) == 0:
    print(f'O valor {v} não existe na lista {lista_numeros}!')
else:
    for i,num in enumerate(lista_numeros):
        if num == v:
            lista_numeros.pop(i)
    print(f'Foi removido o valor {v} da lista: {lista_numeros}')