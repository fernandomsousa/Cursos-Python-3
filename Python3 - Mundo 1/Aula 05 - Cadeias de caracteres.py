# Aprendendo mamipulação de cadeias de texto em python!
# Fatiamento = técnica trabalhada para fatiar uma string, exemplo:
# Tenho uma string de 21 caracteres, então fatio-a da seguinte forma: frase[9].
# Fatiando apenas uma única letra da string que está atribuída no índice 9 (contando de 0 a 21).
# Há outra forma de fatiar, como: frase[9:13], fatiando do indice 9 ao 13.
# Porém, o python elimina o último indice, então iria apenas do índice 9 ao 12.
# Posso também utilizar o [9:20:2] fazendo com que vá do 9 ao 20, pulando de dois em dois e contando o 2.
# Caso seja [:5] ele pega do começo ao 5, pois não há valor de inicio, começando do caractere 0. Assim, posso dar um range começando do inicio e indo até o 5 (excluindo o caractere do 5).
# Caso seja [15:] Não sei onde estáo final, vou do índice 15 até o final da frase.
# [9::3] Começa no nove, vai até o final e pulando de 3 em 3.
# len(frase) = eu analiso e mostro o tamanho contando todos os indices começando do 1, contando todos os caracteres.
# frase.count('o') = faz com que o meu programa conte quantas vezes aparece a letra 'o' minuscula em frase.
# Posso fazer esta contagem anterior com fatiamento: frase.count('o', 0, 13), contando do indice 0 ao 12 todas as letras 'o' minusculas que aparecerem.
# frase.find('deo') = me mostra quantas vezes 'deo' foi encontrado na frase, me dizendo o momento que começou e terminou: iniciando da posição 11.
# Caso eu digite algo que o find nao possa localizar, receberei a resposta '-1', dizendo que a string não pode ser localizada em sua referencia.
# Posso usar o operador 'in': 'Curso' in frase, se existir, me dispõe true ou false, pois existe sim a palavra ou nao.
# Listas são imutáveis, mas posso traalhar com métodos: frase,replace('Python', 'Android') = vai encontrar a palavra python e trocar por android.
# frase.upper(Torna a frase da variável em maiúsculo); Já o frase.lower() deixa tudo em minusculo.
# frase.capitalize() = joga tudo pra minusculo, toda a string e a primeira letra torna-se maiúscula.
# de forma parecida, o frase.title() vê quantas palavras a string tem e faz capitalize de palavra por palavra, iniciando a 1 letra de todas as palavras Com Letra Maiúscula.
# Para remover espações excedentes do inicio e fim, utiliza-se o frase.strip(), apagando os espaços inuteis do inicio e fim.
# o A que era o caractere 3, passa a ser o 0.
# Temos o frase.rstrip() = que é o lado direito, faz a remoção de caracteres apenas do lado direito da string. Há outros módulos em python que podem contar com essa função também.
# Já o frase.lstrip() = faz a remoção apenas do lado esquerdo.
# Divisão de strings: frase.split(), faz uma divisão dentro da string considerando os espaços, onde houver espaços fará o ínicio de um novo índice.
# Ao fim, ele gera diversos espaços diferentes e os aloca em outros espaços diferentes (anotações com imagens no notion).
# Caso eu queira juntar os elementos de frases separados por um split, por exemplo: '-'.join(frase) = junto todos os blocos pelo caractere '-'.
''' LEMBRETE: STRING É IMUTÁVEL!!! '''
# Fim das anotações!

print('====== TESTES DAS TEORIAS ESTUDADAS ======')

frase = 'Curso em Video Python'
print(frase[::2]) # fatiamento de string e pulando de 2 em 2.
print(frase.lower().count('o')) # Torno os caracteres em minusculos e verifico a quantidade de 'o'.
print(frase.upper()) # torno todos os caracteres maiusculos.
print(len(frase.strip())) # função len com strip removendo os espaços que me retorna o tamanho da string (21), sem strip seria 27.
print(len(frase.lstrip())) # len com strip apenas ao lado esquerdo.
print(frase.replace('Python','Android')) #  Altero a palavra python para android.
print(frase[0:].replace('C', 'T')) # Utilizando o módulo de reposição, posso fazer substituições livremente mesmo em posições especificas de uma string.
print('Curso' in frase) # Verifica se a palavra 'Curso' está em frase, obviamente se difere entre letras maiusculas e minusculas e devolve True ou False.
print(frase.find('em')) # Localiza o indice que a palavra 'em' está localizada e devolve sua primeira posição (6).
print(frase.find('boneca')) # Retorna -1 pois não há 'boneca' em nenhuma parte da string.
print(frase.upper().find('Video')) # Retorna -1 pois faz a conversão da palavra 'Video' para totalmente em maiúscula, tornando-a distinta para o find pois o mesmo difere maiúscula e minúscula.

dividido = frase.split() # Aqui efetuo a divisão das palavras contidas em frase.

print(dividido[2][:]) # Desta forma, mostro apenas a letra 3 da palavra contida na segunda divisao da frase (video).

# Aula concluída!