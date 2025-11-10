def main():
    print("Hello! Welcome to the Financia Bank chatbot. Please enter your name and age.")
    name = input("Name: ")
    age = int(input("Age: "))
    print("Thank you.")
    prompt()

def prompt():
    bot_run = True
    while bot_run == True:
        user_input = input("What would you like assistance with?\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit")
        if user_input == "1":
            credit_cards()
        elif user_input == "2":
            interests()
        elif user_input == "3":
            account_creation()
        elif user_input == "4":
            print("Thank you for using the Financia chatbot. We hope to see you again soon!")
            bot_run = False
        else:
            user_input = input("Invalid input, please try again.\n 1. Cards and Account Types\n 2. Interest Calculator \n 3. How to Make a Bank Account with Us\n 4. Exit")

def credit_cards():
    

def interests():

def account_creation():

def exit():


main()