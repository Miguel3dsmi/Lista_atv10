'''4. (ExeFuncao04) Crie uma função chamada inverter_vetor(vetor_ref) que receba uma lista
de inteiros. Esta função NÃO deve ter return, pois seu objetivo é
alterar a lista original (passada por referência) invertendo fisicamente
as posições de seus elementos (o 1o troca com o último, etc). No
programa principal, declare a lista de numeros = [10, 20, 30, 40, 50], imprima-o,
chame a função e imprima novamente (com os valores invertidos).'''
lista_numeros = []
numero = ""
def inverter_lista(lista_numeros):
    print(f"Lista invertida: {lista_numeros[::-1]}")

while numero != "sair":
    numero = input("Digite sua idade: ").lower().strip()
    if numero != "sair":
        numero = int(numero)
        lista_numeros.append(numero)

print(f"A lista de número: {lista_numeros}")
inverter_lista(lista_numeros)