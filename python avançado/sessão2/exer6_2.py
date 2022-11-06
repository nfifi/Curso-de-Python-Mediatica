cinema = ('Sony Pictures', 'Walt Disney','Universal Pictures', 'Warner')
proc = input('Procura por: ').title()
try:
    i = cinema.index(proc)
except ValueError:
    print(f'{proc} não está na tupla!')
else:
    print(f'{proc} se encontra na {i}º posição da tupla!')