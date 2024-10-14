import random
import string 

tabuleiro_player1 = [["-" for _ in range(10)] for _ in range(10)]
tabuleiro_player2 = [["-" for _ in range(10)] for _ in range(10)]

# Navios de uma posição
def navios_pequenos(tabuleiro_player): 
    navios_colocados = 0
    while navios_colocados <5:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if tabuleiro_player[x][y] == "-":
            tabuleiro_player[x][y] = 'N'
            navios_colocados += 1
        
            
# Navios de três posições
def navios_grandes(tabuleiro_player): 
    for i in range(3):
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            if y <= 7: # verifica se o navio cabe na coluna
                tabuleiro_player[x][y] = "G"
                tabuleiro_player[x][y+1] = "G"
                tabuleiro_player[x][y+2] = "G"
                break
            else: # move o navio para trás caso não caiba  
                tabuleiro_player[x][y] = "G"
                tabuleiro_player[x][y-1] = "G"
                tabuleiro_player[x][y-2] = "G"
                break
def imprimir_tabuleiro(tabuleiro):
    linhas = string.ascii_uppercase[:10]  # Letras de A a J para as linhas
    print(" ", end=" ")  # Espaçamento inicial para alinhar com as colunas
    for i in range(10):
        print(f"{i+1} ", end="")  # Imprime os números das linhas
    print()  # Quebra de linha após imprimir os números

    # Imprime as linhas do tabuleiro 
    for i, linha in enumerate(tabuleiro):
        print(f"{linhas[i]} ", end="")  # Imprime a letra da linha
        for x in linha:
            print(x, end=" ")  # Imprime cada célula da linha com espaço
        print()  # Quebra de linha após cada linha
