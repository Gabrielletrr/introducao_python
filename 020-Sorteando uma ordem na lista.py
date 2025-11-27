import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
aluno5 = input('Digite o nome do quinto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
print(lista_alunos)
random.shuffle(lista_alunos)
print(f'A ordem de apresentação é {lista_alunos}')