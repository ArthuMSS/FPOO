nota1 = input('Entre com a 1 nota: ')
nota2 = input('Entre com a 2 nota: ')
media = (int(nota1) + int(nota2)) / 2
if media >= 5:
    print('parabens, voce passou')
elif media >= 3 and media <= 4:
    print('recuperacao!!!!')
elif media < 3:
    print('Que pena, voce esta reprovado')