'''5. (ExeFuncao05) Crie uma função chamada buscar_em_matriz(matriz, alvo) que receba uma
matriz e um número inteiro. A função deve percorrer a
matriz com laços aninhados e retornar um texto com a coordenada [i][j]
se encontrar o alvo (ex. Alvo encontrado na coordenada [1][1]), ou "Alvo não encontrado".
Crie uma segunda função só para imprimir a matriz. O nome dela deverá ser
imprime_matriz(matriz). Ela não deverá retornar nada, no entanto, deverá imprimir a matriz
informada ao ser chamada. No programa principal, declare uma matriz estática 3x3, imprima
a matriz chamando a função “imprime_matriz(matriz)”, e teste a função buscando
“buscar_em_matriz(matriz, alvo)” um valor existente e um inexistente.'''
import biblioteca_matriz

def visualizar_matriz(matriz):
    print(f"Matriz: {matriz}")

def buscar_matriz(matriz, alvo):
    situacao = False
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == alvo:
                situacao = True
                print(f"Alvo encontrado na coordenada [{i}][{j}]")
                break
            else:
                continue
    if situacao == False:
        print("Alvo não encontrado")

matriz = biblioteca_matriz.matriz_quadrada(10)
alvo = int(input("Informe qual número você está buscando dentro da matriz: "))
buscar_matriz(matriz, alvo)
visualizar_matriz(matriz)
print(matriz[4][9])