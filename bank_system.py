def menu():
    menu_text = """\n
    ********** PYTHON BANK **********
    ********** Selecione uma opção: **********
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas
    [7]\tSair
    => """
    return input(menu_text)


def deposit(balance, amount, statement):
    if amount > 0:
        balance += amount
        statement += f"Deposito:\tR$ {amount:.2f}\n"
        print("\n********** Depósito realizado com sucesso! **********")
    else:
        print("\n********** O valor informado é inválido. **********")

    return balance, statement


def withdraw(
    balance,
    amount,
    statement,
    withdraw_limit,
    num_withdrawals,
    withdrawal_limit,
    daily_withdrawals_sum,
):

    if amount > balance:
        print("\n********** Saldo insuficiente! **********")

    elif daily_withdrawals_sum + amount > withdraw_limit:
        print(
            "\n********** Valor do saque acima do limite diário permitido! **********"
        )

    elif num_withdrawals >= withdrawal_limit:
        print("\n********** Limite de saques diários atingido! **********")

    elif amount > 0:
        balance -= amount
        statement += f"Saque:\t\tR$ {amount:.2f}\n"
        num_withdrawals += 1
        daily_withdrawals_sum += amount
        print("\n********** Saque realizado com sucesso! **********")

    else:
        print("\n********** O valor informado é inválido. **********")

    return balance, statement, num_withdrawals, daily_withdrawals_sum


def display_statement(balance, statement):
    print("\n********** Extrato **********")
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("********** Fim do Extrato **********\n")


def create_user(users):
    cpf = input("Informe o CPF (apenas números): ")
    user = filter_user(cpf, users)

    if user:
        print("\n********** Usuário já cadastrado! **********")
        return

    name = input("Informe o nome completo: ")
    date_of_birth = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço: ")

    users.append(
        {
            "nome": name,
            "data_de_nascimento": date_of_birth,
            "cpf": cpf,
            "endereco": address,
        }
    )

    print("********** Usuário cadastrado com sucesso! **********")


def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None


def create_account(bank_branch, account_number, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filter_user(cpf, users)

    if user:
        print("\n********** Usuário encontrado! Conta criada com sucesso! **********")
        return {"agencia": bank_branch, "numero_conta": account_number, "usuario": user}

    print(
        "\n********** Usuário não encontrado! Utilize a opção '4' para cadastrar um novo usuário. **********"
    )


def list_accounts(accounts):
    for account in accounts:
        bank_account = f"""\
            Número da conta:\t{account['numero_conta']}
            Usuário:\t\t{account['usuario']['nome']}
        """
        print("*" * 100)
        print(bank_account)
        print(accounts)


def main():
    WITHDRAW_LIMIT = 500
    WITHDRAWAL_LIMIT = 3
    BANK_BRANCH = "0001"

    balance = 0
    statement = ""
    num_withdrawals = 0
    daily_withdrawals_sum = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == str(1):
            amount = float(input("Informe o valor do depósito: "))
            balance, statement = deposit(balance, amount, statement)

        elif option == str(2):
            amount = float(input("Informe o valor do saque: "))
            balance, statement, num_withdrawals, daily_withdrawals_sum = withdraw(
                balance,
                amount,
                statement,
                WITHDRAW_LIMIT,
                num_withdrawals,
                WITHDRAWAL_LIMIT,
                daily_withdrawals_sum,
            )

        elif option == str(3):
            display_statement(balance, statement)

        elif option == str(4):
            create_user(users)

        elif option == str(5):
            account_number = len(accounts) + 1
            account = create_account(BANK_BRANCH, str(account_number), users)

            if account:
                accounts.append(account)

        elif option == str(6):
            list_accounts(accounts)

        elif option == str(7):
            break

        else:
            print("Operação inválida. Selecione uma opção válida do menu (1 a 7).")
