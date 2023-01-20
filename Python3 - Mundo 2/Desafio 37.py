# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# Bases: Binário; Octal; Hexadecimal.

print('\n====== DESAFIO 37 - CONVERSOR DE BASES NUMÉRICAS! ======\n')

cont = 1
menu ='x'

while cont != 0:
    print('-=-'*21)
    print('\033[1;32m{}BEM-VINDO AO MENU\033[m'.format(' '*20))
    print('-=-'*21)
    opcao = int (input('Selecione a opção desejada:\n[1] - Conversão em binário.\n[2] - Conversão em Octal.\n[3] - Conversão em Hexadecimal.\n[4] - Sair.\nSua escolha será: ')) 

    while opcao > 4 or opcao < 1: # Caso a opção esteja fora do range sugerido no menu.
        print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
        print('-=-'*21)
        print('\033[1;32m{}BEM-VINDO AO MENU\033[m'.format(' '*20))
        print('-=-'*21)
        opcao = int (input('Selecione a opção desejada:\n[1] - Conversão em binário.\n[2] - Conversão em Octal.\n[3] - Conversão em Hexadecimal.\n[4] - Sair.\nSua escolha será: '))
    pass

    if opcao == 1:
        numero = int (input('Digite um número inteiro qualquer: '))
        print('-=-'*21)
        print('{}\033[1;36m CONVERSÃO PARA BASE: BINÁRIO\033[m {}'.format('-'*15,'-'*15))
        print('-=-'*21)
        print(f'\033[1;31mRESULTADO:\033[m O número {numero} convertdo em base binária se torna: {bin(numero)}')
        menu = str (input('Deseja converter outro valor? Digite [Y] para continuar ou [N] para voltar ao menu: ')).capitalize()
        while menu != 'N':
            numero = int (input('Digite um número inteiro qualquer: '))
            print('-=-'*21)
            print('{}\033[1;36m CONVERSÃO PARA BASE: BINÁRIO\033[m {}'.format('-'*15,'-'*15))
            print('-=-'*21)
            print(f'\033[1;31mRESULTADO:\033[m O número {numero} convertdo em base binária se torna: {bin(numero)}')
            menu = str (input('Deseja converter outro valor? Digite [Y] para continuar ou [N] para voltar ao menu: ')).capitalize()
        pass

    elif opcao == 2:
        numero = int (input('Digite um número inteiro qualquer: '))
        print('-=-'*20)
        print('{}\033[1;36m CONVERSÃO PARA BASE: OCTAL\033[m {}'.format('-'*15,'-'*15))
        print('-=-'*20)
        print(f'\033[1;31mRESULTADO:\033[m O número {numero} convertdo em base octal se torna: {oct(numero)}')
        menu = str (input('Deseja converter outro valor? Digite [Y] para continuar ou [N] para voltar ao menu: ')).capitalize()
        while menu != 'N':
            numero = int (input('Digite um número inteiro qualquer: '))
            print('-=-'*21)
            print('{}\033[1;36m CONVERSÃO PARA BASE: OCTAL\033[m {}'.format('-'*15,'-'*15))
            print('-=-'*21)
            print(f'\033[1;31mRESULTADO:\033[m O número {numero} convertdo em base octal se torna: {oct(numero)}')
            menu = str (input('Deseja converter outro valor? Digite [Y] para continuar ou [N] para voltar ao menu: ')).capitalize()
        pass
    
    elif opcao == 3:
        numero = int (input('Digite um número inteiro qualquer '))
        print('-=-'*20)
        print('{}\033[1;36m CONVERSÃO PARA BASE: HEXADECIMAL\033[m {}'.format('-'*15,'-'*15))
        print('-=-'*20)
        print(f'\033[1;31mRESULTADO:\033[m O número {numero} convertdo em base hexadecimal se torna: {hex(numero)}')
        menu = str (input('Deseja converter outro valor? Digite [Y] para continuar ou [N] para voltar ao menu: ')).capitalize()
        while menu != 'N':
            numero = int (input('Digite um número inteiro qualquer: '))
            print('-=-'*21)
            print('{}\033[1;36m CONVERSÃO PARA BASE: HEXADECIMAL\033[m {}'.format('-'*15,'-'*15))
            print('-=-'*21)
            print(f'\033[1;31mRESULTADO:\033[m O número {numero} convertdo em base hexadecimal se torna: {hex(numero)}')
            menu = str (input('Deseja converter outro valor? Digite [Y] para continuar ou [N] para voltar ao menu: ')).capitalize()
        pass
    
    elif opcao == 4:
        cont = 0
        print('\033[1;33m{} PROGRAMA FINALIZADO, OBRIGADO UTILIZAR MEU SISTEMA DE CONVERSÃO! {}\033[m'.format('-'*20, '-'*20))
        break

# Um dos que mais gostei e me dediquei!!
# Desafio concluído sem ajuda!