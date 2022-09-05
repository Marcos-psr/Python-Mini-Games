import random

def jogar():

    tela_de_inicio()
    resposta = "s"
    lista_repete = []
    while resposta == "s":
        escolha_tema = selecionar_temas()
        palavra_secreta = inicializa_palavra_secreta(escolha_tema)
        
        letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
        print(letras_acertadas)

        perdeu = False
        acertou = False
        erros = 0
        acertos = 0
        
        while(not perdeu and not acertou):

            chute = inicializa_chute()
            if (chute in palavra_secreta) and (chute not in lista_repete):
                lista_repete.append(chute)
                marca_chute(chute, letras_acertadas, palavra_secreta)
            else:
                erros += 1
                desenha_forca(erros)
                print("\n-"+"-"*50)
                print("\nOps, você errou! Faltam {} tentativas.".format(7-erros))

            acertou = "_" not in letras_acertadas
            perdeu = erros == 7
            print(letras_acertadas)
            
        if acertou:
            decreta_vitoria(erros)
                
        else:
            decreta_derrota(palavra_secreta)

        resposta = input("\nDeseja continuar jogando? (S/N)").lower()

    print("\nFINALIZANDO JOGO...")



def tela_de_inicio(): #imprime tela de abertura do jogo.
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")
    print("-"*50+"\n")
    print('''REGRAS

- Use - para espaçamento;
- Insira letra por letra da palavra;
- Não use acento nas letras.\n''')

def selecionar_temas(): #extensão que coloca novos temas e escolhas para a forca
        print('''\nTEMAS\n
1 - COMIDAS
2 - PROFISSÕES
3 - PAÍSES''')   
        tema = input("\nSelecione o tema da forca inserindo o número desejado: ")
        if tema == "1":
            escolha_tema = 'comidas.txt'
        elif tema == "2":
            escolha_tema = 'trabalhos.txt'
        elif tema == "3":
            escolha_tema = 'paises.txt'
        else:
            print("Número inserido inválido")
        return escolha_tema
    
def inicializa_palavra_secreta(escolha_tema): #sorteia palavra do arquivo txt
    arquivo = open(escolha_tema, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra): #mostra total de letras da palavra
    return ["_" for letra in palavra]
    

def inicializa_chute(): #inicializa e filtra o chute
    chute = input("\nQual letra? ")
    print("\n-"+"-"*50+"\n")
    chute = chute.strip().upper()
    return chute

def marca_chute(chute, letras_acertadas, palavra_secreta): #marca o chute nas letras da palavra
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index = index + 1

def decreta_vitoria(erros): 
    if erros == 0:
        print("Simplesmente o milior!")
    elif erros == 1:
        print("Quase genial!")
    elif erros == 2:
        print("Foi bem!")
    elif erros == 6:
        print("Passou raspando!")
    print("Parabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:      |) |    ")
    print("      '-|:      |-'     ")
    print("        \\::     /      ")
    print("         '::  .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
            

def decreta_derrota(palavra_secreta):
    print("Você foi enforcado!\n")
    print("A palavra era {}\n".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \  ")
    print(" |   XXXX     XXXX   |    ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXXX     XXXX   |      ")
    print(" |                   |      ")
    print(" \__       X       __/     ")
    print("   |\     XXX    /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

    
if(__name__ == "__main__"):
    jogar()

