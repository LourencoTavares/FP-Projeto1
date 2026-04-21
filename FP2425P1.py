"""
1) Verifica se o argumento fornecido é um tabuleito válido
2) Um tabuleiro é válido se: o número de linhas estiver entre 2 e 100, se todas as linhas tiverem o mesmo comprimeito (entre 2 e 100) e se cada elemento é um inteiro que pode valer 0, 1 ou -1.
3) Faz a verificação e devolde True se for um tabuleiro segundo as validações feitas, e False caso contrário
"""
def eh_tabuleiro(arg):
    if not isinstance(arg, tuple) or not (2 <= len(arg) <= 100):
        return False
    
    for linha in arg:
        if not isinstance(linha, tuple) or len(linha) != len(arg[0]) or not (2 <= len(linha) <= 100):     # Verifica se cada linha é um tuplo, se tem o mesmo comprimento da primeira linha e se o comprimento está entre 2 e 100
            return False
        for elemento in linha:
            if type(elemento) != int or (elemento != 0 and elemento != 1 and elemento != -1):               #Verifica se cada elemento é um inteiro e se é igual a 0, 1 ou -1
                return False
    return True

"""
1) Verifica se o argumento fornecido é uma posição válida (será um inteiro que estará contido entre 1 e 10000 (inclusive))
"""
def eh_posicao(arg):
    if type(arg) != int or arg <= 0 or arg >= 10001:
        return False
    return True

"""
1) Calcula o número de linhas e colunas de uma tabela reprensetada por uma lista de listas
2) Devolve um tuplo contendo o número de linhas e o número de colunas do tabuleiro
"""
def obtem_dimensao(tab):
    soma_linhas = 0
    soma_colunas = 0
    for m in range(len(tab)):               #Calcula o número de linhas segundo a tabela
        soma_linhas += 1
    for n in range(len(tab[0])):            #Calula o número de colunas segundo as linhas
        soma_colunas += 1
    return (soma_linhas, soma_colunas)

"""
1) Obtem o valor de uma posição específica numa tabela
"""
def obtem_valor(tab, pos):
    posicao_atual = 1                         #Inicializa a posição atual como 1
    for lista in tab:
        for elemento in lista:
            if pos == posicao_atual:          #Verifica se a posição atual é igual à posição desejada 
                return elemento
            posicao_atual += 1                #Incrementa a posição atual
    
"""
1) Obtém um tuplo com os índices de uma determinada coluna de uma tabela
"""
def obtem_coluna(tab, pos):
    novo_tuplo = ()
    posicao_atual = 1
    for linha in range(len(tab)):
        for coluna in range(len(tab[linha])):
            if coluna == (pos - 1) % len(tab[linha]):         #Verifica se a coluna atual é a desejada
                novo_tuplo += (posicao_atual,)
            posicao_atual += 1
    return novo_tuplo

"""
Obtém um tuplo de posições correspondentes a uma toda linha em que se encontra a posição atual
"""
def obtem_linha(tab, pos):
    novo_tuplo = ()
    posicao_atual = 1
    for linha in tab:
        if pos >= posicao_atual and pos < posicao_atual + len(linha):             #Verifica se a posição fornecida está dentro da linha atual
            for posicao in range(len(linha)):
                novo_tuplo += (posicao_atual+posicao,)                        #Adiciona à tupla todas as posições da linha atual
        posicao_atual += len(linha)
    return novo_tuplo
    
