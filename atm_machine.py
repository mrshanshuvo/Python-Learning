def quick_cash(balance):
    print("1. 200\t\t2. 500\t\t3. 1000")
    print("4. 2000\t\t5. 5000\t\t6. 10000")

    while True:
        a = int(input("ENTER: "))
        if (a == 1):
            balance -= 200
            print("200 TK Withdrawn Successfully!")
            print(f'New Balance is {balance} TK')
            return balance
        elif (a == 2):
            balance -= 500
            print("500 TK Withdrawn Successfully!")
            print(f'New Balance is {balance} TK')
            break
        elif (a == 3):
            balance -= 1000
            print("1000 TK Withdrawn Successfully!")
            print(f'New Balance is {balance} TK')
            break
        elif (a == 4):
            balance -= 2000
            print("2000 TK Withdrawn Successfully!")
            print(f'New Balance is {balance} TK')
            break
        elif (a == 5):
            balance -= 5000
            print("5000 TK Withdrawn Successfully!")
            print(f'New Balance is {balance} TK')
            break
        elif (a == 6):
            balance -= 10000
            print("10000 TK Withdrawn Successfully!")
            print(f'New Balance is {balance} TK')
            break
        else:
            print("INVALID CHOICE!! Please try again !!")


def withdraw(balance):
    print("Withdraw")


def deposit(balance):
    print("Deposit")


def mini_statement(balance):
    print("Mini Statement")


def balance_enquiry(balance):
    print("Balance Enquiry")


def change_pin():
    print("Change PIN")


def user_main_menu(balance):

    while True:
        print("\n\n1. Quick Cash\t\t\t2. Withdraw")
        print("3. Deposit\t\t\t4. Mini Statement")
        print("5. Balance Enquiry\t\t6. Change PIN")
        print("7. Exit\n")
        option_ch = int(input("Enter Your Choice: "))
        if (option_ch == 1):
            return quick_cash(balance)
        elif (option_ch == 2):
            withdraw(balance)
        elif (option_ch == 3):
            deposit(balance)
        elif (option_ch == 4):
            mini_statement(balance)
        elif (option_ch == 5):
            balance_enquiry(balance)
        elif (option_ch == 6):
            change_pin()
        elif (option_ch == 7):
            print(
                "You have selected to end your seassion here!\nThank you.Dear, Customer!")
            break
        else:
            print("INVALID CHOICE!! \nPlease select your option between (1-6) !!")


def user_login_interface(balance):
    print("---------------------------------------------")
    print("---------------WELCOME DEAR,-----------------")
    print("----------------------------CUSTOMER---------")
    print("---------------------------------------------")
    print("================= Log In ====================\n\n")

    while True:
        user_acc_num = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        if (user_acc_num == 221002038):
            while True:
                user_pin_num = int(input("ENTER YOUR PIN: "))
                if (user_pin_num == 64345):
                    return user_main_menu(balance)
                else:
                    print(
                        "INVALID PIN NUMBER !!\nPlease re-enter your PIN number !!\n\n")
            break
        else:
            print("INVALID ACCOUNT NUMBER !!\nPlease Re-enter your Account Number !!\n\n")


def admin_login_interface():
    b = 5


balance = 40000
print("\n\n----------------------------------------")
print("---------ATM MANAGEMENT SYSTEM----------")
print("----------------------------------------\n\n")
print("1. USER LOGIN")
print("2. ADMIN LOGIN")

user_ch = int(input())

if (user_ch == 1):
    user_login_interface(balance)
elif (user_ch == 2):
    admin_login_interface()
