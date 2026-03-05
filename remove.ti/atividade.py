import random

lista = [91, 34, 67, 15, 82]
lista.sort()
print("Lista ordenada: ", lista)

lista.sort(reverse=True)
print("Lista ordenada (decrescente): ", lista)

numeros3 = [6,7,8,9,10] 
random.shuffle(numeros3)
print("Lista embaralhada: ", numeros3)

numeros4 = [23, 5, 17, 42, 11, 8]
numeros4.sort()
print("Terceira lista ordenada: ", numeros4)

numeros4.sort(reverse=True)
print("Terceira lista ordenada (decrescente): ", numeros4)

random.shuffle(numeros4)
print("Terceira lista embaralhada: ", numeros4)

numeros5 = [80, 20, 30, 20, 40, 90, 50]
print("lista:",numeros5)
print("Número de elementos da lista: ", len(numeros5))
print("Número de vezes que o número 20 aparece: ", numeros5.count(20))
print("Número de vezes que o número 100 aparece: ", numeros5.count(30))
print("O número 100 está na lista? ", 100 in numeros5)