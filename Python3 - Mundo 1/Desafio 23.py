# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: 1834 = unidade: 4; dezena: 3; centena: 8; milhar = 1;

print('====== DESAFIO 23 ======')

numero = str (input('Digite um número de 0 a 9999: '))

numero = numero.split()

print(f'Unidade: {numero[0][3]}.')
print(f'Dezena: {numero[0][2]}.')
print(f'Centena: {numero[0][1]}.')
print(f'Milhar: {numero[0][0]}.')

# Desafio concluído sem ajuda!