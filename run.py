#!/usr/bin/env python3.8
# before running the program on terminal Type: chmod +x run.py to gain access

from password import Cridential,User
import random
import string

# User-----------------------------------------
# 1. Creating created_user_password details
def save_user(login):
    """
    Function to save created_username created_user_password details
    """
    login.save_password()
    return User

# Cridentials----------------------------------------------------
# 1. Creating an account 
def create_password(account,username,password):
    '''
    Function to create a new Account
    '''
    new_password = Cridential(account,username,password)
    return new_password

# 1. Save the account
def save_password(account):
    '''
    Function to save Account
    '''
    account.save_password()


# 3. Delete account
def del_password(account):
    '''
    Function to delete an account
    '''
    account.delete_password()

# 4. Finding account
def find_account(account):
    '''
    Function that finds password by account and returns the account
    '''
    return Cridential.find_by_account(account)


# Check if an account exists
def check_existing_password(account):
    """
    Function that returs all the accounts
    """
    return Cridential.password_exists(account)

# Display all password and account
def display_password():
    """
    Function returns all accounts and their passwords
    """
    return Cridential.display_all_passwords()


# Main function
def main():
    while True:
        print("Welcome to your password manager.")
        print("\n")
        # User Authentication first
        print(
        """Use the following shortcodes to navigate these app : 
        new = new Password manager account.
        log = log in to your account.
        exit = quit the account creation program.
        """)
        shortcode = input(">>>").lower()
        print("\n")

        if shortcode == "new":
            print("Create Username : \n")
            created_username = input(">>>")

            print("Create a secure password: \n")
            created_user_password = input(">>>")

            print("Confirm your password: \n")
            confirm_password = input(">>>")

            # check whether the created_user_password and created_user_password confirmation match
            while confirm_password != created_user_password:
                print("Login confirmation did not match!! \n")
                print("Enter your created_user_password \n")
                created_user_password = input(">>>")
                print("Confirm your password: \n")
                confirm_password = input(">>>")
            else:
                print(f"Congratulations {created_username}! Account created")
                print("\n")
                print("Proceed to login")
                print("Enter your name \n")
                entered_username = input(">>>")
                print("Enter your password")
                entered_password = input(">>>")

            while entered_username != created_username or entered_password != created_user_password:
                print("Invalid username or password")
                print("User: \n")
                exit()
            else:
                print(f"Welcome {created_username} to your account")
                print("\n")

                while True:
            # Save and store password______________________________________________________________________________________________
                    print(
                        """Use the short codes :
                        cre = new account password.
                        disp = display account details.
                        find = find account.
                        del = delete account.
                        quit = exit.
                        """)
                    print("\n")

                    short_codes = input(">>>").lower()

                    # Conditions
                    if short_codes == "cre":
                        print("New account to be created")
                        print("\n")
                        print("-"*30)

                        print("Account/Website")
                        print("-"*30)
                        print("\n")
                        account = input(">>>")
                        print("__"*10)
                        print("\n")
            
                        print("Username")
                        print("-"*30)
                        print("\n")
                        username = input(">>>")
                        print("__"*10)
                    
                    #    Giving the created_username choice on password. Either generate or input own
                        print("Cridential: Type pass - to input your own password or gen -to auto generate \t\n")
                        print("-"*30)
                        pass_choice = input(">>>").lower()

                        if pass_choice == "pass":
                            print("Key in the password")
                            print("-"*30)
                            password = input(">>>")
                        elif pass_choice == "gen":
                            digits = int(input('How many characters do you want for your password ?: \n'))
                            password = ""
                            for i in range(digits):
                                char = random.choice(string.ascii_letters)
                                password += char

                        save_password(create_password(account, username, password))

                        # file to store the password
                        folder = open("password.txt", "a")
                        folder.write(f"{account}---{username}---{password} \r\n")
                        folder.close()

                        print("\t\n")
                        print(f"Accounts Created:\n Account:{account}\n Username:{username}\n Passwaord:{password}\n")
                        print("\n")


            # Display_____________________________________________________________________________________

                    elif short_codes == "disp":
                        if display_password():
                            print("Here is the list of all your accounts and their related information")

                            for password in display_password():
                                print("\n")
                                print(f"  {password.account} | {password.username}  | {password.password}")
                        else:
                            print("\n")
                            print("Archive empty")

            # Find the list_____________________________________________________________________________________

                    elif short_codes == "find":
                        print("Enter the account for which you want to see the details")
                        search_account = input(">>>")
                        if check_existing_password(search_account):
                            search_account = find_account(search_account)

                            print("-"*20)
                            print(f"Account..{search_account.account}")
                            print(f"Username..{search_account.username}")
                            print(f"Cridential..{search_account.password}")
                            print("__"*20)

                        else:
                            print("Searched account is not in the archive")
            # Delete Account_____________________________________________________________________________________
                    elif short_codes == "del":
                        print("Enter the account for which you want to delete :\n")
                        delete_account = input(">>>")

                        if check_existing_password(delete_account):
                            found_delete = find_account(delete_account)
                            print("\n")
                            print(f" {found_delete.account} {found_delete.username} {found_delete.password} deleted")
                            del_password(found_delete)
                            print("\n")
                        else:
                            print("Account selected is not in the archive")


            # Exiting the program_________________________________________________________________________________________________
                    elif short_codes == "quit":
                        print("Goodbye. Have a nice day")
                        break


        # login to your account
        elif shortcode == "log":
            print("Welcome")
            print("Enter created_username \n")
            default_user = input(">>>")

            print(f"Enter created_username password: \n")
            default_login = input("")
            print(f"\n")

            while default_user != "testuser" or default_login != "1000":
                print("Wrong username or password. Account name and password doesnt exist. Please enter valid cridentials ")
                print("Enter username: \n")
                default_user = input(">>>")
                print(f"Enter password: \n")
                default_login = input("")
                print("\n")
            else:
                print("Login successful")
                print("\n")
                if "Login successful":
                    return exit()
        elif shortcode == "exit":
            print("Bye!")
            exit()
        else:
            print("Enter a valid code to create account...or just proceed to saving your accounts though not secure")
            print("\n")
            break

if __name__ == '__main__':

    main()