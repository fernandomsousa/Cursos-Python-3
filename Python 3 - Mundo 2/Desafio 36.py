# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele irá pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('====== DESAFIO 36 - APROVANDO EMPRÉSTIMO! ======')

valor_casa = float (input('Digite o valor da casa: R$'))
salario = float (input('Digite seu salário atual: R$'))
quantidade_anos = int (input('Digite em quantos anos irá pagar: '))
prestacao = float (f'{valor_casa / (quantidade_anos * 12):.2f}')

if prestacao > salario * 0.30:
    print('-=-'*20)
    print(f'\033[1;31m                    EMPRRÉSTIMO NEGADO!\033[m')
    print('-=-'*20)
    print(f'Sentimos muito... o valor da prestação será de: R${prestacao}\nEste valor de prestação é muito alto para o seu salário. Portanto, o seu empréstimo foi negado.')

else:
    print('-=-'*20)
    print('\033[1;32m                    EMPRRÉSTIMO APROVADO!\033[m')
    print('-=-'*20)
    print(f'Parabéns!! O valor da prestação será de: R${prestacao}\nEste valor de prestação é compatível com seu salário. Portanto, seu empréstimo está aprovado!')

# Desafio concluído sem ajuda!