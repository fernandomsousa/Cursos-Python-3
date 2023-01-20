# Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo serpa formado.

print('\n====== DESAFIO 42 - ANALISANDO TRIÂNGULOS V2! ======\n')

v1 = float (input('Digite o primeiro comprimento: '))
v2 = float (input('Digite o segundo comprimento: '))
v3 = float (input('Digite o terceiro comprimento: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('\n\033[1;32m{}FORMA UM TRIÂNGULO!\033[m'.format(' '*5))
    
    if v1 == v2 == v3:
        print(f'\033[1;33mTEREMOS UM TRIÂNGULO EQUILÁTERO!\033[m\n')

    elif v1 == v2 != v3 or v1 == v3 != v2 or v2 == v1 != v3 or v2 == v3 != v1 or v3 == v1 != v2 or v3 == v2 != v1:
        print(f'\033[1;34mTEREMOS UM TRIÂNGULO ISÓSCELES!\033[m\n')

    elif v1 != v2 or v1 != v3 or v2 != v1 or v2 != v3 or v3 != v1 or v3!= v2:
        print(f'\033[1;35mTEREMOS UM TRIÂNGULO ESCALENO!\033[m\n')

else: 
        print("\n\033[1;31mOS VALORES INFORMADOS NÃO FORMAM UM TRIÂNGULO!\033[m\n")

# Desafio concluído sem ajuda!