# 6. Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input(' Digite a quantidade de metros: '))
print('Metros = {} \nCentimetros = {} \nMilimetros = {}' .format(metro, metro * 100, metro * 1000))