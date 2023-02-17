print('# 1 - Opção1 #')
print('# 2 - Opção2 #')
print('# 3 - Opção3 #')
print('# 4 - Sair #') 

usuario = int(input('Digite uma das opções acima: '))

if usuario == 1:
    print('Você selecionou a opção 1')
elif usuario == 2:
    print('Você selecionou a opção 2')
elif usuario == 3:
    print('Você selecionou a opção 3')
elif usuario == 4:
    print('Você selecionou Sair')
else:
    print('Número Inválido!')