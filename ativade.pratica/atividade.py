paciente = {}

paciente['nome'] = input("Qual o seu nome:")
paciente['idade'] = int(input("Quantos anos sua idade:"))
paciente['peso'] = float(input("Digite seu peso:"))
paciente['altura'] = float(input("Digite sua altura:"))

imc = paciente["peso"] / (paciente["altura"] ** 2)

paciente["imc"] = imc

print("\n Dados)")
print("Nome:", paciente["nome"])
print("Idade:", paciente["idade"])
print("Peso:", paciente["peso"])
print("Altura:", paciente["altura"])
print("IMC:", round(paciente["imc"], 2))