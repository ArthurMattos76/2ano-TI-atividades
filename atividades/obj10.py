def analisar_numero():
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Número positivo:", numero)
    elif numero < 0:
        print("Número negativo:", numero)
    else:
        print("Número é zero:", numero)
