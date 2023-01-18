# Escreva um programa que faça o computador pensar em um número entre 0 e 5, após, peça para o usuário tentar descobrir.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('====== DESAFIO 28 - JOGO DE ADIVINHAÇÃO! ======')

from random import randint

numero = randint (0,5)

tentativa = int (input('Digite um número entre 0 e 5: '))

if tentativa == numero:
    print(f'Parabéns, você acertou o número era {numero} mesmo!')

else:
    print(f'Poooxa, você perdeu... O número era: {numero}.')

# Desafio concluído sem ajuda!