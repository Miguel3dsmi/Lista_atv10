'''1. (ExeFuncao01) Crie uma função chamada validar_senha(senha) que receba uma string
como parâmetro. A função deve retornar True, se a senha for forte, ou False se for fraca,
baseada nestas regras: ter pelo menos 8 caracteres e NÃO ser “12345678” nem conter a
palavra “senha” (independente de maiúsculas/minúsculas). No programa principal, use um
laço de repetição while para pedir e validar uma senha continuamente até a função de
validação da senha retornar True.'''

def validar_senha(senha: str):
    forte = False
    if len(senha) > 8:
        if "12345678" not in senha or "senha" not in senha:
            forte = True
    return forte

while True:
    senha = input("Digite uma senha: ").lower().strip()
    condicao = validar_senha(senha)

    if condicao == True:
        print("Senha validada com sucesso!")
        break
    else:
        print("Senha invalida! Digite uma nova senha!")