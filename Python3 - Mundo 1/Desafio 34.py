# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários maiores que R$1250, calcular um aumento de 10%; Para inferiores, aumento de 15%.

print('====== DESAFIO 34 - AUMENTOS MÚLTIPLOS! ======')

salario = float (input('Digite o valor do seu salário R$'))

if salario >= 1250:
    print(f'Seu salário atual é de R${salario:.2f}. Portanto receberá um aumento de 10%!\nSeu aumento será de R${salario*0.10:.2f}.\nLogo, o total será de R${salario*0.10 + salario:.2f}')

else:
    print(f'Seu salário atual é de R${salario:.2f}. Portanto receberá um aumento de 15%!\nSeu aumento será de R${salario*0.15:.2f}\nLogo, o total será de R${salario*0.15 + salario:.2f}')

# Desafio concluído sem ajuda!