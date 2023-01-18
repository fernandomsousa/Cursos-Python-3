# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: 1834 = unidade: 4; dezena: 3; centena: 8; milhar = 1;

print('====== DESAFIO 23 ======')

numero = int (input('Digite um número de 0 a 9999: '))

print(f'Unidade: {numero // 1 % 10}.')
print(f'Dezena: {numero // 10 % 10}.')
print(f'Centena: {numero // 100 % 10}.')
print(f'Milhar: {numero // 1000 % 10}.')

# Desafio concluído sem ajuda!