# Um professor que sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

print('====== DESAFIO 19 ======')

from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

print(f'O aluno escolhido é: {choice([aluno1, aluno2, aluno3, aluno4])}')

# Quando trabalho com choice, posso criar uma lista durante o print ou separadamente.
# Já com shuffle, obrigatoriamente a lista deve ser separada.

# Desafio Concluído sem ajuda!