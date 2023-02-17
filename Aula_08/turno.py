print('**************************')
print('Matutino\nVespertino\nNoturno')
print('**************************')

turno = input('Digite o turno que você costuma estudar: ')

if turno == 'Matutino':
    print('Bom dia!')
elif turno == 'Vespertino':
    print('Boa tarde!')
elif turno == 'Noturno':
    print('Boa noite!')
else:
    print('letra capitalizada')
