# 10. Crie um programa que leia/solicite para o usuário inserir quatro notas, realize a média e mostre na tela o resultado.

nt1 = float(input('Digite a primeira nota :')) 
nt2 = float(input('Digite a segunda nota :'))
nt3 = float(input('Digite a terceira nota :'))
nt4 = float(input('Digite a quarta nota :'))

print('NOTA 1 = {}\nNOTA 2 = {}\nNOTA 3 = {}\nNOTA 4 = {}\nSua Média Foi: {}' .format(nt1, nt2, nt3, nt4, float(nt1 + nt2 + nt3 + nt4) / 4))