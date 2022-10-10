num = int(input('Digite um numero: '))
soma = 0
for n in range(1,num+1):
    print(n,end=' ')
    if n < num:
        print('+',end=' ')
    else:
        print('=',end=' ')
    soma+=n
print(soma)