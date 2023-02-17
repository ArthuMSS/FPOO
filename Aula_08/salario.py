salarioFuncionario = float(input('Digite o salário de um funcionário: '))
if salarioFuncionario <= 1000:
    print('Salário digitado: {}\nAumento: {}\nValor do aumento: {}\nNovo salário: {}'.format(salarioFuncionario, "20%", ((salarioFuncionario * 20) / 100), salarioFuncionario + (salarioFuncionario * 20) / 100))
elif salarioFuncionario <= 1700:
    print('Salário digitado: {}\nAumento: {}\nValor do aumento: {}\nNovo salário: {}'.format(salarioFuncionario, "10%", ((salarioFuncionario * 10) / 100), salarioFuncionario + (salarioFuncionario * 10) / 100))
elif salarioFuncionario <= 2300:
    print('Salário digitado: {}\nAumento: {}\nValor do aumento: {}\nNovo salário: {}'.format(salarioFuncionario, "15%", ((salarioFuncionario * 15) / 100), salarioFuncionario + (salarioFuncionario * 15) / 100))
else:
    print('Salário digitado: {}\nAumento: {}\nValor do aumento: {}\nNovo salário: {}'.format(salarioFuncionario, "5%", ((salarioFuncionario * 5) / 100), salarioFuncionario + (salarioFuncionario * 5) / 100))