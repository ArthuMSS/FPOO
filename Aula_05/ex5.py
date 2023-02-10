# 5. Crie um programa que leia um número e mostre na tela seu dobro, triplo e raiz quadrada.

import math

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

print ('Dobro = {},\nTriplo = {},\nRaiz = {}' .format(dobro, triplo, raiz))