"""
1) Obtém as diagonais de uma posiçao em um tabuleiro
2) Esta função recebe um tabauleiro e uma posição e retorn as duas diagonais que passam por esaa posição (Diagonal e Antidiagonal)
3) Devolve um par de tuplos, onde o primeiro tuplo é a diagonal onde ordena de forma crescente as posições dos elementos da sua diagonal, e o segundo tuplo, a antidiagonal onde ordena de forma decrescente as posições dos elementos pertencentes às antidiagonais, incluindo a própria posição (pos)
"""
def obtem_diagonais(tab, pos):
    linhas, colunas = obtem_dimensao(tab)       #Obtem as dimensões do tableiro
    linha = (pos - 1) // colunas                    #Linha correspondente à posição indicada
    coluna = (pos - 1) % colunas                     #Coluna correspondente à posição indicada

    diagonal = []
    antidiagonal = []
    #Antidiagonal
    i, j = linha, coluna
    while i < linhas and j >= 0:                #Percorre a Antidiagonal (estabelece os seus limites)
        antidiagonal.append(i * colunas + j + 1)#Calcula a posição e adiciona-o a antiagonal
        i += 1
        j -= 1
    i, j = linha-1, coluna+1
    while i >= 0 and j < colunas:               #Percorre a Antidiagonal (estabelece os seus limites)
        antidiagonal.append(i * colunas + j + 1)#Calcula a posição e adiciona-o a antiagonal
        i -= 1
        j += 1

    #Diagonal 
    i, j = linha, coluna
    while i >= 0 and j >= 0:                    #Percorre a Diagonal (estabelece os seus limites)
        diagonal.append(i * colunas + j + 1)    #Calcula a posição e adiciona-o a diagonal
        i -= 1
        j -= 1
    i, j = linha+1, coluna+1
    while i < linhas and j < colunas:           #Percorre a Diagonal - (estabelece os seus limites)
        diagonal.append(i * colunas + j + 1)    #Calcula a posição e adiciona-o a diagonal
        i += 1
        j += 1


    return tuple(sorted(diagonal)), tuple(sorted(antidiagonal))[::-1]       #Devolve as diagonais em forma crescente e antidiagonais em forma decrescente, ambas num tuplo

"""
1) Obtem um tabuleiro de jogo (é representado como uma lista de inteiros) em formato str
2) Cada elemento do tabuleiro pode ter o valor 1 que é representado por "X", o que é representado por "+" e -1 que é representado por "0"
3) Cada linha é separada por um separador de colunas ("---") e cada linha do tabuleiro é separado por separados verticais ("|")
"""
def tabuleiro_para_str(tab):
    simbolos = {1: "X", 0: "+", -1: "O"}                  #Dicionário com os símbolos correspondentes
    resultado = ""
    for l in range(len(tab)):
        linha = tab[l]
        for coluna in range(len(linha)):
            resultado += simbolos[linha[coluna]]
            if coluna < len(linha)-1:                     #Verifica se ão é a última coluna da linha
                resultado += "---"                        #Adiciona um separador entre colunas
        if l < len(tab)-1:                                #Verifica se não é a última linha do tabuleiro
            resultado += "\n"
            for separador in range(len(linha)-1):
                resultado += "|   "                       #Adiciona um separador vertical entre colunas
            resultado += "|" + "\n"                         #Adiciona o último separador da linha e muda de linha
    return resultado

"""
1) Verifica se a posição fornecida é válida no tabuleiro (devolve True) e caso contrário, devolve False
2) Se não tiver de acordo com as caracteristicas apresentadas, faz o levantamento do erro
"""
def eh_posicao_valida(tab,pos):
    if not eh_tabuleiro(tab) or pos <= 0 or not isinstance(pos, int):
        raise ValueError("eh_posicao_valida: argumentos invalidos")
    else:
        posicao_atual = 1                                                 #Representa a primeira posição do tabuleiro
        for linha in tab:
            for elemento in linha:
                if posicao_atual == pos:                                  #Verifica se a posição atual é igual ao valor fornecido
                    return True                                         #Se a posição for encontrada, devolve True, caso contrário False
                posicao_atual += 1                                        #Incrementa para a próxima posição
    return False

"""
1) Verifica se uma posição no tabuleiro está livre e em caso afirmativo, devolve "True"
2) Caso os argumentos não estejam de acordo, levanta um erro (ValueError)
3) Caso contrário devolve "False"
"""
def eh_posicao_livre(tab, pos):
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    return obtem_valor(tab,pos) == 0

"""
1) Obtém todas as posições livres de um tabuleiro
2) Caso passe na verificação, irá criar um tuplo com todas as posições livres do tabuleiro ou as que admitem como valor o "0"
"""
def obtem_posicoes_livres(tab):
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    
    novo_tuplo = ()
    posicao_atual = 1
    for linha in tab:
        for elemento in linha:
            if elemento == 0:                         #Adiciona a posição ao tuplo se estiver livre
                novo_tuplo += (posicao_atual,)
            posicao_atual += 1
    return novo_tuplo

