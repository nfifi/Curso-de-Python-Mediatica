
lim = int(input('Informe o limite: ')) 
primos = list()
while lim < 0:
    lim = int(input('Informe o limite: ')) 
for n in range(1,lim+1):
    cont=0
    for num in range(1,lim+1):
        if n % num == 0:
            cont+=1
    if cont==2:
        primos.append(n)
print(primos)
