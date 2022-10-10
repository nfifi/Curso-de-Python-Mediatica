from random import randint
n1 = n2 = randint(1,9)
print('n1=',n1)
while n2 == n1:
    n2 = randint(1,9)
    print('n2=',n2)
n3 = randint(1,9)
print('n3=',n3)
while n3 == n2 or n3 == n1:
    n3 = randint(1,9)
    print('n3=',n3)
n4 = randint(1,9)
print('n4=',n4)
while n4 == n3 or n4 == n2 or n4 == n1:
    n4 = randint(1,9)
    print('n4=',n4)
n5 = randint(1,9)
print('n5=',n5)
while n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
    n5 = randint(1,9)
    print('n5=',n5)
nSorte = randint(1,10)
print('nSorte=',nSorte)
while nSorte == n5 or nSorte == n4 or nSorte == n3 or nSorte == n2 or nSorte == n1:
    nSorte = randint(1,13)
    print('nSorte=',nSorte)          
print(f'A chave do totoloto é {n1},{n2},{n3},{n4},{n5} - {nSorte}')
