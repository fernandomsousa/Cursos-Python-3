# Desenvolva um programa que pergunte a distância de uma viagem em Km. Caso a viagem seja até 200km, a passagem terá um valor de R$0.50 por Km.
# Caso a viagem seja superior a 200km, o valor sairá por R$0.45.

print('====== DESAFIO 31 - CUSTO DA VIAGEM! ======')

distancia = float (input('Digite a distância percorrida: '))

if distancia <= 200:
    print(f'Você irá percorrer {distancia:.0f}Km! Portanto, o valor a ser pago em sua passagem será: R${distancia * 0.50:.2f}')

else:
    print(f'Você irá percorrer {distancia:.0f}Km! Porntanto, o valor a ser pago em sua passagem será: R${distancia * 0.45:.2f}')

# Desafio concluído sem ajuda!