import random
import string 
import time

tabuleiro_player1 = [["-" for _ in range(10)] for _ in range(10)]
tabuleiro_player2 = [["-" for _ in range(10)] for _ in range(10)]

def ataque(player, oponente):
    print(f"Sua vez {player}, faça sua jogada! \n")
    jogada_linha = input("Digite a Linha desejada: ").upper()
    while jogada_linha not in string.ascii_uppercase[:10]:
        print("\nLinha invalida! Digite uma letra de A a J.")
        jogada_linha = input("Digite a Linha desejada: ").upper()

    jogada_linha = string.ascii_uppercase.index(jogada_linha)  # Converte a letra para o índice (0 a 9)
    
    jogada_coluna = int(input("Digite a coluna desejada: ")) - 1
    while jogada_coluna < 0 or jogada_coluna > 9:
        print("\nColuna inválida! Digite um número entre 1 e 10.")
        jogada_coluna = int(input("Digite a coluna desejada (1-10): ")) - 1

    time.sleep(1)  # Pausa antes de revelar o resultado do ataque
    if oponente[jogada_linha][jogada_coluna] == "N" or oponente[jogada_linha][jogada_coluna] == "G":
        print("Navio oponente acertado!")
        print("""
                _ ._  _ , _ ._     
                (_ ' ( `  )_  .__)   
            ( (  (   )   `)  ) _) 
            (__ (_  (_ . _) _) ,__)
                `~~`| ' . /`~~`     
                    ;   ;          
                    |   |          
          _________|_ __ |_________
        """)
        oponente[jogada_linha][jogada_coluna] = "X"
    else: 
        print("\nAcerto na água!")
        oponente[jogada_linha][jogada_coluna] = "O"
    time.sleep(1)  # Pausa antes de continuar para o próximo jogador


# Navios de uma posição
def navios_pequenos(tabuleiro_player): 
    navios_colocados = 0
    while navios_colocados < 5:
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
            if y <= 7:  # verifica se o navio cabe na coluna
                tabuleiro_player[x][y] = "G"
                tabuleiro_player[x][y+1] = "G"
                tabuleiro_player[x][y+2] = "G"
                break
            else:  # move o navio para trás caso não caiba  
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
    time.sleep(2)  # Pausa para o jogador visualizar o tabuleiro

# Adiciona os navios ao tabuleiro
navios_grandes(tabuleiro_player1)
navios_pequenos(tabuleiro_player1)
navios_grandes(tabuleiro_player2)
navios_pequenos(tabuleiro_player2)

# Loop de ataque entre os jogadores
while True:
    print("   Tabuleiro Player 2")
    imprimir_tabuleiro(tabuleiro_player2)

    ataque("Player 1", tabuleiro_player2)  # Player 1 ataca o tabuleiro do Player 2
    imprimir_tabuleiro(tabuleiro_player2)

    print("   Tabuleiro Player 1")
    imprimir_tabuleiro(tabuleiro_player1)

    ataque("Player 2", tabuleiro_player1)  # Player 2 ataca o tabuleiro do Player 1
    imprimir_tabuleiro(tabuleiro_player1)

# print("""
        ##########################          
        ##########################          
   #####################################    
 #########################################  
####      ######################       #### 
###       ######################        ### 
##        ######################        ### 
###     ##########################      ### 
###    ############################    #### 
 ###   ### #################### ###    ###  
 ####   ### ################## ####  ####   
   ####  ######################### #####    
    ######## ################ #########     
      ######  ##############   ######       
               ############                 
                 ########                   
                   ####                     
                   ####                     
                   ####                     
                   ####                     
               ############                 
            ##################              
            ##################              
            ###            ###              
            ###            ###              
            ###            ###              
            ##################              
            ##################              
          ######################            
         ########################           
      """)
