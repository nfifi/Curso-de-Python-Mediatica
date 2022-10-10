from random import sample
#sample() retorna um número especifico dos elementos, sem repeti-los.
#range() gera a sequência imutável de números a partir do inteiro inicial fornecido até o inteiro final.
chave = sample(range(1,50),6)
print(f'{chave[0]}, {chave[1]}, {chave[2]}, {chave[3]}, {chave[4]} - {chave[5]}')
