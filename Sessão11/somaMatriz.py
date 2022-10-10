matrizA = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
matrizB = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for linha in range(len(matrizA)):
    for coluna in range(len(matrizA)):
        print(f'[{matrizA[linha][coluna] + matrizB[linha][coluna]:^5}]',end='')
    print('\n')