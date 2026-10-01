'''8. (ExeFuncao08) Crie um programa que aplique "funções chamando funções":
I. Função eh_par(n): retorna True/False.
II. Função eh_primo(n): testa se divisível apenas por 1 e ele mesmo, retornando True/False.
III. Função analisar_numero(n): recebe um número, chama as duas funções anteriores
internamente e imprime na tela o laudo (par/ímpar e primo/não primo).
No programa principal, crie um laço que chame analisar_numero(i) para os números de 1 a 10.'''
def eh_par(n):
    if n % 2 == 0:
        resulto = True
    else:
        resulto = False
    return resulto

def eh_primo(n):
    if n <= 1:
        return False
    elif n == 1:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
def analisar_numero(n):
    par = eh_par(n)
    primo = eh_primo(n)
    if par == True:
        if primo == True:
            print(f"{n} é par e primo.")
        else:
            print(f"{n} é par, porém não é primo.")
    else:
        if primo == True:
            print(f"{n} é impar e primo.")
        else:
            print(f"{n} é impar, porém não é primo.")
for i in range(1,11):
    numero = i
    analisar_numero(numero)

