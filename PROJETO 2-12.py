#UMC
#4/11/24
#Programador: Rafael da Silva Alves
#Software para armazenar jogos em forma de Dicionário-Lista, usando CRUD (TXT)


#===============
from colorama import init, Fore, Back, Style
init()
# print(Fore.RED + 'Este texto é vermelho' +Style.RESET_ALL)

#===============
import os   # biblioteca que apaga o console de modo automatico
import DEF   # Puxa as funcoes de outro arquivo PY

#===============
D1 = DEF.Load_TXT()

os.system("cls")

#===============

while True:
    os.system("cls")
    opt = input('''
                
========================================================           
|   ╔╗ ╦╔╗ ╦  ╦╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔═╗   ╦╔═╗╔═╗╔═╗╔═╗
|   ╠╩╗║╠╩╗║  ║║ ║ ║ ║╣ ║  ╠═╣   ║║║╣    ║║ ║║ ╦║ ║╚═╗
|   ╚═╝╩╚═╝╩═╝╩╚═╝ ╩ ╚═╝╚═╝╩ ╩  ═╩╝╚═╝  ╚╝╚═╝╚═╝╚═╝╚═╝
|                                                      
|   (1) Inclusão                                        |
|   (2) Alteração pelo o numero do Jogo                 | 
|   (3) Exclusao baseado no numero do Jogo              |      
|   (4) Mostra lista de Jogos                           |
|   (5) Pesquisa por Nome do Jogo                       |   
|   (6) Saída                                           |
=========================================================
==> ''')
    
    if opt not in ["1", "2", "3", "4", "5", "6"]:
        input(Fore.RED + Style.BRIGHT + 'ENTRADA INVALIDA!' +Style.RESET_ALL+ '-pressione ENTER para voltar ao menu.')
         
    
#============OPCOES==============             
#|   (1) Alterar Nome           |
#|   (2) Alteração Plataforma   |
#|   (3) Alteração Ano          |
#|   (4) Alteração Categoria    |
#|   (5) Saída                  |
#================================                                                      
#==> ''')    
#                if opt not in ["1", "2", "3", "4", "5"]:
#                    input(Fore.RED + 'ENTRADA INVALIDA!' +Style.RESET_ALL+ '-pressione ENTER para voltar ao menu.')
                
                