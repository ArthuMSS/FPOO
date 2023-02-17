salario = float(input('Digite um salário qualquer: '))
if salario <= 1302 or salario <= 1903.98:
    print('Desconto de 7,5%\nDescontado = {:.2f}\nTotal = {:.2f}'.format( ((salario * 7.5) / 200) ,salario - (salario * 7.5) / 200))
elif salario <= 2571.29 or salario <= 2826.65:
    print('Desconto de 16,5%,\nDescontado = {:.2f}\nTotal = {:.2f}'.format( ((salario * 16.5) / 200),salario - (salario * 16.5) / 200))
elif salario <= 3751.05 or salario <= 3856.94:
    print('Desconto de 27%\nDescontado = {:.2f}\nTotal = {:.2f}'.format( ((salario * 27) / 200) ,salario - (salario * 27) / 200))
elif salario <= 7507.49 or salario <= 4664.68:
    print('Desconto de 36,5%\nDescontado = {:.2f}\nTotal = {:.2f}'.format( ((salario * 36.5) / 200) ,salario - (salario * 36.5) / 200))
else:
    print('Salário Inválido, tente um Número menor!')