# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('====== DESAFIO 10 ======')

money = float (input('Digite a quantia presente em reais na sua carteira: R$'))
dolar = money / 5.16
euro = money / 5.55

print(f'Com R${money} você pode comprar US${dolar:.2f} e EUR€{euro:.2f}')

# Desafio resolvido com ajuda...