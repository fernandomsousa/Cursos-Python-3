# Aprendendo manipulação de cadeias de texto em python!

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