"""
1) Devolve um tuplo com as posições do tabuleiro ocupadas pelo jogador dito nos argumentos da função
2) Caso o tabuleiro não for válido, ou se o jogador escolher um número diferente de -1 e 1, faz o levantamento do erro (ValueError)
"""
def obtem_posicoes_jogador(tab, jog):
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in [-1, 1]:
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    
    novo_tuplo = ()
    posicao_atual = 1
    for linha in tab:
        for elemento in linha:
            if jog == 1 and elemento == 1:              #Verifica se o elemento corresponde ao jogador escolhido
                novo_tuplo += (posicao_atual,)
            elif jog == -1 and elemento == -1:          #Verifica se o elemento corresponde ao jogador escolhido
                novo_tuplo += (posicao_atual,)
            posicao_atual += 1
    return novo_tuplo


"""
1) Obtém as posições adjacentes válidas de uma posição do tabuleiro
2) Se não estiver de acordo com o pedido, levanta um ValueError
3) Cada lista do tabuleiro é representada por uma linha, onde cada lista da linha é representada por uma coluna
4) Adicina a uma lista cada umas das posições adjacentes
5) Devolve as posições adjacentes em ordem crescente
"""
def obtem_posicoes_adjacentes(tab,pos):
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    linhas = len(tab)
    colunas = len(tab[0])
    adjacentes = []
    linha = (pos - 1) // colunas
    coluna = (pos - 1) % colunas

    if linha-1 >= 0:                                          # Parte de Cima
        adjacentes.append((linha-1) * colunas + coluna + 1)
    
    if linha+1 < linhas:                                      # Parte de Baixo
        adjacentes.append((linha+1) * colunas + coluna + 1)
    
    if coluna-1 >= 0:                                         # Lado Esquerdo
        adjacentes.append(linha * colunas + (coluna-1) + 1)
    
    if coluna+1 < colunas:                                    # Lado Direito
        adjacentes.append(linha * colunas + (coluna+1) + 1)
    
    if linha-1 >= 0 and coluna-1 >= 0:                          # Diagonal Superior Esquerda
        adjacentes.append((linha-1) * colunas + (coluna-1) + 1)

    if linha-1 >= 0 and coluna+1 < colunas:                     # Diagonal Superior Direita
        adjacentes.append((linha-1) * colunas + (coluna+1) + 1)

    if linha+1 < linhas and coluna-1 >= 0:                      # Diagonal Interior Esquerda
        adjacentes.append((linha+1) * colunas + (coluna-1) + 1)   

    if linha+1 < linhas and coluna+1 < colunas:                 # Diagonal Inferior Direita
        adjacentes.append((linha+1) * colunas + (coluna+1) + 1) 

    return tuple(sorted(adjacentes))

