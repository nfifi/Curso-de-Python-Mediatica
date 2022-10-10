num = int(input('Digite um número: '))
cont = 0
while num < 0:
    num = int(input('Digite um número: '))
    print('Deve introduzir um número positivo!')
for n in range(1,num+1):
    if num%n==0:
        cont+=1
if cont <=2:
    print('É primo!')
else:
    print('Não é primo!')
