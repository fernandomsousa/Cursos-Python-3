# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ainda irá se alistar; Se já é a hora de se alistar; Se ja passou da hora.

print('\n====== DESAFIO 39 - ALISTAMENTO MILITAR! ======\n')

from datetime import date

ano_atual = date.today().year
ano_nasc = int (input('Digite o ano em que você nasceu: '))
idade_atual = int (ano_atual - ano_nasc)
contador = len(str(ano_nasc))

while contador > 4 or contador <4:
    print(f'\n\033[1;31mVOCÊ INSERIU UM ANO DE {contador} DIGITOS! POR FAVOR, INSIRA UM ANO VÁLIDO!\033[m\n')
    ano_atual = date.today().year
    ano_nasc = int (input('Digite o ano em que você nasceu:'))
    idade_atual = int (ano_atual - ano_nasc)
    contador = len(str(ano_nasc))
pass

if idade_atual == 18:
    print('-=-'*20,"\n\033[1;32m{}HORA DE SE ALISTAR, CAMPEÃO!\033[m".format(' '*15))
    print('-=-'*20)
    print(f'\nVocê possui {idade_atual} anos de idade! Portanto, este é o momento exato no qual se deve efetuar o alistamento militar.\n')

elif idade_atual > 18:
    tempo_atraso = (ano_atual - ano_nasc) - 18
    print('-=-'*20,"\n\033[1;31m{}ATRASADO, CORRA IMEDIATAMENTE!!\033[m".format(' '*15))
    print('-=-'*20)
    print(f'\nVocê possui {idade_atual} anos de idade! Portanto, está atrasado para o alistamento militar em {tempo_atraso} anos, busque se regularizar imediatamente!\nSeu alistamento deveria ter sido feito no ano de: {ano_atual - tempo_atraso}!\n')

elif idade_atual < 18:
    tempo_adiantado = 18 - (idade_atual)
    print('-=-'*20,'\n\033[1;33m{}CALMA, AINDA NÃO CHEGOU SEU MOMENTO DE SE ALISTAR!\033[m'.format(' '*5))
    print('-=-'*20)
    print(f'\nVocê possui {idade_atual} anos de idade, portanto deve esperar mais {tempo_adiantado} anos até que complete 18!\nSeu alistamento será no ano de: {ano_atual + tempo_adiantado}!\n')
    
# Desafio concluído sem ajuda!