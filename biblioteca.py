def matriz_quadrada(valor):
    matriz = []
    contador = 1
    for i in range(valor):
        linha = []
        for j in range(valor):
            linha.append(contador)
            contador += 1
        matriz.append(linha)
    return matriz

def matriz4vetor(matriz,valor):
    vetor = [0] * valor * valor
    k = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vetor[k] = matriz[i][j]
            k += 1
    return vetor