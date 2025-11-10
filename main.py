# TODO: Implement sign up and log in system into function login_system. - EK 10/15/25
name = ""
age = ""
###     FUNCTION DEFINITIONS     ###

def user_introduction(name, age): # This function lets the user input their name and age, which is then returned to the global variables for further use.
    print("Hello, I am Dora, welcome to the Financia Bank Chatbot! You may sign up to access advanced chatbot options.")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    print(f"Thank you for providing this information. You are {name} and you are {age} years old.")
    return name and age

def bot_prompt(): # This function prompts the user with 4 base choices. It only moves to advanced features once logged in.
    help_user = input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n")
    user_prompt(help_user)

username_signup = ""
user_signup_password = ""
def user_prompt(user_response): # This function displays different outputs for each of the four inputs. The first one is for signing up, the second is for logging in once you signed up, the third is to learn how to make a basic account with or without signing in, and the fourth is the exit.
    bot_run = True
    while bot_run:
        if (user_response=="1"):
            signup_system()
            print("Thanks for creating an account! Please log into your new account to access advanced options.")
            user_response = input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n")
        elif (user_response=="2"):
            login_system(username_signup, user_signup_password)
        elif (user_response=="3"):
            print("Connecting you to customer service...") # Tutorial response TBA for response #3.
            print("Connected.")
            account_creation_help()
            user_response = int(input("How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n"))
        elif (user_response=="4"):
            print("Thank you for checking out Financia Bank! We hope to see you soon!")
            bot_run = False
        else:
            user_response = input("Invalid input. How can I help you?\n 1. Sign up\n 2. Log In \n 3. How To Set Up An Account With Us \n 4. Exit\n")

def signup_system():
    username_signup = input("You seem to be a new user, please sign up with your username here: ")
    user_signup_password = input("Password: ")
    return username_signup and user_signup_password

def login_system(username_signup, user_signup_password): # This function lets the user log into their account and access the advanced features.
    if username_signup == "" and user_signup_password == "":
        print("You currently don't have an account. Please sign up to create one.")
        signup_system()
    username_login = username_signup
    userpass_login = user_signup_password
    print("Please log in.")
    username_correct = input("Username: ")
    userpass_correct = input("Password: ")
    if username_correct == username_login and userpass_correct == userpass_login:
            print(f"Welcome {username_correct} to your banking and financials account.\n Here are some advanced features you can use to navigate your account.")
            adv_features = int(input("1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))
            advanced_features(adv_features)
    elif username_correct != username_login and userpass_correct != userpass_login:
        print("Please try again.")
        username_correct = input("Username: ")
        userpass_correct = input("Password: ")
        

def advanced_features(feature_num): # This function uses the advanced features of the account and bot to show 4 more options. The first 
    bot_run = True
    while bot_run:
        if (feature_num==1):
            banking_info(age, account_amount)
            feature_num = int(input("1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))
        elif (feature_num==2):
            print("Here is a comparison of your account using both compound ")
        elif (feature_num==3):
            print("Connecting you to customer service: ") # Tutorial response TBA for response #3.
            feature_num = int(input("1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit"))
        elif (feature_num==4):
            print("Thank you for checking out Financia Bank! We hope to see you soon!")
            bot_run = False
        else:
            feature_num = input("Invalid input. 1. Bank Account Information\n 2. Financial Planning\n 3. Cards, Accounts, & Rates\n 4. Exit")

account_amount = 0
def banking_info(name, account_amount):
    print(f"Hello {name}, here is your banking information.")
    if account_amount == 0:
        account_amount = int(input("Please put in some money into your account: "))
        return account_amount
    else: 
        print(f"Current account amount: ${account_amount}")
    
def account_creation_help():
    print("It seems that you are trying to make an account, let's go through the steps\n 1. Go through the chatbot's basic entry. Select 'Sign Up' once you reach it.\n 2. Go through the sign up process.\n 3. All done! Now go back and log into your new account!")

def main():
    user_introduction(name, age)
    bot_prompt()

main()
