#sem função
print("Phyton é facil")
print("Phyton é facil")
print("Phyton é facil")

# com função
def imprime_mensagem():
    print("Phyton é facil")

imprime_mensagem()
imprime_mensagem()	

#Função com parâmetro
def saudar(nome):
    print(f"olá, {nome}!")

saudar("Ana")
saudar("Bruno")

def exibirMensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

    exibirMensagem("Ana", "bom dia")

#Parâmetros nomeados
    exibirMensagem(nome = "Bruno", mensagem = "boa noite")

#função que retorna media
def calcularMedia(nota1, nota2):
    return (nota1 + nota2) / 2

resultado = calcularMedia(8.0, 9.0)
print(f" média: {resultado}")

