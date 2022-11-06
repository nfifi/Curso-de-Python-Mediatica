dict = {
    'Porto':315,
    'Faro':250,
    'Coimbra':197,
    'Braga':360,
    'Evora':135
} 
print(f'{"Distancias de Lisboa":^30}')
print('='*30)
destino = 'Lisboa'
while True:
    while True:
        destino = input('Qual é a cidade de destino: ').strip().title()
        if destino != 'Lisboa':
            break
        else:
            print('Lisboa é o ponto de Origem!',end=' ')
    dist = dict.get(destino, '!')
    if dist != '!':
        print(f'De Lisboa a {destino} são {dist} km.')   
    else:
        add = input(f'A cidade destino {destino} não existe!Quer inserir a distância [S/N]: ').strip().upper()[0]
        if add in 'S':
            d = input('Insira a distância : ')
            dict.update({destino : d})
            print('-='*20)
            for k,v in dict.items():
                print(f'{k}  {v}')
            print('-='*20)
    cont = input('Pretende continuar [S/N]:').strip().upper()[0]
    print('-='*20)
    if cont == 'N':
        print('Fim do Programa!!!')
        break