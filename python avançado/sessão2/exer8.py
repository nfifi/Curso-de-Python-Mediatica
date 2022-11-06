qtd = int(input('Quantos elementos terá a tupla: '))
tupla = ()
for i  in range(qtd):
    numero = (input(f'Entre com o {i+1}º elemento: '))
    tupla = tupla + tuple([numero]) # forçar que considere a palavra e que não faça a iteração da tupla, guarda como string
print(tupla)