"""
1) Calcula a distância de Chebyshev de uma posição ao centro do tabuleiro (Distância de Chebyshev - Maior vaor absoluto da diferença entre as coordenadas da linha e coluna)
"""
def ordena_posicoes_tabuleiro_aux(pos,tab):
    linhas, colunas = obtem_dimensao(tab)                                             #Número de linhas e de colunas do tabuleiro, respetivamente 
    posicao_central = (linhas // 2) * colunas + (colunas // 2) + 1                              #Cálculo da posição central do tabuleiro
    linha_central = (posicao_central - 1) // colunas
    coluna_central = (posicao_central - 1) % colunas
    linha_pos = (pos - 1) // colunas                                                      #Cálculo da linha e da coluna, respetivamente, à posição fornecida
    coluna_pos = (pos - 1) % colunas
    return max(abs(linha_central - linha_pos), abs(coluna_central - coluna_pos))        #Calcula a distância de Chebyshev entre a posição fornecida e o centro
"""
1) Ordena as posições de um tabuleiro pela distância ao centro do tabuleiro
2) Faz a verificação dos argumentos, vendo se estes são válidos. Se não forem, levanta o erro ("ValueError")
3) Recebe um tabuleiro e um tuplo, e devolve todas as posições ordenadas inicialmente pelas mais próximas ao centro, até as que se encontram mais longe
"""
def ordena_posicoes_tabuleiro(tab, tup):
    if not eh_tabuleiro(tab) or not isinstance(tup, tuple) or len(tup) == 0:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    for elementos in tup:
        if not eh_posicao(elementos) or elementos < 1:                                         #Se os elementos dentro do tuplo não forem uma posição, levanta o erro ("ValueError")
            raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
        
    posicoes_ordenadas = sorted(tup, key = lambda pos: (ordena_posicoes_tabuleiro_aux(pos,tab), pos))

    return tuple(posicoes_ordenadas)

"""
1) Marca uma posição no tabuleiro com o valor do jogador fornecido
2) Se algum dos argumentos não for válido, faz o levantamento do erro("ValueError")
"""
def marca_posicao(tab, pos, jog):
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_posicao_livre(tab, pos) or pos <= 0 or pos > (len(tab[0]) * len(tab)) or jog not in [-1, 1]:
        raise ValueError("marca_posicao: argumentos invalidos")
    
    novo_tuplo = ()
    posicao_atual = 1
    for linha in tab:
        nova_linha = ()
        for elemento in linha:
            if posicao_atual == pos:
                nova_linha += (jog,)                          #Marca a posição desejada com o valor do jogador
            else:
                nova_linha += (elemento,)                     #Mantém o valor original da posição
            posicao_atual += 1
        novo_tuplo += (nova_linha,)
    return novo_tuplo

"""
Verifica a quantidade de elementos consequtivos de um jogador numa determinada direção
"""
def verifica_k_linhas_aux(tab, pos, jog, l1, c1):
    linhas, colunas = obtem_dimensao(tab)                     #Número de linhas e colunas, respetivamente, num tabuleiro
    linha = (pos - 1) // colunas                                  #Determina a posição da linha e da coluna à posição dada (pos)
    coluna = (pos - 1) % colunas
    l, c = linha, coluna

    contador = 0
    while 0 <= l < linhas and 0 <= c < colunas and tab[l][c] == jog:  #Conta as peças consequitvas do jogador
        contador += 1
        l += l1
        c += c1
    return contador
"""
1) Verifica se um jogador tem k elementos consequtivos a partir de uma posição
2) Caso os argumentos não sejam válidos, faz o levantamento do erro ("ValueError)
"""
def verifica_k_linhas(tab, pos, jog, k):
    if not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or type(k) != int or k <= 0 or not eh_tabuleiro(tab) or jog not in [1, -1]:
        raise ValueError("verifica_k_linhas: argumentos invalidos")
    if eh_posicao_livre(tab,pos):                                                       #Verifica se a posição está livre
        return False
    
    direcoes = [(0, 1), (1, 0), (1, 1), (1, -1)]                                        #Direções: Horizontal, Vertical, Diagonais e Antidiagonais
    for linha_direcao, coluna_direcao in direcoes:
        if verifica_k_linhas_aux(tab, pos, jog, linha_direcao, coluna_direcao) + verifica_k_linhas_aux(tab, pos, jog, -linha_direcao, -coluna_direcao) - 1 >= k:     #O menos(-) inverte a direção ////// Soma os elementos numa direção e na direção oposta, subtrai 1 para evitar contar a posição inicial duas vezes
            return True
    return False

"""
1) Verifica se o jogo chegou ao fim, isto implica que não haja mais movimentos possiveis ou se um jogador já conseguiu k pedras consequtivas
2) Em caso afirmativo, devolve "True", caso contrário "False"
3) Caso os argumentos não sejam válidos, faz o levantamento do erro ("ValueError)
"""
def eh_fim_jogo(tab, k):
    # Verificar se os argumentos são válidos
    if not eh_tabuleiro(tab) or k <= 0 or not isinstance(k, int):
        raise ValueError("eh_fim_jogo: argumentos invalidos")
    
    contador = 1
    if obtem_posicoes_livres(tab) == ():                                                                      #Verifica se existem posições livres
        return True
    
    for pos in tab:                                                                                         #Verifica se há k consecutivos
        for i in pos:   
            if verifica_k_linhas(tab, contador, -1, k) or verifica_k_linhas(tab, contador, 1, k):           #Verifica se o jogador -1 ou 1 têm k pedras consequtivas
                return True
            contador += 1
    
    return False

"""
1) Pede ao jogador para escolher uma posição livre do tabuleiro
2) Caso os argumentos não sejam válidos, faz o levantamento do erro ("ValueError")
"""
def escolhe_posicao_manual(tab):
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")

    while True:
        posicao = input("Turno do jogador. Escolha uma posicao livre: ")
        if not posicao:                                                                                                 #Verifica se a entrada é vazia 
            continue
        if posicao.isdigit():                                                                                           #Verifica se a entrada é um número
            posicao = int(posicao)
        else: 
            continue
        if not eh_posicao(posicao) or not eh_posicao_valida(tab,posicao) or not eh_posicao_livre(tab,posicao):          #Verifica se a posição é valida e não está ocupada no tabuleiro
            continue
        return posicao
    
"""
1) Esta função recebe um tabuleiro, um identificador de jogador, um valor positivo k e uma estratégia ('facil', 'normal' ou 'dificil') e devolve a posição escolhida automaticamente de acordo com a estratégia selecionada. 
2) Se houver várias posições possíveis, escolhe a mais próxima da posição central do tabuleiro. 
3) Caso os argumentos não sejam válidos, faz o levantamento do erro ("ValueError")
"""
def escolhe_posicao_auto(tab, jog, k, lvl):
    if not eh_tabuleiro(tab) or jog not in [-1, 1] or not isinstance(k, int) or k <= 0 or lvl not in ["facil","normal","dificil"]:
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
    for dificuldade in lvl:
        if dificuldade not in lvl:
            raise ValueError("escolhe_posicao_auto: argumentos invalidos")
        
    livres_adjacentes = []
    if lvl=="facil":
        for p in obtem_posicoes_jogador(tab, jog):
            for pos in obtem_posicoes_adjacentes(tab, p):
                if eh_posicao_livre(tab, pos):                                      #Se houver posições adjacentes, escolhe a primeira posição livre do tabuleiro
                    livres_adjacentes.append(pos)
        if livres_adjacentes:                                                       #Se não houver posições adjacentes, escohe a primeira posição livre do tabuleiro 
            return ordena_posicoes_tabuleiro(tab, tuple(livres_adjacentes))[0]
        return ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab))[0]
    
