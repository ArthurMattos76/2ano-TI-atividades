numeroaleatorio = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
import random

numero_secreto = random.choice(numeroaleatorio)
tentativas = 0

while True:
    tentativa = int(input("Adivinha o número entre 1 e 100: "))
    tentativas += 1
    if tentativa < numero_secreto:
        print("maior")
    elif tentativa > numero_secreto:
        print("menor")
    else:
        print(f"NICE CARA ACERTOU EM {tentativas} tentativas.")
        break

numeros_usuario = []
for i in range(8):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros_usuario.append(num)

repetidos = {}
for num in numeros_usuario:
    if numeros_usuario.count(num) > 1:
        repetidos[num] = numeros_usuario.count(num)

if repetidos:
    print("Números repetidos e suas quantidades:")
    for num, qtd in repetidos.items():
        print(f"{num} apareceu {qtd} vezes")
else:
    print("Nenhum número foi repetido.")