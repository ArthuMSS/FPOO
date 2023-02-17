metrosCubicos = float(input('Digite quantos metros cubicos vc gastou de água: '))
if metrosCubicos <= 10:
    print('O seu gasto foi de R$44.95')
elif metrosCubicos <= 20:
    print('O seu gasto foi de R${:.5}' .format(8.75 * metrosCubicos))
elif metrosCubicos <= 50:
    print('O seu gasto foi de R${:.5}' .format(16.76 * metrosCubicos))
else:
    print('O seu gasto foi de R${:.5}' .format(17.46 * metrosCubicos))