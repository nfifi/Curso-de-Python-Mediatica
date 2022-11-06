nomes = ('João', 'Carlos', 'Luisa', 'Luís')
apelidos = ('Santos', 'Meireles','Silva', 'Almeida')
idades = (17, 55, 39, 33)

tupla_unida = zip(nomes, apelidos, idades)
#print(tupla_unida) retrorna endereço de memoria
#mas podemos converter para tupla
pessoas = tuple(tupla_unida)
print(pessoas)
print('-='*15)
#podemos iterar os elementos num ciclo
for valores in pessoas:
    print(valores)

nomes, apelidos, idades = pessoas[1]
    
#print(next(tupla_unida)) # também podemos visualizar o 1º item mas o valor é consumido

#Swaping
x = 100
y = [1, 2, 3]
z = 'Python'

z, x, y = x , y, z
print(f'x = {x} , y = {y}, z = {z}')