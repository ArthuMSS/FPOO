nt1 = float(input('Digite a primeira nota:'))
nt2 = float(input('Digite a segunda nota:'))
nt3 = float(input('Digite a terceira nota:'))
nt4 = float(input('Digite a quarta nota:'))

mf = (nt1 + nt2 + nt3 + nt4) / 4

if (mf >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')