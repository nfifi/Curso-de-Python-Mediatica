lista_nomes = ['Luis','Paulo','Alexandre','Marcelo','Patricia','Tiago','Autilio','Nzola','Andreia','Daniela']
nome = str(input(f'Qual o nome a remover da lista {lista_nomes}: ')).strip().capitalize()
if lista_nomes.count(nome) == 0:
    print(f'O nome {nome} não existe na lista {lista_nomes}!')
else:
    for i,n in enumerate(lista_nomes):
        if n == nome:
            lista_nomes.pop(i)
    print(f'Foi removido o nome {nome} da lista: {lista_nomes}')