cinema = ('Sony Pictures', 'Walt Disney','Universal Pictures', 'Warner')
proc = input('Procura por: ').title()
if proc in cinema:
    print(f'{proc} se encontra na {cinema.index(proc)}º posição da tupla.')
else:
    print(f'{proc} não está na tupla!')