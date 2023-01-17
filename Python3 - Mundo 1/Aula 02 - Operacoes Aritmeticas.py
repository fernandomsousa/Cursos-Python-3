# Estudando Operadores Aritméticos!

print('====== TESTES DAS TEORIAS ESTUDADAS ======')

n1 = int (input('Digite o primeiro número: '))
n2 = int (input('Digite o segundo número: '))

print(f'Exemplo de soma em Python: {n1 + n2}')
print(f'Exemplo de subtração em Python: {n1 - n2}')
print(f'Exemplo de multiplicação em Python: {n1 * n2}')
print(f'Exemplo de divisão em Python: {n1 / n2:.3f}')
print(f'Exemplo de potência em Python: {n1 ** n2}')
print(f'Exemplo de divisão inteira em Python: {n1 // n2}')
print(f'Exemplo de resto de divisão em Python: {n1 % n2}')

# Ordem de precedência: 1° (); 2° **; 3° *, /, //, %; 4° +,-.
# No 3° e 4° a ordem entre eles vale para o operador que aparecer primeiro.