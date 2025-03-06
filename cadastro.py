 

#Calcular a porcentagem de vcs darem certo
class AmorDaMinhaVida():
    def __init__(self, pessoa1, pessoa2):
        self.pessoa1 = pessoa1
        # self.idade1 = idade1
        self.pessoa2 = pessoa2
        
    
    def dif_idade(self, idade1, idade2):
        self.idade1 = idade1
        self.idade2 = idade2
        self.diferenca = idade1 - idade2

print("Bem vindo ao Lovômetro")
AmorDaMinhaVida.pessoa1 = input("Digite o seu nome: ")
AmorDaMinhaVida.idade1 = int(input("Digite a sua idade: "))
AmorDaMinhaVida.idade1 = input("Digite o nome do seu amor: ")
AmorDaMinhaVida.idade2 = int(input("Digite a idade do seu amor"))
print(f"A diferença de idade entre vcs é de {AmorDaMinhaVida.diferenca}") #Ta errado 

print(AmorDaMinhaVida.dif_idade)