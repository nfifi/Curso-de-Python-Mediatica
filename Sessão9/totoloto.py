from random import randint
n1 = randint(1,49)
n2 = randint(1,49)
while n2 == n1:
    n2 = randint(1,49) 
n3 = randint(1,49)
while n3 == n2 or n3 == n1:
    n3 = randint(1,49)   
n4 = randint(1,49)
while n4 == n3 or n4 == n2 or n4 == n1:
    n4 = randint(1,49)
n5 = randint(1,49)
while n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
    n5 = randint(1,49)  
nSorte = randint(1,13)  
print(f'\nA chave do totoloto é {n1},{n2},{n3},{n4},{n5} - {nSorte}')

