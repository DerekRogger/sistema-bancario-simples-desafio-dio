print('\nDESAFIO DIO - POTÊNCIA TECH POWERED BY IFOOD')
menu = '''
Informe qual serviço realizar:

--------------- 
[D] Depositar |
---------------
[S] Sacar     |
---------------
[E] Extrato   |
---------------
[X] Sair      |
---------------
===> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu).upper()

    if opcao == 'D':
        valor = float(input(('\nInforme o valor do Depósito: ')))
        print('Depositando...')

        if valor > 0:
            saldo += valor
            extrato += f'Depósito no valor de: R$ {valor:.2f}\n'
        else:
            print('\nOperação falhou! O valor informado é inválido')
    
    elif opcao == 'S':
        valor = float(input(('\nInforme o valor do Saque: ')))
        print('Em andamento...')

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo: 
            print('\nOperação falhou! você não tem saldo suficiente.')

        elif excedeu_limite:
            print('\nOperação falhou! O valor do saque excede o limite de R$ 500 por saque.')

        elif excedeu_saques:
            ('\nOperação falhou! Número de saques excedidos.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'E':
        print('==============EXTRATO============') 
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=================================') 


    elif opcao == 'X':
        print('\nSaindo...')
        break

    else: 
        print('\nOperação Inválida, por favor selecione novamente a operação desejada.' )

        print('=================================') 
