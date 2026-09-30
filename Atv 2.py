'''2. (ExeFuncao02) Crie uma função chamada calcular_preco_final(valor, cupom) que receba
o total de uma compra e um texto (cupom). Se o cupom for "PYTHON10", aplique 10%
de desconto. Se for "PROG20", aplique 20%. Caso contrário, 0 (zero) desconto.
A função deve retornar o valor a ser pago. No programa principal, peça para o usuário digitar
o valor da compra e o cupom de desconto e imprima o resultado.'''

def calcular_preco_final(valor, cupom):
    if cupom == "PYTHON10":
        desconto = valor * 0.1
        print("Cupom aplicado")
    elif cupom == "PROG20":
        desconto = valor * 0.2
        print("Cupom aplicado")
    else:
        desconto = 0
        print("Cupom inválido")
    valor_final = valor - desconto
    return valor_final

valor = float(input("Digite o valor da compra: "))
cupom = input("Digite o cupom de desconto: ").upper()
valor_final = calcular_preco_final(valor, cupom)

print(f"Valor final: R${valor_final:.2f}")