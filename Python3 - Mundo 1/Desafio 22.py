# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas; Todas as letras minúsculas; Quantas letras ao todo, sem considerar espaços; Quantas letras tem o primeiro nome.

print('====== DESAFIO 22 ======')

nome = (input('Digite seu nome completo: '))

print(f'Seu nome com todas as letras maiúsculas é: {nome.strip().upper()}.\nSeu nome com todas as letras minúsculas é: {nome.strip().lower()}.')

quantidade = len(nome.strip())
print(f'A quantidade de letras que seu nome completo possui é:', quantidade - nome.strip().count(' '), 'letras!')

dividido = nome.split()
print(f'Seu primeiro nome é: {dividido[0].capitalize()}.' )

# Desafio concluído sem ajuda!