def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = calcular_media(nota1, nota2, nota3)
    print("A média das notas é: ", media)
except ValueError:
    print("Por favor, digite um número válido para as notas.")
    print("A média das notas é: ", media)
except ValueError:
    print("Por favor, digite um número válido para as notas.")