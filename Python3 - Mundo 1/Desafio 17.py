# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo
# E por fim, calcule e mostre o comprimento da hipotenusa.

print('====== DESAFIO 17 ======')

from math import sqrt, hypot

cateto_oposto = float (input('Insira o valor do cateto oposto: '))
cateto_adjascente = float (input('Insira o valor do cateto adsjacente: '))

hipotenusa = sqrt(cateto_oposto**2 + cateto_adjascente**2)

print(f'O valor da hipotenusa trabalhando com os catetos digitados é: {hipotenusa:.3f}!')
print(f'O valor da hipotenusa utilizando a biblioteca hypot é: {hypot(cateto_oposto, cateto_adjascente):.3f}!')

# Acima, vemos mais de uma forma de trabalhar com bibliotecas dentro de amth para obter o resultado final!

# Desafio concluído sem ajuda!