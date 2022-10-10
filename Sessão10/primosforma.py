#imprimir todos os primos de 1 ate um numero limite introduzido pelo utilizador
limite = int(input('Até que limite deseja imprimir os números primos? : '))
if limite < 1:
    print('Deve introduzir um numero positivo!')
else: 
    primos=[] #cria a lista primos
    for numero in range(1,limite+1):
        contador=0 #contador de restos = 0
        for divisor in range(1,numero+1):    
            if numero%divisor==0:
                contador+=1 
        if contador==2:
                primos.append(numero) # adiciona o nº primo à lista de primos
print(f'Numero primos de 1 a {limite}: ', primos)
