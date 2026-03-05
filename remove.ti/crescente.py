dados = [52, 25, 92, 19, 51, 65]
print(dados)

# numeros de elementos da lista
print("Número de elementos da lista: ", len(dados))

print("Número de vezes que o número 25 aparece: ", dados.count(25))

# conta ocorrências de um elemento específico
print("Número de vezes que o número 92 aparece: ", dados.count(92))

#index encontrar posiçao    
print("Posição do número 19: ", dados.index(19))

# in verificar se um elemento existe na lista
print("O número 52 está na lista? ", 52 in dados)
print("O número 100 está na lista? ", 100 in dados)

# acessando elementos da lista
print("Primeiro elemento: ", dados[0])
print("Último elemento: ", dados[-1])