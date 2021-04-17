from datetime import date, datetime

database = {"Joanna": "password", "Lily": "love", "Kemi": "password", "Lekan": "password1", "Bimbo": "password2"}

account_balance = 5000

username = input("Enter your username \n")
if username in database:
    password = input("Enter your password \n")

    if database[username] == password:
        print("Welcome %s " % username)
        print("Today's date is %s" % date.today().strftime("%d/%m/%Y"))
        print("The time is %s" % datetime.now().strftime("%H:%M:%S"))
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash deposit")
        print("3. Complaint")

        selected_option = int(input("Please select an option:\n"))

        if selected_option == 1:
            print("You selected %s " % selected_option)
            amount_to_withdraw = int(input("How much would you like to withdraw? \n"))
            if amount_to_withdraw > account_balance:
                print("Insufficient fund")
            else:
                account_balance = account_balance - amount_to_withdraw
                print("take your cash!")

        elif selected_option == 2:
            print("You selected %s " % selected_option)
            amount_to_deposit = int(input("How much would you like to deposit? \n"))
            account_balance = account_balance + amount_to_deposit
            print(account_balance)

        elif selected_option == 3:
            print("You selected %s" % selected_option)
            input("What issue would you like to report? \n")
            print("Thank you for contacting us!")

    else:
        print("You have entered an incorrect password")

else:
    print("The username isn't in the database")





