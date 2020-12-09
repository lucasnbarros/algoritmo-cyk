def ler_gramatica():
    with open('gramatica.txt', 'r') as gramatica:
        regras = gramatica.read().splitlines()
        regras_terminais = []
        regras_variaveis = []

        for linha in regras:
            lado_esquerdo, lado_direito = linha.split(" => ")
            lado_direito = lado_direito.split(" | ")

            for letra in lado_direito:
                if(str.islower(letra)):
                    regras_terminais.append([lado_esquerdo, letra])
                else:
                    regras_variaveis.append([lado_esquerdo, letra])

        return regras_variaveis, regras_terminais


def cyk(reg_variaveis, reg_terminais, entrada):
    tamanho = len(entrada)

    variaveis_pos_0 = [var[0] for var in reg_variaveis]
    variaveis_pos_1 = [var[1] for var in reg_variaveis]

    tabela = [[set() for _ in range(tamanho-i)] for i in range(tamanho)]

    for i in range(tamanho):
        for regra in reg_terminais:
            if entrada[i] == regra[1]:
                tabela[0][i].add(regra[0])

    for i in range(1, tamanho):
        for j in range(tamanho - i):
            for k in range(i):
                conjunto_valores = set()

                if (tabela[k][j] == set() or tabela[i-k-1][j+k+1] == set()):
                    combinacoes = set()
                for primeira_letra in tabela[k][j]:
                    for segunda_letra in tabela[i-k-1][j+k+1]:
                        conjunto_valores.add(primeira_letra+segunda_letra)
                combinacoes = conjunto_valores

                for combinacao in combinacoes:
                    if combinacao in variaveis_pos_1:
                        tabela[i][j].add(
                            variaveis_pos_0[variaveis_pos_1.index(combinacao)])

    if ('S') in tabela[len(entrada)-1][0]:
        print(entrada, "pertence a gramática")
    else:
        print(entrada, "não pertence a gramática")
    return tabela


if __name__ == '__main__':
    r_variaveis, r_terminais = ler_gramatica()
    palavra = input("Escreva uma palavra:\n")
    teste = cyk(r_variaveis, r_terminais, palavra)
