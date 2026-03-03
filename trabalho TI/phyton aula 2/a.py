num1 = float(input("Informe o primeiro número real: "))
num2 = float(input("Informe o segundo número real: "))

soma = num1 + num2
produto = num1 * num2

print("Soma dos dois valores:", soma)
print("Produto entre eles:", produto)

num = int(input("Informe um número inteiro positivo: "))

if num % 2 == 0:
    resultado = num ** 2
    print("É par. Seu quadrado é:", resultado)
else:
    resultado = num ** 3
    print("É ímpar. Seu cubo é:", resultado)