frase = str(input('Digite uma frase: ').strip().upper())

print(f'A letra A aparece {frase.count('A')} vezes na frase')

print(f'A primeira incidência da letra A é no índice {frase.find('A')+1}')

print(f'A última incidênci da letra A é no índice {frase.rfind('A')+1}')


