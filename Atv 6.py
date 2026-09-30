'''6. (ExeFuncao06) Crie uma função chamada gerar_matriz_aleatoria(linhas, colunas) que
receba as dimensões da matriz. A função deve construir dinamicamente uma matriz
com esses tamanhos (inicializada com zeros) e, em seguida, usar
random.randint(1, 50) para preencher todas as coordenadas. A função
deve retornar a matriz pronta (isso é passagem de parâmetro por referência). No programa
principal, peça ao usuário as dimensões da matriz, chame a função e imprima a matriz em
grade. Usar a mesma função de impressão de matrizes do exercício 6 para imprimir a matriz.'''
import random
def gerar_matriza(linhas, colunas):
    matriz = [0] * linhas
    for i in range(linhas):
        matriz[i] = [0] * colunas
        for j in range(colunas):
            matriz[i][j] = random.randint(1, 50)
    return matriz

linha = int(input("Digite o número de linhas: "))
coluna = int(input("Digite o número de colunas: "))
matriz = gerar_matriza(linha, coluna)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"[{matriz[i][j]:2}]", end="")
    print()
