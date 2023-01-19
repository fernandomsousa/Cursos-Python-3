# Desenvolva um programa que leia o comprimento de três retas e diga se o usuário conseguiu ou não formar umn triângulo.
# Condição de existência = a soma de dois lados é sempre menor que o terceiro lado.

print('====== DESAFIO 34 - ANALISANDO TRIÂNGULO! ======')

v1 = float (input('Digite o primeiro comprimento: '))
v2 = float (input('Digite o segundo comprimento: '))
v3 = float (input('Digite o terceiro comprimento: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Forma um triângulo!')

else: 
    print("Não forma um triângulo!")

# Desafio concluído com ajuda...
# PYTHON 3 - MUNDO 1 FINALIZADO!