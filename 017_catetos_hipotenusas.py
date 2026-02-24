from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

print(f'A hipotenusa do triângulo é: {hypot(cateto_oposto, cateto_adjacente):.2f}')