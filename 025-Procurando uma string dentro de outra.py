"""
nome = input('Digite seu nome completo:').lower().strip()

sobrenome = nome.split()

if sobrenome[2][0:7] == 'machado' or sobrenome[1][0:7] == 'machado':
    print('Seu nome tem Machado')

else:
    print('Seu nome não tem Machado')

"""

nome = str(input('Digite um nome completo: ')).lower().strip()

print('O nome tem Machado? {}'.format('machado' in nome ))


