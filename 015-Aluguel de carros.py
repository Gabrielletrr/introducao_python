km = float(input('Digite a quantidade de KM percorridos: '))
dia = int(input('Digite a quantidade de dias que você ficou como carro: '))

preco_dia = dia * 60
preco_km = km * 0.15

preco_total = preco_dia + preco_km

print('O preço total que você deve pagar é {}'.format(preco_total))