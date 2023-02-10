# 4. Crie um programa que leia um número inteiro e exiba na tela seu antecessor e seu sucessor.

num = int (input('Digite um número: '))
ant = num - 1
suc = num + 1
print('O número é = {}, Antecessor = {}, Sucessor = {}' .format (num , ant, suc))