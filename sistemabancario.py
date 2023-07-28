print("""
    ----------------------------------
    | Bem-vindo, o que deseja fazer? |
    ----------------------------------
      
      1 - Depósito

      2 - Saque

      3 - Extrato
      """)

balanco = 0
extrato = ""
num_saque = 0
LIMITE_SAQUE = 3
limite = 500

while True:
    print('')
    escolha = int(input("Digite opção desejada: \t"))
    print('')
    if(escolha == 1):
        valor = float(input("Você escolheu depósito, qual valor gostaria de depositar? \t "))
            
        print(f'Valor depositado foi de: \t R${valor:,.2f}')
        if (valor > 0):
            balanco += valor
            extrato += f'Depósito: \t R${valor:,.2f}\n'
            
        else:
                  print('Não foi possível realizar essa operação')
    elif (escolha == 2):
        
        valor = float(input("Você escolheu retirada, qual valor gostaria de sacar? \t "))
        
        excedeu_saldo = valor > balanco
        excedeu_limite = valor > limite
        excedeu_saque = num_saque >= LIMITE_SAQUE

        if excedeu_saldo:
             print('Não há saldo suficiente, operação não realizada')
        elif excedeu_limite:
             print('Valor diário de saque foi atingido, operação não realizada')
        elif excedeu_saque:
             print('Limite de saques diários atingido, operação não realizada')
        elif valor > 0:
            print(f'Valor retirado foi de: \t R${valor:,.2f}')
            balanco -= valor
            extrato += f'Retirada \t R${valor:,.2f}\n'
            num_saque += 1
        else:
             print('Valor informado inválido!')

    elif (escolha == 3):
            print('Extrato')
            print('Não há transição financeira' if not extrato else extrato)
            print(f'Balanço: R$ {balanco:,.2f}')

    else:
        print('Não foi possível realizar operação')
