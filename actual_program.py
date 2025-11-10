def main():
    print("Hello! Welcome to the Financia Bank chatbot. Please enter your name and age.")
    name = input("Name: ")
    age = int(input("Age: "))
    print("Thank you.")
    prompt(name,age)

def prompt(name,age):
    bot_run = True
    while bot_run == True:
        user_input = input("What would you like assistance with?\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit ")
        if user_input == "1":
            credit_cards()
            user_input = input("What would you like assistance with?\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit ")
        elif user_input == "2":
            interests(name,age)
            user_input = input("What would you like assistance with?\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit ")
        elif user_input == "3":
            account_creation()
            user_input = input("What would you like assistance with?\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit ")
        elif user_input == "4":
            print("Thank you for using the Financia chatbot. We hope to see you again soon!")
            bot_run = False
        else:
            user_input = input("Invalid input, please try again.\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit ")

def credit_cards():
    ask_user = input("Would you like to look at 1. Cards or 2. Accounts?")
    if ask_user == "1":
        print("Here are some cards Financia Bank can offer:\n 1. Rewards Cards - These include cash back (flat-rate, tiered, or rotating), point-based, travel, & co-branded credit cards.\n 2. Low Interest Cards - These cards include 0% Intro APR and balance transfer credit cards.\n 3. Secured Credit Cards - These cards can help you to improve your credit score.\n 4. Business Credit Cards - Great for business owners due to expense tracking and higher credit limits.")
        print("We also offer debit cards for other needs.")
        print("Remember to ask your local Financia Bank banker to find what is right for you.")
        print("-----------------------------------------------")
        print("")
    elif ask_user == "2":
        print("Financia Bank offers 4 different accounts: \n 1. Checking Account - These can help you store your money securely.\n 2. Savings Account - These can be for short-term goals or act as emergency funds.\n 3. Certificate of Deposit Account - These provde higher APYs than the traditional savings account.\n 4. Money Market Account - This account is a type of savings account that helps you earn interest.")
        print("Remember to ask your local Financia Bank banker to find what is right for you.")
        print("-----------------------------------------------")
        print("")
    else:
        ask_user = input("Invalid input, please try again.\n Would you like to look at 1. Cards or 2. Accounts?")

def interests(name,age):
    calculations = input("Would you like a 1. Compound Interest Calculator or 2. Simple Interest Calculator? ")
    if calculations == "1":
        rate = float(input("What rate would you like to calculate? "))
        year = int(input("At what year would you like to withdraw the interest money? "))
        principal = float(input("How much money would you like to add as your principal? "))
        c_interest = round((principal *(1+rate) ** (year-2025)),2)
        final_age = (year-(2025-age))
        print(f"{name}, by the time you are {final_age}, you will have ${c_interest} in your account via compound interest.")
        print("-----------------------------------------------")
        print("")
    elif calculations == "2":
        rate = float(input("What rate would you like to calculate? "))
        year = int(input("At what year would you like to withdraw the interest money? "))
        principal = float(input("How much money would you like to add as your principal? "))
        c_interest = round((principal * rate * (year-2025)), 2)
        final_age = (year-(2025-age))
        print(f"{name}, by the time you are {final_age}, you will have ${c_interest} in your account via simple interest.")
        print("-----------------------------------------------")
        print("")
    else:
        calculations = input("Invalid input, please try again. Would you like a 1. Compound Interest Calculator or 2. Simple Interest Calculator?")

def account_creation():
    print("Connecting you to Customer Service...")
    print("Connected!")
    print("Welcome to Financia Bank! Here's how you can create an account with us.\n In-person\n 1. Head on over to your local Financia Bank.\n 2. Meet one of our employees or bankers to find what options are right for you.\n 3. Create your intial account with the information you have received. You may change these later.\n 4. You have now a bank account with Financia Bank!\n Online\n 1. Head over to the Financia Bank website fianciasbank.com.\n 2. Check out different plans for what you want your account to be. You may contact our customer service at any time to connect you with a banker.\n 3. Create your account with the necessary information.\n 4. You have now made a bank account with Financia Bank!")
    print("-----------------------------------------------")
    print("")

main()