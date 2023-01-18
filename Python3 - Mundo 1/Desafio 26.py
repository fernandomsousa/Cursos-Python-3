# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes a letra A aparece; Em que posição ela aparece a primeira vez; Em que posição ela aparece a última vez.

print('====== DESAFIO 26 ======')

frase = input("Digite uma frase: ").strip()

print(f"A letra' a' na frase '{frase}' aparece:",frase.upper().count('A'), "vezes!")

print(f"A letra 'a' aparece pela primeiro vez no indice:",frase.upper().find('A')+1)
print(f"A letra 'a' aparece pela última vez no indice:",frase.upper().rfind("A")+1)

# Desafio concluído sem ajuda!