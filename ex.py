# 1) Crie um programa que determine se um ano é bissexto com base nas
# regras do calendário gregoriano.Seu programa deve receber um ano como entrada  e verificar se ele atende às seguintes condições:
# Um ano é bissexto se for divisível por 4, exceto se também for divisível por 100. Entretanto, se o ano for divisível por 100 e por 400, ele será bissexto.
# Com base nessas regras, implemente a lógica e exiba se o ano fornecido é bissexto ou não.
#%%
ano = int(input("Digite um ano:"))

if ano % 4 == 0:
    if ano % 100 == 0:
        print("Não é bissexto")
    else:
        print("É bissexto")

elif ano % 100 == 0 and ano % 400 == 0:
    print("O ano é bissexto")

else:
    print("O ano não é bissexto")

#%%
# 2) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
def conversao():
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    c = (5 / 9)  * (temp - 32)
    return print("A temperatura em fahrenheit é " ,temp , " e a sua conversão para celsius é ", c)

conversao()

#%%
''' 3) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.'''

ganho = float(input("Quanto vc ganha por hora trabalhada?: "))
hora = int(input("Quantas horas vc trabalha no mês?: "))
salario_bruto = ganho * hora 
imp_renda = (salario_bruto/100) * 11
inss_valor = (salario_bruto/100) * 8
sindicato_val = (salario_bruto/100) * 5
salario_liquido = salario_bruto - imp_renda - inss_valor - sindicato_val
# def imp_renda():
#     imp_renda = (salario_bruto/100) * 11
#     return print (imp_renda)

# def inss():
#     inss_valor = (salario_bruto/100) * 8
#     return print (inss_valor)

# def sindicato():
#     sindicato_val = (salario_bruto/100) * 5
#     return print (sindicato)
print("O salário bruto é: ", salario_bruto)
print("O valor do imposto de renda é: ",imp_renda)
print("O valor de inss é: ", inss_valor)
print("O valor pago ao sindicato é: ", sindicato_val)
print("O valor do salário líquido é: ", salario_liquido)


# %%
# 4) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
# por aluno e apresentar: A mensagem &quot;Aprovado&quot;, se a média alcançada for maior ou igual a
# sete; A mensagem &quot;Reprovado&quot;, se a média for menor do que sete; A mensagem &quot;Aprovado com 
# Distinção&quot;, se a média for igual a dez.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2

if media == 10:
    print("Aprovado com distinção")   
elif media >= 7:
    print("Aprovado")    
else:
    print("Reprovado")

#%% 
# 5)Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a 
# quantidade de números ímpares.
lista = []
contador_par = 0
contador_impar = 0

for i in range (10):
    num_int = int(input("Digite um número: "))
    lista.append(num_int)
    if num_int % 2:
        contador_par += 1
    else:
        contador_impar += 1

print(f'valores Digitados: {lista}')
print(f'quantidade números pares: {contador_par}')
print(f'quantidade números ímpares: {contador_impar}')

#%%

# 6)A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar
# a série até o n−ésimo termo.
def fibo(n):
    sequencia = [0,1]
    while len (sequencia) < n: #usado quando não tem um núm de repetições determinado
        prox_num = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_num)
    return sequencia

n = 15
resultado = fibo(n)
print(resultado)

#%%
# 7) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
#número de votos de cada candidato.
voto_cand_1 = 0
voto_cand_2 = 0
voto_cand_3 = 0 #variável contadora

eleitores = int(input("Digite o número de eleitores: "))

for i in range(eleitores):
    voto = input("Digite o numero (1/2/3) do candidato em quem o "f"eleitor {i + 1} quer votar: ")
    if voto == "1":
        voto_cand_1 += 1
    if voto == "2":
        voto_cand_2 += 1
    if voto == "3":
        voto_cand_3 += 1
    if voto == "4":
        break

print(
    "Votação encerrada"
    f"\nCandidato 1: {voto_cand_1} voto(s)"
    f"\nCandidato 2: {voto_cand_2} voto(s)"
    f"\nCandidato 3: {voto_cand_3} voto(s)"
)
# %%
#8. Jogo de Craps: Crie um programa que simule um jogo de Craps. O jogo funciona da seguinte maneira: O jogador lança dois dados, resultando em um valor entre 2 e 12.
#Na primeira jogada:  Se o resultado for 7 ou 11, o jogador vence automaticamente (chamado
#de &quot;natural&quot;).
# Se o resultado for 2, 3 ou 12, o jogador perde imediatamente (chamado
# de &quot;craps&quot;).
#  Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o &quot;Ponto&quot; do
# jogador.
# Caso um &quot;Ponto&quot; tenha sido estabelecido, o jogador continua lançando os
# dados:
#  Se tirar o mesmo valor do Ponto, ele vence.
#  Se tirar um 7 antes de repetir o Ponto, ele perde.
# Implemente a lógica para simular esse jogo e exiba o resultado de cada jogada.



#%%
# 9. Construa uma função que receba uma data no formato DD/MM/AAAA e
# devolva uma string no formato de “D de mesPorExtenso de AAAA”.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.