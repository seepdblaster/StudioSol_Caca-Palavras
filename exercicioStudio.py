# Programa feito por Bruno Rodrigues Paschoalino para vaga de estágio em suporte para Studio Sol
# Feito dia 25/08/2019
# Versão 1.0

# Achar se existe a palavra no caça palavras
# caso existir a palavra irá pegar a posição e a quantidade
# de ocorrências.
def get_Posicao( linhas, colunas, palavra, d1_colunas, d2_colunas ):

    posicao = set() #estrutura para salvar sem duplicações valor das posições das palavras dentro do caça palavras
    ocorrencia = 0 #variavel para verificar quantidade de ocorrências da palavra procurada

#loop para percorrer o vetor de palavras feitas pelas linhas da matriz
    for y, linha in enumerate(linhas):

        if palavra in linha:
            ocorrencia += 1
            comeco = linha.find(palavra)
            fim = linha.find(palavra) + len(palavra)

            for x in range(comeco, fim):
                posicao.add((x, y))

#loop para percorrer o vetor de palavras feitas pelas colunas da matriz
    for x, coluna in enumerate(colunas):

        if palavra in coluna:
            ocorrencia += 1
            comeco = coluna.find(palavra)
            fim = coluna.find(palavra) + len(palavra)

            for y in range(comeco, fim):
                posicao.add((x, y))

#loop para percorrer o vetor de palavras feitas pela diagonal direita
    for x, diagonalD1 in enumerate(d1_colunas):

        if palavra in diagonalD1:
            ocorrencia += 1
            comeco_palavra = diagonalD1.find(palavra)
            fim_palavra = diagonalD1.find(palavra) + len(palavra)

            for y in range(comeco_palavra, fim_palavra):
                posicao.add((x - y, y))

    controle = -16 #variavel de controle para correto posicionamento da posição da palavra dentro do caça palavras

#loop para percorrer o vetor de palavras feitas pela diagonal esquerda
    for x, diagonalD2 in enumerate(d2_colunas):
        controle += 2

        if palavra in diagonalD2:
            ocorrencia += 1
            comeco_palavra = diagonalD2.find(palavra)
            fim_palavra = diagonalD2.find(palavra) + len(palavra)

            for y in range(comeco_palavra, fim_palavra):
                posicao.add((y - x + controle, y))

    return posicao, ocorrencia

# Printar o resultado da quantidade de ocorrências e
# locais das palavras encontradas no caça palavras
def print_Resultado( linhas, colunas, palavra, d1_colunas, d2_colunas ):

    resultado = get_Posicao( linhas, colunas, palavra.upper(), d1_colunas, d2_colunas ) #pega o valor da tupla retornada pelo metodo get_Posicao
    posicao = resultado[0]
    ocorrencia = resultado[1]

#verificação de ocorrência de apenas uma letra para português correto
    if ocorrencia == 1:
        print(str(ocorrencia) + ' ocorrência para a palavra "' + palavra + '"')

        for y in range(len(linhas)):

            for x in range(len(linhas[y])):

                if (x, y) in posicao:
                    print(linhas[y][x] + " ", end="")
                else:
                    print('* ', end='')
            print('')

    elif ocorrencia > 1:
        print(str(ocorrencia) + ' ocorrências para a palavra "' + palavra + '"')

        for y in range(len(linhas)):

            for x in range(len(linhas[y])):

                if (x, y) in posicao:
                    print(linhas[y][x] + " ", end="")
                else:
                    print('* ', end='')
            print('')

    elif ocorrencia == 0: print('Nenhuma ocorrência para a palavra "'+palavra+ '"')

