'''3. (ExeFuncao03) Crie uma função chamada classificar_idades(vetor) que receba uma lista de
inteiros com as idades. A função deve analisar o vetor e retornar dois valores
simultaneamente: a quantidade de pessoas maiores de idade (>= 18) e a
quantidade de menores. No programa principal, declare um vetor fixo
com 10 idades à sua escolha e imprima o resultado devolvido pela função.'''
idade = ""
lista_idades = []
idades_verificadas = []
def classificar_idades (lista_idades):
    maior_idade = 0
    menor_idade = 0
    for i in range (len(lista_idades)):
        if lista_idades[i] >= 18:
            maior_idade += 1
        else:
            menor_idade += 1
    idades_verificadas.append(maior_idade)
    idades_verificadas.append(menor_idade)
    return idades_verificadas

while idade != "sair":
    idade = input("Digite sua idade: ").lower().strip()
    if idade != "sair":
        idade = int(idade)
        if idade >= 0 and idade <= 110:
            lista_idades.append(idade)
        else:
            continue
idades_verificadas = classificar_idades(lista_idades)
print(lista_idades)
print(f"Quantidade de pessoas maiores de idade: {idades_verificadas[0]}\nQuantidade de pessoas menores de idade: {idades_verificadas[1]}")