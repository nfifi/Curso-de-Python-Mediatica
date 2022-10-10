n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))


if(n1 > n2) and (n1 > n3):
    print('n1 Maior')
    if(n2 < n3):
        print('n2 é Menor')
    else:
        print('n3 é Menor') 
else:
    if(n2 > n1) and (n2 > n3):
        print('n2 Maior')
        if(n1 < n3):
            print('n1 é Menor')
        else:
    else:
        if(n3 > n1) and (n3 > n2):
            print('n3 Maior')
            if(n1 < n2):    print('n2 é Menor')
                print('n1 é Menor')
            else:
            