# Contém repetição para continuar pegando palavras para busca
# Contém transformações de colunas, linhas e diagonais para arrays com as palavras formadas
# por cada um
def getPalavra():

    matriz = \
        """Y C Y G W R P K H O A B U V H
S C I R F Z B M C P M Y C F P
U A F R X T W L O T A S M X C
E J R A G S A V H G L R X G F
K X Z T A P C V J Q M J Y M G
G C X Q E W S I A L A E O I V
I F Y F X V A L P A L H E T A
L E K O U U T I G U A N C O I
V H I H Z U A I F R D B A L U
A R Z H X C L C O G E E X V R
U N B S T M U S I C A T L A A
W R A U J A B I S S N O R I S
C M P L E N P A L C O A H B E
T M F O T Z M P T R E S J R L
F S I K U F P E Q T A M L O J"""

    matrizdiag1 = \
        """YCYGWRPKHOABUVH . . . . . . . . . . . . . .
        . SCIRFZBMCPMYCFP . . . . . . . . . . . . .
        . . UAFRXTWLOTASMXC . . . . . . . . . . . .
        . . . EJRAGSAVHGLRXGF . . . . . . . . . . .
        . . . . KXZTAPCVJQMJYMG . . . . . . . . . .
        . . . . . GCXQEWSIALAEOIV . . . . . . . . .
        . . . . . . IFYFXVALPALHETA . . . . . . . .
        . . . . . . . LEKOUUTIGUANCOI . . . . . . .
        . . . . . . . . VHIHZUAIFRDBALU . . . . . .
        . . . . . . . . . ARZHXCLCOGEEXVR . . . . .
        . . . . . . . . . . UNBSTMUSICATLAA . . . .
        . . . . . . . . . . . WRAUJABISSNORIS . . .
        . . . . . . . . . . . . CMPLENPALCOAHBE . .
        . . . . . . . . . . . . . TMFOTZMPTRESJRL .
        . . . . . . . . . . . . . . FSIKUFPEQTAMLOJ"""

    matrizdiag2 = \
        """. . . . . . . . . . . . . . YCYGWRPKHOABUVH
        . . . . . . . . . . . . . SCIRFZBMCPMYCFP .
        . . . . . . . . . . . . UAFRXTWLOTASMXC . .
        . . . . . . . . . . . EJRAGSAVHGLRXGF . . .
        . . . . . . . . . . KXZTAPCVJQMJYMG . . . .
        . . . . . . . . . GCXQEWSIALAEOIV . . . . .
        . . . . . . . . IFYFXVALPALHETA . . . . . .
        . . . . . . . LEKOUUTIGUANCOI . . . . . . .
        . . . . . . VHIHZUAIFRDBALU . . . . . . . .
        . . . . . ARZHXCLCOGEEXVR . . . . . . . . .
        . . . . UNBSTMUSICATLAA . . . . . . . . . .
        . . . WRAUJABISSNORIS . . . . . . . . . . .
        . . CMPLENPALCOAHBE . . . . . . . . . . . .
        . TMFOTZMPTRESJRL . . . . . . . . . . . . .
        FSIKUFPEQTAMLOJ . . . . . . . . . . . . . ."""

    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            print(matriz[x][y], end='')
    print("")

    print("Digite a palavra a ser buscada: ",end='')
    digitado = input()
    palavra = digitado.replace(' ', '').replace(".", "").replace(",", "")

    linhas = [linha.replace(' ', '') for linha in matriz.split('\n')]#transforma as linhas da "matriz" em palavras e salva em um array
    colunas = [''.join(coluna) for coluna in zip(*linhas)]#transforma as colunas em palavras e salva em um array

    d1_linhas = [d1linha.replace(' ', '') for d1linha in
                 matrizdiag1.split('\n')]
    d1_colunas = [''.join(d1coluna) for d1coluna in zip(*d1_linhas)]

    d2_linhas = [d2linha.replace(' ', '') for d2linha in
                 matrizdiag2.split('\n')]
    d2_colunas = [''.join(d2coluna) for d2coluna in zip(*d2_linhas)]

    #loop para continuar executando o programa
    while palavra != '0':
        if palavra != '':
            print_Resultado(linhas, colunas, palavra, d1_colunas, d2_colunas)
        else:
            print("Palavra inválida.")

        print("Digite a palavra a ser buscada: ", end='')
        digitado = input()
        palavra = digitado.replace(' ', '').replace(".", "").replace(",", "")

getPalavra()