# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('====== DESAFIO 27 ======')

nome_compĺeto = (input('Digite seu nome completo: ')).strip()

dividindo = nome_compĺeto.split()

print(f'Olá, {nome_compĺeto}!','\nSeu pŕimeiro nome é:',dividindo[0].capitalize(),'\nE seu último nome é:', dividindo[-1].capitalize())

print('Seu último nome é:',dividindo[len(dividindo)-1].capitalize()) # Forma alternativa vista durante a correção, onde visualizo a quantidade de indices já dividios e printo o último, com -1 pois o 0 conta.

# Desafio concluído sem ajuda!