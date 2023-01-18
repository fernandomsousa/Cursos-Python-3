# Aprendendo condições em pyhton!

print('====== TESTE 1 ======') # Exemplo de condição comum.

nome = (input('Qual seu nome? ')).capitalize()

if nome == 'Gustavo':
    print('Que nome lindo o seu!')

else:
    print('Seu nome é tão normal...')

print(f'Bom dia, {nome}!')

print('====== TESTE 2 ======') # Exemplo clássico de condição comum.

n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print(f'A sua média final é: {media}')

if media >= 6.0:
    print('Sua média foi boa, está aprovado!')

else:
    print('Sua média foi menor que o essencial, está reprovado!')

print('====== TESTE 3 ======') # Exemplo de condição simplificada.

print(f'PARABÉNS, VOCÊ ESTÁ APROVADO!' if media >=6 else 'ESTUDE MAIS, ESTÁ REPROVADO...')

# Aula concluída!