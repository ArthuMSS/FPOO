nt1 = float(input('Digite a nota 1: '))
nt2 = float(input('Digite a nota 2: '))
nt3 = float(input('Digite a nota 3: '))
nt4 = float(input('Digite a nota 4: '))
print('******************************')
mf = (nt1 + nt2 + nt3 +nt4) / 4

if mf >= 9.0 and mf <= 10:
    print('Nota 1 = {}\nNota 2 = {}\nNota 3 = {}\nNota 4 = {}\nMédia Final = {}\nConceito = {}\nResultado = {}'.format(nt1, nt2, nt3, nt4, mf, "A", "Aprovado"))
elif mf >= 7.5 and mf <= 8.9:
    print('Nota 1 = {}\nNota 2 = {}\nNota 3 = {}\nNota 4 = {}\nMédia Final = {}\nConceito = {}\nResultado = {}'.format(nt1, nt2, nt3, nt4, mf, "B", "Aprovado"))
elif mf >= 6.0 and mf <= 7.4:
    print('Nota 1 = {}\nNota 2 = {}\nNota 3 = {}\nNota 4 = {}\nMédia Final = {}\nConceito = {}\nResultado = {}'.format(nt1, nt2, nt3, nt4, mf, "C", "Aprovado"))
elif mf >= 4.0 and mf <= 5.9:
    print('Nota 1 = {}\nNota 2 = {}\nNota 3 = {}\nNota 4 = {}\nMédia Final = {}\nConceito = {}\nResultado = {}'.format(nt1, nt2, nt3, nt4, mf, "D", "Reprovado"))
elif mf >= 0 and mf <= 3.9:
    print('Nota 1 = {}\nNota 2 = {}\nNota 3 = {}\nNota 4 = {}\nMédia Final = {}\nConceito = {}\nResultado = {}'.format(nt1, nt2, nt3, nt4, mf, "E", "Reprovado"))