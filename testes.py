import random
# Rever esse código - não está puxando a condição que vai validar se é ímpar ou par
class Jogo: 
    def __init__(self, jogador1, jogador2, valor1, valor2, impar_par1, impar_par2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.valor1 = valor1
        self.valor2 = valor2
        self.impar_par1 = impar_par1
        self.impar_par2 = impar_par2
    
    def soma(self, valor1, valor2):
        return valor1 + valor2

    def verif_impar_par(self, valor):
        if valor % 2 == 0:
            if self.impar_par1 == 1:
                print(f"O vencedor foi: {self.jogador1}, com {valor}")
            else:
                print(f"O vencedor foi: {self.jogador2}, com {valor}")
            
        else:
            if self.impar_par1 == 2:
              print(f"O vencedor foi: {self.jogador1}, com {valor}")
            else:
              print(f"O vencedor foi: {self.jogador2}, com {valor}")


class Maquina:
   
  def __init__(self, nome_jogador, impar_par_jogador1, num_dedo):
    self.valor
    self.num
    self.impar_par_jogador1 = impar_par_jogador1
    self.nome_jogador = nome_jogador
    self.num_dedo = num_dedo
    
  def gera_maquina(self):
    if self.impar_par_jogador1 == 1:
        self.valor = 2
    else:
        self.valor = 1

        self.num_dedo = random.randint(1,10)
  
  def soma(self):
    soma = self.num + self.valor
    return soma
  
  def verif_impar_par(self, valor):
        if valor % 2 == 0:
            if self.impar_par_jogador1 == 1:
                print(f"O vencedor foi: {self.nome_jogador}, com {valor}")
            else:
                print(f"O vencedor foi: Maquina, com {valor}")
            
        else:
            if self.impar_par1 == 2:
              print(f"O vencedor foi: {self.nome_jogador}, com {valor}")
            else:
              print(f"O vencedor foi: Maquina, com {valor}")







# principal
print("Bem-vindo ao jogo ímpar-par. Vamos começar...") 
oponente = int(input("Contra quem vc deseja jogar?[1- Outro jogador, 2- Computador]: "))

def escolha(oponente):
  if oponente == 1:
    nome1 = input("Digite o seu nome: ")
    tipo1 = int(input("Escolha ímpar ou par [1- ímpar, 2- par]: "))
    num1 = int(input("Escolha um número: "))

    nome2 = input("Digite o seu nome: ")  
    tipo2 = int(input("Escolha ímpar ou par [1- ímpar, 2- par]: "))
    num2 = int(input("Escolha um número: "))

    jogo = Jogo(nome1, nome2, num1, num2, tipo1, tipo2)
    jogo_soma = jogo.soma(jogo.valor1, jogo.valor2)
    jogo.verif_impar_par(jogo_soma)

  elif oponente == 2:
      print("Vc escolheu jogar contra o computador")

      nome1 = input("Digite o seu nome: ")
      tipo1 = int(input("Escolha ímpar ou par [1- ímpar, 2- par]: "))
      num1 = int(input("Escolha um número: "))
    
      maquina = Maquina(tipo1)
      maquina.gera_maquina()
      jogo_soma = maquina.soma(num1, maquina.num_dedo)
      maquina.verif_impar_par(jogo_soma)

  else:
      print("Valor inválido, tente novamente")
    
       
  
       

escolha(oponente)





# nome1 = input("Digite o seu nome: ")
# # jogador1 = Jogador(nome1, num, 1)
# oponente = int(input("Contra quem vc deseja jogar?[1- Outro jogador, 2- Computador]: "))
#     if oponente == 1:
#        print("Vc escolheu jogar contra outro jogador")
#        nome2 = input("Informe o nome do oponente: ")
       
#     elif oponente == 2:
#        print("Vc escolheu jogar contra o computador")
#        nome2 = "Computador"
#     else:
#        print("Valor inválido, tente novamente")


# nome2 = 


#1- escolher impar ou par (jogador 1 e dps jogador 2)
#2-jogador 1 = um num > jogador 2 = outro num