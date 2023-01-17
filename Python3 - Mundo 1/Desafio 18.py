# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente.

print('====== DESAFIO 18 ======')

from math import radians, sin, cos, tan

angulo = float (input('Digite um ângulo qualquer: '))

angulo2 = radians(angulo)
seno = sin(angulo2)
cosseno = cos(angulo2)
tangente = tan(angulo2)

print(f'Sobre o ângulo {angulo}, temos:\nseu seno é: {seno:.2f}\nSeu cosseno é: {cosseno:.2f}\nE sua tangente é: {tangente:.2f}')

# Durante a correção, descobri que posso utilizar a conversão de radians dentro do sen e tudo mais
# seno = math.sin(math.radians(angulo2))

# Desafio concluído sem ajuda!