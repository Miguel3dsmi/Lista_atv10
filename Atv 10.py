'''10. (ExeFuncao10) Crie um programa de gerenciamento acadêmico que opere usando quatro funções:
I. criar_vetor_notas(quantidade): Recebe o tamanho desejado (inteiro), aloca na memória e retorna uma nova lista preenchida com zeros.
II. ler_notas(vetor_ref): Recebe o vetor alocado e substitui fisicamente os zeros pelas notas lidas. Não possui retorno.
III. calcular_media_turma(vetor): Recebe o vetor preenchido, calcula e retorna a média.
IV. exibir_relatorio(vetor, media_alvo): Recebe o vetor e a média e imprime o relatório de aprovação/reprovação.
No programa principal, orquestre o chamamento das funções em sequência para q o vetor de
notas seja criado, populado, que a média da turma seja gerada, e ao final, que imprima o
relatório.'''
def criar_vetor(tamanho):
    vetor = [0] * tamanho
    return vetor

def ler_notas(vetor):
    print(f"----- Lanaçamento de notas para {len(vetor)} alunos -----")
    for i in range(len(vetor)):
        vetor[i] = float(input(f"Digite a nota do aluno {i + 1}: "))
    print(f"Notas cadastradas com sucesso na memória.\n")

def media_turma(vetor):
    media = sum(vetor) / len(vetor)
    return media

def relatorio(vetor, media):
    alvo = media
    contador_p = 0
    contador_r = 0
    print(f"--------- Relatório da turma ---------")
    for i in range(len(vetor)):
        if vetor[i] >= alvo:
            situacao = "Acima/Na Média"
            contador_p += 1
        else:
            situacao = "Abaixo da Media"
            contador_r += 1
        print(f"Nota aluno {i + 1}: Nota {vetor[i]:.1f} ({situacao})")
    print("-" * 40)
    if contador_p > contador_r:
        situacao = "APROVADA"
    else:
        situacao = "REPROVADA"
    print(f"Media da turma: {alvo:.1f}\nStatus da Turma: {situacao}")

def main():
    Tamanho = int(input("Quantas notas o programa deverá armazenar: "))
    notas = criar_vetor(Tamanho)
    ler_notas(notas)

    media_t = media_turma(notas)
    relatorio(notas, media_t)

main()