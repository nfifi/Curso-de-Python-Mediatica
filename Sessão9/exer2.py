cont = n = 1
cont_par = cont_impar = 0
while n!= 0:
    cont += 1
    n = int(input(f'Informe o {cont}º número: '))
    if n == 0:
        break
    elif n%2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print (f'Foram introduzidos {cont_par} números pares e {cont_impar} números impares!')