#questão 1
print("Hello, World!")


#questão 2
def ler_idade(idade):
    idade = int(input("Digite sua idade: "))
    print("Sua idade é:", idade)

    if idade >= 16:
        print("Pode votar!")
    else:
        print("Ainda não pode votar.")

ler_idade()

#questão 3
def soma_itens_mercado():
    total = 0
    while True:
        numero = int(input("Soma de itens do mercado (0 para sair): "))
        if numero == 0:
            break
        total += numero
    print("Total da compra:", total)
    total_final = float(total)
    print("Total final da compra: R$", total_final)

#questão 4
def calcular_peso():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = peso / (altura ** 2)
        print("Seu IMC é:", imc)
        if imc < 24.9:
            print("Você está parecendo um graveto.")
        elif 24.9 <= imc < 29.9:
            print("pessoa normal.")
        elif 29.9 <= imc < 35:
            print("Obesidade morbida, com risco.")
        else:
            print("Você está obeso.")
    except ValueError:
        print("Entrada inválida. Digite um número para o peso e altura.")

calcular_peso()

#questão 5
lista = ["marcos", "joão", "maria", "pedro", "ana"]
for nome in lista:
    print(nome)
quantidade = len(lista)
print("Quantidade de nomes na lista:", quantidade)
if quantidade % 2 == 0:
    print("A quantidade de pessoas é par.")
else:
    print("A quantidade de pessoas é ímpar.")

#questão 6
lista_temperaturas_semana_diaria = [28.5, 30.2, 27.8, 29.1, 31.0, 26.4, 28.9]
for i in range(7):
    temperatura = float(input("Digite a temperatura do dia {}: ".format(i + 1)))
    lista_temperaturas_semana_diaria.append(temperatura)
media_temperaturas = sum(lista_temperaturas_semana_diaria) / len(lista_temperaturas_semana_diaria)
print("A média das temperaturas da semana é:", media_temperaturas)

#questão 7
lista_vendas = [100.0, 150.0, 200.0, 250.0, 300.0]
total_vendas = sum(lista_vendas)
print("Total de vendas:", total_vendas)
soma = 0
for i in range(len(lista_vendas)):
    soma += lista_vendas[i]
print("Total de vendas:", soma)
print("Total de vendas:", total_vendas)

#questão 8
loja = {
    "nome": "Loja de Roupas",
    "localizacao": "Shopping Center",
    "vendas": [1000.0, 1500.0, 2000.0]
}
valor = float(input("Digite o valor da compra: R$ "))
if valor > 500:
    desconto = valor * 0.20
elif 200 <= valor <= 500:
    desconto = valor * 0.10
else:
    desconto = 0
valor_final = valor - desconto
print(f"Valor final com desconto: R$ {valor_final:.2f}")

#questão 9
contar_media_notas = [3,5,8,10,9,2,4]
media = sum(contar_media_notas) / len(contar_media_notas)
print("A média das notas é:", media)
if media >= 7:
    print("Aprovado!")
elif media < 7:
    print("Reprovado.")
    notas_acima_de_7 = [nota for nota in contar_media_notas if nota > 7]
    print("Quantidade de notas acima de 7:", len(notas_acima_de_7))
    for nota in contar_media_notas:
        if nota > media:
            print(f"Nota {nota} está acima da média.")


#questão 10
palavra="análise de texto para rede social"
contar_vogais = 0
for letra in palavra:
    if letra.lower() in "aeiou":
        contar_vogais += 1
print("Quantidade de vogais na frase:", contar_vogais)


#questão 11
lista = ["10","11","12","13","14"]
lista.sort()
print(lista)

#questão 12
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
print("Usuário:", usuario)
print("Senha:", senha)  
if usuario == "admin" and senha == "1234":
    print("Acesso concedido.")
else:
    print("Acesso negado.")
    print("Usuário ou senha incorretos.")
    
if usuario: 
    print("usar calculadora")
    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        soma += numero
    print("A soma dos números digitados é:", soma)
    subtracao = 0
    while True:
        numero = int(input("Digite um número para subtrair (0 para sair): "))
        if numero == 0:
            break
        subtracao -= numero
    print("O resultado da subtração é:", subtracao)
    multiplicacao = 1
    while True:
        numero = int(input("Digite um número para multiplicar (0 para sair): "))
        if numero == 0:
            break
        multiplicacao *= numero
    print("O resultado da multiplicação é:", multiplicacao)
    divisao = 1
    while True:
        numero = int(input("Digite um número para dividir (0 para sair): "))
        if numero == 0:
            break
        divisao /= numero
    print("O resultado da divisão é:", divisao)
    