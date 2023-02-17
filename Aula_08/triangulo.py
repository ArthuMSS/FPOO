L1 = int(input('Digite o Lado 1 do triangulo: '))
L2 = int(input('Digite o Lado 2 do triangulo: '))
L3 = int(input('Digite o Lado 3 do triangulo: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Não é um triângulo')
elif L1 == L2 and L2 == L3 and L1 == L3:
    print('Triângulo Equilátero')
elif L1 == L2 or L2 == L3 or L1 == L3:
    print('Triângulo Isósciles')
else:
    print('Triângulo Escaleno')