import random

def jogar():

    print("\n\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")
    continuar = "S"
    
    while continuar == "S" or continuar == "s":
        numero_secreto = random.randrange(1,101)
        total_de_tentativas = 0
        pontos = 1000
        rodada = 1
        nivel = 0
        
        print("\nQual nível de dificuldade?")
        while nivel <= 0 or nivel >= 4:
            print("(1) Fácil - (2) Médio - (3) Difícil\n")
            nivel = int(input("Defina o nível de dificuldade: "))
            if(nivel <= 0 or nivel >= 4):
               print("\nOpção inválida selecione novamente!")

        if(nivel == 1):
            total_de_tentativas = 20
            conquista = "No fácil até minha vó!"
        elif(nivel == 2):
            total_de_tentativas = 10
            conquista = "Parece até o doutor estranho."
        else:
            total_de_tentativas = 5
            conquista = "Simplesmente Akinator!"
            
        pontos_perdidos = int(pontos/total_de_tentativas)
        print (numero_secreto)
        while rodada <= total_de_tentativas:
            print("\n------------------------------------------------------------\n")
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))

            chute_str = input("Digite um número entre 1 e 100: ")
            print("Você digitou o número {}!".format(chute_str))
            chute = int(chute_str)

            if(chute < 1 or chute > 100):
                print("VOCÊ DEVE DIGITAR UM NÚMERO ENTRE 1 E 100!")
                continue
            
            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                pontos_finais = pontos - pontos_perdidos * (rodada-1)
                print("\n------------------------------------------------------------\n")
                print("VOCÊ ACERTOU\nPontos: {} de {}!".format(pontos_finais, pontos))
                if pontos_finais == pontos:
                    print("\n* VITÓRIA PERFEITA *")
                print ("\nConquista desbloqueada: {}".format(conquista))
                break
            else:
                print ("\n-{} pontos".format(pontos_perdidos))
                if(maior):
                    print("Você errou! O seu chute foi maior do que o número secreto.")
                elif(menor):
                    print("Você errou! O seu chute foi menor do que o número secreto.")
            rodada += 1
            
        if acertou is False:
            print("\n------------------------------------------------------------\n")
            print("GAME OVER!")
            print("\n------------------------------------------------------------\n")
        continuar = input("\nVocê deseja continuar? (S/N)\n")
    print("\n------------------------------------------------------------\n")
    print("FIM DE JOGO...")

if(__name__ == "__main__"):
    jogar()
