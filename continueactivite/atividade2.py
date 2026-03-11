distancia = float(input("Digite a distância em km: "))
kmporlitro = float(input("Digite o consumo de combustível em km/l: "))
gasolina = float(input("Digite o valor da gasolina por litro: "))
litros = distancia / kmporlitro
custo = litros * gasolina

print(f"Custo total da viagem: R$ {custo:.2f}")
print(f"Para percorrer {distancia}, você precisará de {litros:.2f} litros de gasolina.")    