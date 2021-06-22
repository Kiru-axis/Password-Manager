# Cridential class
class Cridential:
    """
    Class that generates new instances of passwords
    """
    password_list = []
# 1. Initialisation
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password


#2. save acount password / save multiple account passwords
    def save_password(self):
        '''
        save_password method saves password objects into password_list
        '''
        Cridential.password_list.append(self)


 #3.Delete account password
    def delete_password(self):
        '''
        delete_password method deletes a saved password from the password_list
        '''
        
        Cridential.password_list.remove(self)

# 4 Search and display password
    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in a number and returns a contact that matches that number.
        '''
        for password in cls.password_list:
            if password.account == account:
                return password

# 5 if the account really exists
    @classmethod
    def password_exists(cls,account):
        for password in cls.password_list:
            if password.account == account:
                return True
        return False

# 6 Display all accounts
    @classmethod
    def display_all_passwords(cls):
        return cls.password_list


# User class 
class User:
    user_list = []
    """
    generates new instances of users to login
    """
    def __init__(self,user,login_password):
        self.user = user
        self.login_password = login_password


# Save user logins
    def save_user(self):
        """
        saves user logins in the user_list List which acts as our database
        """
        # User.user_list.append(self)
        User.user_list.append(self)


