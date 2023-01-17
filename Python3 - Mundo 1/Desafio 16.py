# Crie um programa que leia um número Real e mostre na tela a sua porção inteira.

print('====== DESAFIO 16 ======')

from math import trunc

num = float(input('Digite um número Real: '))

print(f'A parte inteira do número real digitado é: {trunc(num)}')

print(f'A parte inteira do número real digitado (agora com int) é: {int(num)}')

# Acima, podemos ver duas formas distintas de executar o mesmo objetivo, mostrando que nem sempre há necessidade de importar biblioetcas.

# Desafio concluído sem ajuda!