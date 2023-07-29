import textwrap

def menu():
    print("""
        ----------------------------------
        | Bem-vindo, o que deseja fazer? |
        ----------------------------------
        
        1 - Depósito

        2 - Saque

        3 - Extrato
        
        4 - Novo Usuário
        
        5 - Criar Conta
        
        6 - Listar Contas
        
        7 - Sair
        """)
    return int(input("Digite opção desejada: \t"))

def depositar(valor,balanco, extrato):
    if (valor > 0):
            balanco += valor
            extrato += f'Depósito: \t R${valor:,.2f}\n'
            print(f'Valor depositado foi de: \t R${valor:,.2f}')
    else:
            print('Não foi possível realizar essa operação')
    return balanco, extrato

def retirar(*, balanco, valor, extrato, limite, num_saque, limite_saque):
    
    excedeu_saldo = valor > balanco
    excedeu_limite = valor > limite
    excedeu_saque = num_saque >= limite_saque

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
    return balanco, extrato    

def mostrar_extrato(balanco, /, *, extrato):
      print('Extrato')
      print('Não há transição financeira' if not extrato else extrato)
      print(f'Balanço: R$ {balanco:,.2f}')
      return extrato

def cliente(usuarios):
    cpf = input("Informe seu CPF (apenas números): ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF")
        return
    
    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":nascimento, "cpf":cpf, "endereco":endereco })

    print("Cliente cadastrado com sucesso!")

def filtro_usuario(cpf, usuarios):
     usuario_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
     return usuario_filtrados[0] if usuario_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
        
    balanco = 0
    extrato = ""
    num_saque = 0
    LIMITE_SAQUES = 3
    limite = 500
    usuarios = []
    contas = []
    agencia = "0001"

    while True:

        print('')
        escolha = menu()
        print('')
        if(escolha == 1):
            valor = float(input("Você escolheu depósito, qual valor gostaria de depositar? \t "))

            balanco, extrato = depositar(valor, balanco, extrato)

        elif (escolha == 2):
            
            valor = float(input("Você escolheu retirada, qual valor gostaria de sacar? \t "))

            balanco, extrato = retirar(balanco=balanco, valor=valor, extrato=extrato, limite=limite, num_saque=num_saque, limite_saque=LIMITE_SAQUES)

        elif (escolha == 3):
            mostrar_extrato(balanco, extrato=extrato)

        elif (escolha == 4):
            cliente(usuarios)   

        elif (escolha == 5):
            numero_conta = len(contas)+1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif (escolha == 6):
            listar_contas(contas)

        elif (escolha == 7):
            break

        else:
            print('Não foi possível realizar operação')

main()
