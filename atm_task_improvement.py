import random

database = {1111111111: ["Salem", "Trey", "st@gm.com", "salsal", 5000]}


def begin():
    print("Welcome to UBA")
    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("Please choose option 1 or 2")


def register():
    print("****** REGISTER ******")
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    email = input("Enter your email address: \n")
    password = input("create a password: \n")
    initial_deposit = int(input("Enter your initial deposit: "))

    account_balance = initial_deposit
    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password, account_balance]

    print("Take note of your account number")
    print("Account Number: %d" % account_number)

    login()


def login():
    print("****** LOGIN ******")
    account_number = int(input("Account number: "))
    password = input("Password: ")

    if account_number in database and database[account_number][3] == password:
        bank_transactions(account_number)
    else:
        print("Account number or password is invalid")
        login_option = int(input("1 (Try again), Any number to exit: \n"))
        if login_option == 1:
            login()
        else:
            exit()


def bank_transactions(account_number):
    first_name = database[account_number][0]
    account_balance = database[account_number][4]

    print("Welcome %s " % first_name)
    print("These are the available options:")

    selected_option = int(
        input("1 (Withdrawal) , 2 (Deposit), 3 (Check Balance), 4 (Report Issue), any other number (exit): \n"))
    if 4 < selected_option < 1:
        exit()


    while 5 > selected_option > 0:
        if selected_option == 1:
            print("***** WITHDRAWAL *****")
            amount_to_withdraw = int(input("How much would you like to withdraw? \n"))
            if amount_to_withdraw > account_balance:
                print("Insufficient fund")
                print("Would you like to do anything else?")
                selected_option = int(
                    input(
                        "1 (Withdrawal) , 2 (Deposit), 3 (Check Balance), 4 (Report Issue), any other number (exit): \n"))
                if 4 < selected_option < 1:
                    exit()

            else:
                account_balance = account_balance - amount_to_withdraw
                print("take your cash!")
                print("Would you like to do anything else?")
                selected_option = int(
                    input(
                        "1 (Withdrawal) , 2 (Deposit), 3 (Check Balance), 4 (Report Issue), any other number (exit): \n"))
                if 4 < selected_option < 1:
                    exit()

        elif selected_option == 2:
            print("***** DEPOSIT *****")
            amount_to_deposit = int(input("How much would you like to deposit? \n"))
            account_balance = account_balance + amount_to_deposit
            print(account_balance)
            print("Would you like to do anything else?")
            selected_option = int(
                input("1 (Withdrawal) , 2 (Deposit), 3 (Check Balance), 4 (Report Issue), any other number (exit): \n"))
            if 4 < selected_option < 1:
                exit()

        elif selected_option == 3:
            print("***** CHECK BALANCE *****")
            print("Your account balance is: %d" % account_balance)
            print("Would you like to do anything else?")
            selected_option = int(
                input("1 (Withdrawal) , 2 (Deposit), 3 (Check Balance), 4 (Report Issue), any other number (exit): \n"))
            if 4 < selected_option < 1:
                exit()

        elif selected_option == 4:
            print("***** REPORT ISSUE *****")
            input("What issue would you like to report? \n")
            print("Thank you for contacting us!")
            print("Would you like to do anything else?")
            selected_option = int(
                input("1 (Withdrawal) , 2 (Deposit), 3 (Check Balance), 4 (Report Issue), any other number (exit): \n"))
            if 4 < selected_option < 1:
                exit()


def generate_account_number():
    account_number = random.randrange(1111111111, 9999999999)
    return account_number


begin()
