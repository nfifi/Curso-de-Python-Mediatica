dict = {
    '1': 'um',
    '2': 'dois',
    '3': 'três',
    '4': 'quatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'sete',
    '8': 'oito',
    '9': 'nove',
    '0': 'zero',
}
num = input('Informe uma sequência de números: ')
for n in num:
    verif = dict.get(n,'!')
    print(verif.title(), end=' ')        

