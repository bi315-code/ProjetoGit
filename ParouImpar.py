#Jogo do ímpar ou par
from random import randint
v = 0

while True:
        num = int(input("Digite um número: "))
        comp = randint(0,10)
        total = num + comp
        tipo = ''
        while tipo not in 'PI':
            tipo = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
        print(f"Valor que vc jogou foi {num} e o valor do computador foi {comp}. Total de {total} ", end = '')
        print("Então o número é Par" if total % 2 == 0
                    else "Então o número é Ímpar" )
        if tipo == 'P':
            if (total % 2) == 0:
                print("Você venceu!")
                v += 1
            else:
                print("Você perdeu!")
                break
        elif tipo == 'I':
            if (total % 2) == 1:
                print("Você venceu!")
                v += 1
            else:
                print("Você perdeu!")
                break
        print("Vamos jogar novamente...")
