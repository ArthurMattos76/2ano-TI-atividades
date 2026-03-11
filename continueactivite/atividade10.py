numero = int(input("Digite um número inteiro para ver sua tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")