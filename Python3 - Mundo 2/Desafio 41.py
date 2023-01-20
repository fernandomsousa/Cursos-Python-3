# Crie um programa que leia um ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: Mirim; até 14: Infantil; Até 19: Junior; té 20: Sênior; Acima: Master.

print('\n====== DESAFIO 41 - CLASSIFICANDO ATLETAS! ======\n')

from datetime import date

ano_nasc = int (input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade_atual = ano_atual - ano_nasc
contador = len(str(ano_nasc))

while contador < 4 or contador > 4:
    print(f'\n\033[1;31mDIGITE UM ANO VÁLIDO!\033[m\n')
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    contador = len(str(ano_nasc))

if idade_atual <= 9:
    print('-=-'*20,'\n\033[1;32m{}NADADOR MIRIM DETECTADO!\033[m'.format(' '*17))
    print('-=-'*20,f'\n\nVocê tem {idade_atual} anos! Portanto, é considerado um nadador Mirim.\n')

elif idade_atual > 9 and idade_atual <= 14:
    print('-=-'*20,'\n\033[1;36m{}NADADOR INFANTIL DETECTADO!\033[m'.format(' '*17))
    print('-=-'*20,f'\n\nVocê tem {idade_atual} anos! Portanto, é considerado um nadador Infantil.\n')

elif idade_atual > 14 and idade_atual <= 19:
    print('-=-'*20,'\n\033[1;33m{}NADADOR JUNIOR DETECTADO!\033[m'.format(' '*17))
    print('-=-'*20,f'\n\nVocê tem {idade_atual} anos! Portanto, é considerado um nadador Junior.\n')

elif idade_atual > 19 and idade_atual <= 25:
    print('-=-'*20,'\n\033[1;34m{}NADADOR SÊNIOR DETECTADO!\033[m'.format(' '*17))
    print('-=-'*20,f'\n\nVocê tem {idade_atual} anos! Portanto, é considerado um nadador Sênior.\n')

elif idade_atual > 25 and idade_atual <= 99:
    print('-=-'*20,'\n\033[1;35m{}NADADOR MASTER DETECTADO!\033[m'.format(' '*17))
    print('-=-'*20,f'\n\nVocê tem {idade_atual} anos! Portanto, é considerado um nadador Master.\n')

elif idade_atual > 99:
    print('-=-'*20,'\n\033[1;37m{}NADADOR PRÉ-HISTÓRICO DETECTADO!\033[m'.format(' '*17))
    print('-=-'*20,f'\n\nVocê tem {idade_atual} anos! Portanto, é considerado parente da Rainha Elizabeth.\n')

# Desafio concluído sem ajuda!