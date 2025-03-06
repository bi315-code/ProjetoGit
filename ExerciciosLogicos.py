import random

class Pessoa:
  def __init__(self, pessoa, ponto, tipo):
    self.pessoa = pessoa
    self.ponto = ponto
    self.tipo = tipo

  def jogarDados(self):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"O valor do primeiro dado é: {dado1}")
    print(f"O valor do segundo dado é: {dado2}")
    print(f"{self.pessoa} com a soma dos dados vc tirou {soma}")
    return soma


  def jogar(self):
    somaDosDados = self.jogarDados()
    if somaDosDados == 7 or somaDosDados == 11:
      print(f"{self.pessoa} ganhou!")
    elif somaDosDados == 2 or somaDosDados == 3 or somaDosDados == 12:
      print(f"{self.pessoa} perdeu!")
    else:
      print(f"{self.pessoa} está na fase de ponto!")
      ponto = somaDosDados
      somaDosDados = self.jogarDados()
      while somaDosDados != ponto and somaDosDados != 7:
        somaDosDados = self.jogarDados()
      if somaDosDados == ponto:
        print(f"{self.pessoa} ganhou!")
      else:
        print(f"{self.pessoa} perdeu!")
#dentro da classe não precisa instanciar

#Criou fora da classe - instancia
def vamosJogar():
    print("Bem-vindo ao jogo de Craps!")
    print("Vamos começar!")
    nome1 = input("Informe seu nome: ")
    jogador1 = Pessoa(nome1, 0, 1)

    oponente = int(input("Contra quem vc deseja jogar?[1- Outro jogador, 2- Computador]: "))
    if oponente == 1:
       print("Vc escolheu jogar contra outro jogador")
       nome2 = input("Informe o nome do oponente: ")
       
    elif oponente == 2:
       print("Vc escolheu jogar contra o computador")
       nome2 = "Computador"
    else:
       print("Valor inválido, tente novamente")
       vamosJogar()

    jogador2 = Pessoa(nome2, 0, oponente)
      
    jogador1.jogar()  
    jogador2.jogar()
    if jogador1.ponto == jogador2.ponto:
        print("Empate!")
    elif jogador1.ponto > jogador2.ponto:
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")
    print("Jogo finalizado!")

vamosJogar()


# O usuário vai ter que escolher se quer jogar com a máquina ou com outro jogador