lista_vazia = list()
idade = [10,15,8,9,17]
print(idade)
nome = ['Vitor','Joana','Paulo','Pedro','Ana','Rita']
print(nome)
nome[2] = 'Nzola'
for pos,n in enumerate(nome):
    print(f'O nome {n} da {pos+1}º posição tem {len(nome[pos])} caracteres e começa com a letra {(nome[pos][0].upper())} e termina com a letra {(nome[pos][len(nome[pos])-1])}.')
