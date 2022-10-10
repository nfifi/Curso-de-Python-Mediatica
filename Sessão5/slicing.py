#exer1
nome = 'Nzola'
apelido = 'Fifi'
idade = 34
print('-='*10)
#exer2
nome_Completo = nome +' ('+ apelido+')'
nomeCompleto = f'{nome} ({apelido})'
print('-='*10)
print('A' + nome_Completo +'tem' + idade + 'anos.\tconcatenação')
print(f'A {nome_Completo} tem {idade} anos.\tF Strings')
print('-='*10)
#exer3
tam_1 = len(nome_Completo)
tam_2 = len(nomeCompleto)
print(f'A frase {nomeCompleto} tem tamanho {tam_1}.')
print(f'A frase {nome_Completo} tem tamanho {tam_2}.')
print('-='*10)
#exer4
invert = nomeCompleto[::-1]
print(invert+'\tFrase Invertida')
print('-='*10)
#exer5
sem_parent = nomeCompleto[:6] + nome_Completo[7:11]
print(sem_parent+' tem '+str(idade)+' anos. ')