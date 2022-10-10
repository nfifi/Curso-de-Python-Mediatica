from random import randint
result = randint(1,2)
result = 'Cara' if result == 1 else 'Coroa'
palpite = ' '
while palpite != 'Coroa' and palpite != 'Cara':
    palpite = input ('\nQual é o seu palpite[Cara/Coroa]: ').title()
if palpite == result:
    print(f'\nA moeda foi ao ar e o resultado é {result} e ACERTOU!')
else:
    print(f'\nA moeda foi ao ar e o resultado é {result} e ERROU!')