"""
1) O jogo começa sempre com o jogador com pedras pretas a marcar uma posição livre no tabuleiro e termina quando um dos jogadores vence ou quando não há mais posições livres disponíveis. A função mostra o resultado do jogo, que pode ser "VITÓRIA", "DERROTA" ou "EMPATE.
2) Caso os argumentos não sejam válidos, faz o levantamento do erro ("ValueError")
"""
def jogo_mnk_aux(turno):
    pass
    
def jogo_mnk(cfg, jog, lvl):
    for i in cfg:
        if type(i)!=int:
            raise ValueError("jogo_mnk: argumentos invalidos")
    if jog not in [-1,1] or lvl not in ["facil","normal","dificil"]:
        raise ValueError("jogo_mnk: argumentos invalidos")
    
    tab=()
    for linha in range(cfg[0]):
        tab1=()
        for coluna in range(cfg[1]):
            tab1+=(0,)
        tab+=(tab1,)

    print("Bem-vindo ao JOGO MNK.")
    if jog==1:
        turno = 'X'
        print("O jogador joga com 'X'.")
        while not eh_fim_jogo(tab, cfg[2]):
            if turno == 'X':
                pos = escolhe_posicao_manual(tab)
                tab = marca_posicao(tab,pos,jog)
                print(tabuleiro_para_str(tab))
                turno = 'O'
            
            if turno == 'O':
                pos = escolhe_posicao_auto(tab,-jog,cfg[2],lvl)
                tab = marca_posicao(tab,pos,-jog)
                print("Turno do computador ("+str(lvl)+"):")
                print(tabuleiro_para_str(tab))
                turno = 'X'
        
    if jog == -1:
        turno = 'X'
        print("O jogador joga com 'O'.")
        while not eh_fim_jogo(tab, cfg[2]):
            if turno == 'X':
                pos = escolhe_posicao_manual(tab)
                tab = marca_posicao(tab,pos,jog)
                print(tabuleiro_para_str(tab))
                turno = 'O'
            
            if turno == 'O':
                pos = escolhe_posicao_auto(tab,-jog,cfg[2],lvl)
                tab = marca_posicao(tab,pos,-jog)
                print("Turno do computador ("+str(lvl)+"):")
                print(tabuleiro_para_str(tab))
                turno = 'X'

    for p in obtem_posicoes_jogador(tab, jog):
        if verifica_k_linhas(tab, p, jog, cfg[2]): # significa que ganhei
            print('VITORIA')
            print(jog)
            return jog

    for p in obtem_posicoes_jogador(tab, -jog):
        if verifica_k_linhas(tab, p, -jog, cfg[2]): # significa que o PC ganhou
            print('DERROTA')
            print(jog)
            return jog

    for p in obtem_posicoes_jogador(tab, jog):
        for p in obtem_posicoes_jogador(tab, -jog):
            if not verifica_k_linhas(tab, p, jog, cfg[2]) and not verifica_k_linhas(tab, p, -jog, cfg[2]): # significa que nenhum dos dois ganhou
                print('EMPATE')
                return 0
            
jogo_mnk((10,10,10), 1, 'facil')