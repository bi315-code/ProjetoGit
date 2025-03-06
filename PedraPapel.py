# Programa de cadastro de login
from time import sleep

print("Bem vindo ao jogo da forca!")
print("Vamos começar...")
sleep(1.5)

jogador1 = str(input("Digite o seu nome: "))
modo_jogo = int(input("Você quer jogar com outro jogador ou jogar sozinho(com a máquina)? [Digite 1 para jogar com outro jogador] ou [Digite 2 para jogar sozinho]: "))


escolha1 = input(str("Escolha apenas um, Pedra / Papel / Tesoura: "))

def jogador():
    while True:
        if escolha1 == 'Pedra' or escolha1 == 'pedra':
            print("Você escolheu pedra")
        else: 
            print("Variável inválida")
            print("Vez do próximo jogador")
            break
        

        if escolha1 == 'Papel' or  escolha1 == "papel":
            print("Você escolheu papel")
        else:
            print("Vez do próximo jogador")
            break

        if escolha1 == 'Tesoura' or  escolha1 == "tesoura":
            print("Você escolheu papel")
        else:
            print("Vez do próximo jogador")
            break
   
jogador()




