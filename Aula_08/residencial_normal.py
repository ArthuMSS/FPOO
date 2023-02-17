metrosCubicos = float(input('Digite quantos metros cubicos vc gastou: '))
if metrosCubicos <= 10:
    print('O seu gasto foi de R$22,38')
elif metrosCubicos <= 20:
    print('O seu gasto foi de R${:.5}' .format(3.50 * metrosCubicos))
elif metrosCubicos <= 50:
    print('O seu gasto foi de R${:.5}' .format(8.75 * metrosCubicos))
else:
    print('O seu gasto foi de R${:.5}' .format(9.64 * metrosCubicos))