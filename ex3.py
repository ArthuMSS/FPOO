# 3. Crie um programa que leia algo e informe:
#    3.1. O tipo primitivo dessa informação;
#    3.2. Só tem espaços em branco;
#    3.3. É do tipo numérico;
#    3.4. É do tipo string;
#    3.5. Está em letras maiúculas;
#    3.5. Está em letras minúculas;
#    3.6. Está captalizada.

algo = input('Digite alguma coisa: ')

# Tipo Primitivo
print(type(algo))

# Só tem espaços em branco?
print('Só tem espaços em branco?', algo.isspace())

# É do tipo numérico?
print('É do tipo numérico?', algo.isnumeric())

# É do tipo string?
print('É do tipo string?', algo.isalpha())

# Está em letras maiúsculas?
print('Está em letras maiúsculas?', algo.isupper())

# Está em letras minúsculas?
print('Está em letras minúsculas?', algo.islower())

# Está capitalizada?
print('Está capitalizada?', algo.capitalize())

