nome = input('Digite seu nome completo:').strip()

print(f'Seu nome todo em maiúsculo {nome.upper()}')
print(f'Seu nome em minúsculo {nome.lower()}')
sem_espaco = nome.replace(' ', '')
print(f'Essa é a quantidade de letras do seu nome {len(sem_espaco)}')
atualizado = nome.split()
print(f'Seu primeiro nome tem {len(atualizado[0])} letras')
