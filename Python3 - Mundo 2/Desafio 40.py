# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado!; Entre 5.0 e 6.9: Recuperação!; 7.0 ou maior: Aprovado!.

print('====== DESAFIO 40 - AQUELE CLÁSSICO DA MÉDIA! ======\n')

nome = input('Digite seu nome: ').capitalize()

while nome.isnumeric() == True:
    print('\n\033[1;31mVOCÊ DIGITOU UM VALOR NUMÉRICO, DIGITE UM NOME REAL!\033[m\n')
    nome = input('Digite seu nome: ').capitalize()
pass

n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('-=-'*13,'\n\033[1;31m{}VOCÊ FOI REPROVADO!\033[m'.format(' '*10))
    print('-=-'*13,f'\n\nSinto-lhe informar, {nome} mas você \033[4mreprovou\033[m pois sua média foi de: {media}\n')

elif media >= 5.0 and media <= 6.9:
    print('-=-'*13,'\n\033[1;33m{}VOCÊ ESTÁ DE RECUPERAÇÃO!\033[m'.format(' '*6))
    print('-=-'*13,f'\n\nVocê não foi muito bem, {nome}. Sua média foi {media}. Portanto, ainda há possibilidade de recuperação de nota!\n')

elif media >= 7.0:
    print('-=-'*13,'\n\033[1;32m{}VOCÊ FOI APROVADO!\033[m'.format(' '*10))
    print('-=-'*13,f'\n\nMeus parabéns pela aprovação, {nome}! Sua média foi: {media}. Portanto, você está aprovadissimo!\n')

# Desafio concluído sem ajuda!