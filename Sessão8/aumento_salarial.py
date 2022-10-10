print('*'*6,end=' ')
print('Cálculo do novo salario',end=' ')
print('*'*6)

salario = float(input('Digite o salário atual: '))
if salario < 500:
    ajuste = salario*1.15
elif salario < 1000:
    ajuste = salario*1.10
else:
    ajuste = salario * 1.05
print(f'Salario com reajuste = {ajuste:.2f}')