def bank_system():
    menu = """
    BEM VINDO AO BANK SYSTEM!
    ESCOLHA UMA DAS OPÇÕES ABAIXO:

    1 - DEPÓSITO
    2 - SAQUE
    3 - EXTRATO
    4 - SAIR
    """

    balance = 0
    WITHDRAW_LIMIT = 500
    statement = ""
    num_withdrawals = 0
    WITHDRAWAL_LIMIT = 3
    daily_withdrawals_sum = 0

    while True:
        print(menu)
        option = input("Digite a opção desejada: ")

        if option == "1":
            deposit = float(input("Digite o valor do depósito: "))
            if deposit > 0:
                balance += deposit
                statement += f"Depósito: R${deposit}\n"
                print(statement)
            else:
                print("Valor para depósito deve ser maior que zero.")

        elif option == "2":
            if num_withdrawals < WITHDRAWAL_LIMIT:
                withdrawal = float(input("Digite o valor do saque: "))
                if withdrawal > 0:
                    if withdrawal > balance:
                        print("Saldo insuficiente.")
                    elif daily_withdrawals_sum + withdrawal > WITHDRAW_LIMIT:
                        print(
                            f"O valor total dos saques não pode exceder R${WITHDRAW_LIMIT} por dia."
                        )
                    else:
                        balance -= withdrawal
                        statement += f"Saque: R${withdrawal}\n"
                        num_withdrawals += 1
                        daily_withdrawals_sum += withdrawal
            else:
                print("Você atingiu o limite de saques diários.")

        elif option == "3":
            print("\n=== EXTRATO ===")
            print(
                "Não foram realizadas movimentações hoje."
                if not statement
                else statement
            )
            print(f"O número de saques realizados hoje é: {num_withdrawals}")
            print(f"O saldo atual é: R${balance}")

        elif option == "4":
            print("Obrigado por utilizar o BANK SYSTEM!")
            break

        else:
            print("Opção inválida.")
