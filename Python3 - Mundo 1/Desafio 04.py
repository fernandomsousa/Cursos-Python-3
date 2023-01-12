# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('====== DESAFIO 04 ======')

n = input('Digite algo: ')

print('O tipo primitivo do valor digitado é:',type(n))
print('O valor digitado é composto por letra(s)?',n.isalpha())
print('O valor digitado é composto por número(s)?',n.isnumeric())
print('O valor digitado é alfanumérico?',n.isalnum())
print('O valor digitado é composto somente por espaços?',n.isspace())
print('O valor digitado está disposto completamente em letras maiúsculas?',n.isupper())
print('O valor digitado está disposto completamente em letras minúsculas?',n.islower())
print('O valor digitado está capitalizado?',n.istitle()) # Verifica se a variável está capitalizada, com a primeira letra maiúscula como em um titulo.

# Desafio concluído sem ajuda!