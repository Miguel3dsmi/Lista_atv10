def matriz_quadrada(quantidade,inicializador, salto = 1):
    matriz = []
    contador = inicializador
    for i in range(quantidade):
        linha = []
        for j in range(quantidade):
            linha.append(contador)
            contador += salto
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

def matriz_mix(matriz1, matriz2):
    matriz_mix = []
    vistos = set ()
    for matriz in (matriz1, matriz2):
        for linha in matriz:
            nova_linha = []
            for elemento in linha:
                if elemento not in vistos:
                    nova_linha.append(elemento)
                    vistos.add(elemento)
            if nova_linha:
                matriz_mix.append(nova_linha)
    return matriz_mix

def separador_matriz(matriz1, matriz2):
    separador = []
    vistos = set ()
    for matriz in (matriz1, matriz2):
        for linha in matriz:
            nova_linha = []
            for elemento in linha:
                if elemento in vistos:
                    nova_linha.append(elemento)
                else:
                    vistos.add(elemento)
            if nova_linha:
                separador.append(nova_linha)
    return separador