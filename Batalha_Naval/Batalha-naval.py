import random
import string 
import time
import os 

def criar_tabuleiro():
    return [["-" for _ in range(10)] for _ in range(10)]

def limpar_terminal():
    os.system("cls")

def ataque(player, navios, oponente):
    
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
        navios[jogada_linha][jogada_coluna] = "X"
        

    else: 
        print("\nAcerto na água!")
        navios[jogada_linha][jogada_coluna] = "O"
    time.sleep(1)  # Pausa antes de continuar para o próximo jogador


# Navios de uma posição
def adicionar_navios(tabuleiro_player,navios_pequenos = 5, navios_grandes= 3): 
    for i in range(navios_pequenos):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if tabuleiro_player[x][y] == "-":
            tabuleiro_player[x][y] = 'N'
            
        
    for i in range(navios_grandes):
        while True:
            x = random.randint(0,9)
            y = random.randint(0,7)
            if tabuleiro_player[x][y] == "-" and tabuleiro_player[x][y+1] == "-" and tabuleiro_player[x][y+2] == "-":
                tabuleiro_player[x][y] = "G"
                tabuleiro_player[x][y+1] = "G"
                tabuleiro_player[x][y+2] = "G"
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

tabuleiro_player1 = criar_tabuleiro()
tabuleiro_player2 = criar_tabuleiro()

ataque_player1 = criar_tabuleiro()
ataque_player2 = criar_tabuleiro()
adicionar_navios(tabuleiro_player1)
adicionar_navios(tabuleiro_player2)

while True:
    limpar_terminal()
    print("Tabuleiro de navios Player1")
    imprimir_tabuleiro(tabuleiro_player1)

    print("\nTabuleiro de ataque Player1")
    imprimir_tabuleiro(ataque_player1)

    ataque("player1",ataque_player1, tabuleiro_player2)
    
    limpar_terminal()
    time.sleep(2)
    print("\nTabuleiro de navios Player2")
    imprimir_tabuleiro(tabuleiro_player2)

    print("\nTabuleiro de ataque Player2")
    imprimir_tabuleiro(ataque_player2)
    
    ataque("player2",ataque_player2, tabuleiro_player1)
    
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
#      """)
