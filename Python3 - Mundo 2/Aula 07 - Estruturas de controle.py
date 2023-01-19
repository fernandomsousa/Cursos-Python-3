# Aprendendo estruturas de controle!

nome = str (input('Qual seu nome? ')).strip().capitalize()

if nome == 'Fernando':
    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print(f'Seu nome é bem popular aqui no Brasil, {nome}!')

elif nome in 'Ana Claudia Jessica Junliana':
    print(f'Belo nome feminino, {nome}!')

else:
    print('Seu nome é bem padrão...')

print(f'Tenha um bom dia, \033[1;32m{nome}!\033[m')

# O Else é opcional, não senod obrigatório na execução da estrutura condicional aninhada!

# Aula concluída!