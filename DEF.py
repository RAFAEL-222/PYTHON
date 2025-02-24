
#FUNCOES

#======================
from colorama import init, Fore, Back, Style
init()

#======================
def Load_TXT():
    D2 = []   #Lista que recebe txt
    D1 = {}   #Dicionario que recebe a lista
    try:
        with open('RD.txt', 'r') as DADOS:
            for i in DADOS:
                D2.append(i.rstrip().split(','))
        for i in D2:
            D1[i[0]]= [i[1]] , [i[2]] , [i[3]] , [i[4]]
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Será criado ao salvar.")
    return D1

#======================
def Save_TXT(Dict):        #Escrever no txt
    with open('RD.txt', 'w') as DADOS:
        for chave, dados in Dict.items():
            DADOS.write(f'{chave},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n')

#======================
def V_NUMERO(Num):
    try:
        n = int (Num)
        if n > 0:
            return n
        else:
            print("O número deve ser positivo.")
            return None   
    except ValueError:
        print('ENTRADA INVALIDA! Digite um número válido.')
        return None
    
#======================
def V_STRING(texto, campo):
    texto = texto.strip()
    if not texto:
        print(f"{campo} não pode estar vazio.")
        return None
    return texto

#======================
def V_ANO(ano):
    try:
        if 1950 <= ano:
            return ano
        else :
            print("Ano inválido. Digite um ano maior que 1950 .")
            return None
    except ValueError:
        print("ENTRADA INVALIDA! Digite um ano válido.")
        return None

#======================
def Pesq_NM(nome,Dict): #pesquisa aproxima do campo de nome
    Res_Pes = []    #cria uma lista vazio
    for chave, dados in Dict.items():
        if nome.lower() in dados[0].lower():
            Res_Pes.append([chave, dados])   #caso ache algo relacionado a letra,adiciona na lisat criada 
    return Res_Pes if Res_Pes else None

#======================
def CONT():  #continuar
    input(Fore.BLUE + Style.BRIGHT + 'pressione ENTER!' +Style.RESET_ALL+ '-para voltar ao menu.')

#======================
def conf_ACAO(texto): #confirmar 
    return input(f"{texto}Confirmar? (s/n): ").strip().lower() == 's'

#======================