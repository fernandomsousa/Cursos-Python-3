# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km, diga que foi multado!
# Caso ele seja multado, a multa deverá custar R$7.00 por cada km excedido.

print('====== DESAFIO 28 - RADAR ELETRÔNICO! ======')

velocidade = float (input('Digite a velocidade atual do veículo: '))

if velocidade > 80:
    print(f"Você ultrapassou o limite, passou em {velocidade:.0f}Km/h!\nIsto resulta uma multa de: R${(velocidade - 80)*7.00:.2f}")

else:
    print(f'Você passou no radar em {velocidade:.0f}Km/h. Portanto, não foi multado!')

# Por identação, não precisaria do else, usando a chamada "condição simples".

# Desafio concluído sem ajuda!