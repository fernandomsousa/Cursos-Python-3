# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo
# E por fim, calcule e mostre o comprimento da hipotenusa.

print('====== DESAFIO 17 ======')

from math import sqrt

cateto_oposto = float (input('Insira o valor do cateto oposto: '))
cateto_adjascente = float (input('Insira o valor do cateto adsjacente: '))

hipotenusa = sqrt(cateto_oposto**2 + cateto_adjascente**2)

print(f'O valor da hipotenusa trabalhando com os catetos digitados é: {hipotenusa:.3f}!')

# Desafio concluído sem ajuda!