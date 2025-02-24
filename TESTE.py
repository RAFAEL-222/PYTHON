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
=================OPCOES=====================
|  (1) Inclusão                            |
|  (2) Alteração pelo o numero do Jogo     |
|  (3) Exclusao baseado no numero do Jogo  |
|  (4) Mostra lista de Jogos               |
|  (5) Pesquisa por Nome do Jogo           |   
|  (6) Saída                               |
============================================
==> ''')
    
    if opt not in ["1", "2", "3", "4", "5", "6"]:
        input(Fore.RED + Style.BRIGHT + 'ENTRADA INVALIDA!' +Style.RESET_ALL+ '-pressione ENTER para voltar ao menu.')
         
    elif opt == "1":
        while True:
            SN = DEF.V_Numero(input("Entre com o número da sequência: "))
            if SN is None:
                print("Número inválido!")
                #continue  # Continua pedindo um número válido
            if SN in D1:
                print(Fore.YELLOW + Style.BRIGHT + f"Número {SN} já existe! Por favor, insira um número único." + Style.RESET_ALL)
                #continue  # Pede um novo número se já existir no dicionário
            else:
                # Se o número for único, continua com a inclusão do novo jogo
                Nm = input("Entre com o nome do Jogo: ")
                Plat = input("Entre com a plataforma do Jogo: ")
                Ano = DEF.V_Numero(input("Digite o ano de lançamento: "))
                Cat = input("Entre com a categoria do Jogo: ")
                
                Conf = input("Confirmar inclusão? (s/n): ").lower()
                if Conf == 's': 
                    D1[SN] = [Nm, Plat, Ano, Cat]
                    DEF.SAVE_TXT(D1)  # Salva no arquivo
                    print(Fore.GREEN + Style.BRIGHT + 'INCLUSÃO EFETUADA!' + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + 'Inclusão Cancelada!' + Style.RESET_ALL)
                    break
                
    
    elif opt == "2":
        SN = DEF.V_Numero(input("Entre com o numero da sequencia referente ao jogo a ser alterado: "))
        
        if SN not in D1:
            print('Numero NAO EXISTE')
            input('Pressione ENTER para voltar ao menu')
        else:
            os.system('cls')
            while True:
                print('Dados a serem ALTERADOS:')
                print(SN, D1[SN])
                opt = input('''
============OPCOES==============             
|   (1) Alterar Nome           |
|   (2) Alteração Plataforma   |
|   (3) Alteração Ano          |
|   (4) Alteração Categoria    |
|   (5) Saída                  |
================================                                                      
==> ''')    
                if opt not in ["1", "2", "3", "4", "5"]:
                    input(Fore.RED + 'ENTRADA INVALIDA!' +Style.RESET_ALL+ '-pressione ENTER para voltar ao menu.')
                
                elif opt == '1':
                    print(D1[SN][0])
                    Nm = input('Entre com o novo nome: ')
                    if Nm:  
                        Conf = input("Confirmar alteração? (s/n): ").lower()
                        if Conf != 's':
                            input("ALTERACAO cancelada - pressione ENTER para voltar ao menu ")
                        else:
                            D1[SN][0] = Nm   # Atualiza o nome
                            DEF.SAVE_TXT(D1)
                            input("ALTERACAO Efetuada - pressione ENTER para voltar ao menu ")
                    break       

                elif opt == '2':
                    print(D1[SN][1])
                    Plat = input("Entre com a nova Plataforma: ")
                    if Plat:
                        Conf = input("Confirmar alteração? (s/n): ").lower()
                        if Conf != 's':
                            input("ALTERACAO Cancelada - pressione ENTER para voltar ao menu ")
                        else:
                            D1[SN][1] = Plat   # Atualiza a Plataforma
                            DEF.SAVE_TXT(D1)
                            input("ALTERACAO Efetuada - pressione ENTER para voltar ao menu ")
                    break

                elif opt == '3':
                    print("Ano atual:", D1[SN][2])
                    while True:
                        Ano = DEF.V_Numero(input('Entre com o novo ano: '))
                        if Ano is not None:
                            Conf = input("Confirmar alteração? (s/n): ").lower()
                            if Conf != 's':
                                input("ALTERAÇÃO cancelada - pressione ENTER para voltar ao menu ")
                            else:
                                D1[SN][2] = Ano  # Atualiza o ano
                                DEF.SAVE_TXT(D1)
                                input("Alteração Efetuada - pressione ENTER para voltar ao menu ")
                            break
                    break

                elif opt == '4':
                    print("Categoria atual:", D1[SN][3]) 
                    Cat = input('Entre com a nova categoria: ')
                    if Cat:
                        Conf = input("Confirmar alteração? (s/n): ").lower()
                        if Conf != 's':
                            input("ALTERAÇÃO cancelada - pressione ENTER para voltar ao menu ")
                        else:
                            D1[SN][3] = Cat  # Atualiza a categoria
                            DEF.SAVE_TXT(D1)
                            input("Alteração Efetuada - pressione ENTER para voltar ao menu ")
                    break

                elif opt == "5":
                    input("Pressione ENTER para voltar ao menu anterior")
                    break

    elif opt == "3":
        DN = DEF.V_Numero(input("Entre com o número do jogo a ser DELETADO: "))
        if DN in D1:  # Verifica se o número existe no dicionário
            
            Conf = input(f"Tem certeza de que deseja deletar o jogo {D1[DN][0]}? (s/n): ").lower()
            if Conf == 's':
                del D1[DN]  # Deleta o jogo do dicionário
                DEF.SAVE_TXT(D1)
                input("Jogo deletado com sucesso - pressione ENTER para voltar ao menu ")
            else:
                input("Exclusão cancelada - pressione ENTER para voltar ao menu ")

        else:
            input("Número não encontrado - pressione ENTER para voltar ao menu ")
    
    elif opt == "4":
        for Numero, Dados in D1.items():
            print(Numero, Dados)
        input("Pressione ENTER para voltar ao MENU")

    elif opt == "5":
        Nm = input("Entre com o nome a ser pesquisado: ")
        resultados = DEF.pesq_nm(Nm, D1)
        if not resultados:
            print("Nome não encontrado.")
            input("Pressione ENTER para voltar ao menu ")
        else:
            for i in resultados:
                print(i)
            input("Pressione ENTER para voltar ao menu ")
    
    elif opt == "6":
        Repetir = input("CONFIRMAR ? (s/n): ").lower()
        if Repetir != 'n':
            break