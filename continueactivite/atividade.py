base = float(input("Digite o salário base: "))
bonus = float(input("Digite o valor do bônus: "))
desconto = float(input("Digite o valor do desconto: "))

salariobruto = base + bonus
salariofinal = salariobruto - desconto

print(f"Salário bruto: R$ {salariobruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Salário final: R$ {salariofinal:.2f}")
