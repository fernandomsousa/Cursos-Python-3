# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

print('====== DESAFIO 15 ======')

km = float (input('Quantos Km o veículo percorreu? '))
dias = int (input('Quantos dias o veículo esteve alugado? '))

print(f'A taxa total calculada por km é: R${km*0.15:.2f}\nA taxa total calculada por dia alugado é: R${dias*60.00:.2f}\nO valor total a pagar é: R${(km*0.15)+(dias*60.00):.2f}')

# Desafio concluido sem ajuda!