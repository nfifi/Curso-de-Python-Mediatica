from random import randint
chave = list()
while True:
    n = randint(1,49)
    if chave.count(n) == 0:
        chave.append(n)
    if len(chave) == 5:
        break
print(f'A chave do totoloto é {chave} + {randint(1,13)}')