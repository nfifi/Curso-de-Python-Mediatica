filmes = ('Black Mirror', 'Breaking Bad', 'Game Of Thrones', 'The Big Bang Theory')
while True:
    filme = input('Informe o filme que pretende verificar: ').title()
    if filme in filmes:
        print(f'{filme} está na tupla.')
    else:
        print(f'{filme} não está na tupla')