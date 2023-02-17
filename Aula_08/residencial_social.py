metrosCubicos = float(input('Digite quantos metros cubicos vc gastou: '))
if metrosCubicos <= 10:
    print('O seu gasto foi de R$7,59')
elif metrosCubicos <= 20:
    print('O seu gasto foi de R${:.4}' .format(1.31 * metrosCubicos))
elif metrosCubicos <= 30:
    print('O seu gasto foi de R${:.4}' .format(4.64 * metrosCubicos))
elif metrosCubicos <= 50:
    print('O seu gasto foi de R${:.4}' .format(6.62 * metrosCubicos))
else:
    print('O seu gasto foi de R${:.4}' .format(7.31 * metrosCubicos))