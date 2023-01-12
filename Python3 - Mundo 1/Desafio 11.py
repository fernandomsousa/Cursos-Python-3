# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

print('====== DESAFIO 11 ======')

largura = float (input('Digite a largura de uma parede em metros: '))
altura = float (input('Digite a altura de uma parede em metros: '))
area = largura * altura

print(f'Utilizando {largura:.2f}m de largura e {altura:.2f}m de altura, pode-se calcular uma área de: {area:.2f}m²')  
print(f'Para pintar a parede completamente, você precisará de {area/2}L de tinta.')

# Desafio concluído sem ajuda!
