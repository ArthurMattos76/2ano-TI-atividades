contato = {
    "@camila": "CAMILA",
    "@joao": "JOAO",
    "@maria": "MARIA",
    "@pedro": "PEDRO",
}

#OBTER CHAVE
print("chaves:")
for insta in contato:
    print(insta)

#obter valor
    print("\n Valores:")
    for nome in contato.values():
        print(nome)

#obter pares
print("\n Pares:")
for insta, nome in contato.items():
    print(f"{insta} - - > {nome}")

contato = {
 "@camila": 1.70,
    "@joao": 1.80,
    "@maria": 1.55,
    "@pedro": 1.60

}

print("ordenando por chave:")
for insta in sorted(contato):
    print(f"{insta} - - > {contato[insta]:.2f}m")

    from _operator import itemgetter
    print("\n ordenando por valor (altura):")
    for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
        print(f"{insta} - - > {estatura:.2f}m")