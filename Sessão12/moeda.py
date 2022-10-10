from random import randint
moeda = ['cara','coroa']
palpite = input('Qual é o seu palpite [cara ou coroa]:' )
n = randint(0,1)
if moeda[n] == palpite.lower():
    print(f'A moeda foi ao ar e o resultado é {moeda[n]} e ACERTOU')   
else: 
    print(f'A moeda foi ao ar e o resultado é {moeda[n]} e ERROU') 
