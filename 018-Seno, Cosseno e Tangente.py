import math
angulo = float(input('Digite um ângulo: '))

angulo_radiano = math.radians(angulo)

print(f'O seno é {math.sin(angulo_radiano):.2f}')
print(f'O cosseno é {math.cos(angulo_radiano):.2f}')
print(f'A tangente é {math.tan(angulo_radiano):.2f}')