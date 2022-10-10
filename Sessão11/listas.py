numeros = list()

numeros.append(9)
numeros.insert(0,6) #inserir um elemento num indice especifico
print(numeros)
numeros.clear() # apagar elementos da lista
print(numeros)
n1 = [1,2]
n2 = n1 #faz copia com ligação, portanto toda a alteração feita tanto numa como noutra lista , ranto uma como outra sofrerá a alteração.
n3 = n1.copy() #Faz copia sem ligação
print(n1)
print(n2)
print(n3)
n1.append(9)
print(n1)
print(n2)
print(n3)


