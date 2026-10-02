'''9. (ExeFuncao09) Crie uma função calcular_interseccao(vetor_a, vetor_b) que receba dois
vetores. A função deve construir um terceiro vetor contendo os números
que existem em ambos, alocando a memória dinamicamente sem permitir
números duplicados. Retorne a lista de intersecção. Teste no principal
com vetores de 10 posições.'''
import biblioteca_matriz

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

matriz_a = biblioteca_matriz.matriz_quadrada(5, 1)
matriz_b = biblioteca_matriz.matriz_quadrada(5, 11)
matriz_c = separador_matriz(matriz_a,matriz_b)

print("Matriz A:")
for i in range (len(matriz_a)):
    for j in range (len(matriz_a[i])):
        print(f"[{matriz_a[i][j]:2}]", end="")
    print()

print("\nMatriz B:")
for i in range (len(matriz_b)):
    for j in range(len(matriz_b[i])):
        print(f"[{matriz_b[i][j]:2}]", end="")
    print()

print("\nMatriz C:")
for i in range (len(matriz_c)):
    for j in range(len(matriz_c[i])):
        print(f"[{matriz_c[i][j]:2}]", end="")
    print()