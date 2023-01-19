# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from datetime import date
from time import sleep

print('====== DESAFIO 32 - ANO BISSEXTO! ======')

ano = int (input("Digite um ano para analisar ou '0' para analisar o ano do seu computador: "))

print("Verificando....")
sleep(2)

if ano == 0: 
    ano = date.today().year # Condição da biblioteca datetime para validar o ano da minha máquina.

print(f'O ano de {ano} é um ano bissexto!' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f'O ano de {ano} não é um ano bissexto!')

# Desafio concluído com if simples!
# Adicionado na correção: verificar o ano do computador atualmente e dizer se é bissexto.

# Desafio concluído sem ajuda!