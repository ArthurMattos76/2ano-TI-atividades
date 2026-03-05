# Embaralhando a lista 
import random

numeros = [52, 25, 92, 19, 51, 65]
print("Lista original: ", numeros)

# Ordenando a lista
numeros.sort()
print("Lista ordenada : ", numeros)

# Invertendo a lista
numeros.reverse()
print("Lista invertida: ", numeros)

# Ordenando em ordem decrescente
numeros.sort(reverse=True)
print("Lista ordenada (decrescente): ", numeros)

# Embaralhando a lista 
random.shuffle(numeros)
print("Lista embaralhada: ", numeros)   