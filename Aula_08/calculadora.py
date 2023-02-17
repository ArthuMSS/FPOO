import math

print(' 1 - Adição')
print(' 2 - Subtração')
print(' 3 - Multiplicação')
print(' 4 - Divisão')
print(' 5 - Potência')
print(' 6 - Raiz quadrada')
print(' 7 - Número par')
print(' 8 - Número ímpar')

escolha = int(input('Digite a operação que você deseja realizar: '))

if escolha == 1:
    print('Você escolheu Adição!')
elif escolha == 2:
    print('Você escolheu Subtração!')
elif escolha == 3:
    print('Você escolheu Multiplicação!')
elif escolha == 4:
    print('Você escolheu Divisão!')
elif escolha == 5:
    print('Você escolheu Potência!')
elif escolha == 6:
    print('Você escolheu Raiz Quadrada!')
elif escolha == 7:
    print('Você escolheu Número Par!')
elif escolha == 8:
    print('Você escolheu Número Impar!')

if escolha == 1:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número'))
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
elif escolha == 2:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número'))
    print('{} - {} = {}' .format(num1, num2, num1 - num2))
elif escolha == 3:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número'))
    print('{} x {} = {}'.format(num1, num2, num1 * num2))
elif escolha == 4:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número'))
    print('{} ÷ {} = {}' .format(num1, num2, num1 / num2))
elif escolha == 5:
    Pnum1 = int(input('Digite um número: '))
    Pnum2 = int(input('Digite a potencialização escolhida: '))
    print('{}*{} = {}' .format(Pnum1, Pnum2, pow(Pnum1, Pnum2)))
elif escolha == 6:
    Rnum1 = int(input('Digite o número escolhido: '))
    print('√{} = {:.3}'.format(Rnum1, math.sqrt(Rnum1)))
elif escolha == 7:
    PrNum = int(input('Digite um numero para verificar se o mesmo é par: '))
    PrnumCalc = PrNum % 2 == 0
    print('{} = {}'.format(PrNum, PrnumCalc))
elif escolha == 8:
    ImrNum = int(input('Digite o número para verificar se o mesmo é impar: '))
    ImrNumCalc = ImrNum % 2 == 1
    print('{} = {}'.format(ImrNum, ImrNumCalc))
else:
    print('Este Número não é válido !!!')