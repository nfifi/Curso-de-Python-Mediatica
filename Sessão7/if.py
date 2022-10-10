nota = float(input('Informe a nota do teste: '))
while nota < 0 or nota > 100:
    nota = float(input('Informe a nota do teste: '))

if nota <  50:
    print('Insuficiente!')
elif nota <= 70:
    print('Suficiente!')
elif nota <= 90:
    print('Bom!')
else:
    print('Muito Bom!')