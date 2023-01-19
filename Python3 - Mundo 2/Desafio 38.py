# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é o maior; O segundo valor é o maior; Não existe valor maior, os dois são iguais.

print('====== DESAFIO 38 - COMPARANDO NÚMEROS! ======')

num1 = int (input('Digite o primeiro valor: '))
num2 = int (input('Digite o segundo valor: '))

if num1 > num2:
    print(f'O primeiro valor ({num1}) é o maior entre os dois!')

elif num2 > num1:
    print(f'O segundo valor ({num2}) é o maior entre os dois!')

elif num1 == num2:
    print('Não existe um valor maior, os dois são iguais!')

# Desafio concluído sem ajuda!