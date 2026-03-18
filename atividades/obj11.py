def numeros():
    numeros = [5, 8, 10]
    print(numeros)
    numero = int(input("Digite um número: "))
    if numero in numeros:
        print("Soma total:", numero + sum(numeros))
    else:
        print("Resultado:", numero * 23)