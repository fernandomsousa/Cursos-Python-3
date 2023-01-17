# Aula para aprendizado de módulos!

# import math biblioteca com funcionalidades matemáticas
# Funcionalidade ceil = faz o arredondamento para cima.
# Funcionalidade floor = arredondamento para baixo.
# trunc = elimina a virgula pra frente, truncando.
# pow = potência.
# sqrt = raiz quadrada.
# factorial = cálculo fatorial
# caso queira usar apenas raiz quadrada, por exemplo, posso usar apenas from math import sqrt.

print('====== TESTES DAS TEORIAS ESTUDADAS ======')

import math

num = int (input('Digite um número:'))

raiz = math.sqrt(num)

print(f'A raiz de {num} arredondando para baixo é:{math.floor(raiz)}')

# Este é um exemplo dado em aula!