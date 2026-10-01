'''7. (ExeFuncao07) Um sensor meteorológico grava a média temperatura diária durante 7 dias.
Crie duas funções:
I. obter_media(vetor): Retorna a média dos valores da semana.
II. contar_dias_quentes(vetor, limite): Conta e retorna quantos dias a temperatura
superou o parâmetro limite informado.
No programa principal, crie um vetor com 7 temperaturas float. Calcule a média
das temperaturas informadas usando a primeira função e passe o resultado como o 'limite' da
segunda função para descobrir quantos dias foram "acima da média".'''
temperaturas = []
contador = 0
def media(lista):
    media = sum(lista) / len(lista)
    return media

def acima_media (lista, limite):
    acima_media = []
    for i in range (len(lista)):
        if lista[i] > limite:
            acima_media.append(lista[i])
        else:
            continue
    return acima_media

for i in range (7):
    temp_hoje= float(input("Digite uma temperatura: "))
    temperaturas.append(temp_hoje)

media = media(temperaturas)
quente = acima_media(temperaturas, media)
for i in range (len(quente)):
    contador += 1

print("A lista de temperaturas: ")
for i in range (len(temperaturas)):
    print(f"[{temperaturas[i]:.2f}] ", end="")
print(f"\nTemperatura média: {media:.2f}ºC\nDias acima da média: {quente}\nQuantidade de dias acima da da média:{contador}")

