import unittest
from password import Cridential
from password import User

# Unittest for cridental
class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the paswords class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_passwords = Cridential("Gmail","Pinky","github55.pie")
        # behaviour for user class
        self.new_user = User("Testt","pass")

# Test one:Initialisation   
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_passwords.account,"Gmail")
        self.assertEqual(self.new_passwords.username,"Pinky")
        self.assertEqual(self.new_passwords.password,"github55.pie")


# Test 2: Saving Accounts in the password.txt file    
    def test_save_password(self):
        '''
        test_save_password test case to test if the Account object is saved into
        the Cridential list
        '''
        self.new_passwords.save_password() #add new account

        self.assertEqual(len(Cridential.password_list),1) #checking if the length of the list changes
    

# Test 2.1: Saving multiple Accounts in the password.txt file

    def test_save_multiple_password(self):
        '''
        test_save_multiple_password to check if we can save multiple Account
        objects to our password_list
        '''
        self.new_passwords.save_password() #add new account

        test_password = Cridential("Github","Venus","gitty")
        test_password.save_password() #save
        self.assertEqual(len(Cridential.password_list),2)


# The tearDown method will clean up all the test we make and only add real password
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        This helps us get accurate test results every time a new test case.
        '''
        Cridential.password_list = []
        # Teardown for user
        User.user_list = []

# Test 3: Delete Account 

    def test_delete_password(self):
        '''
        test_delete_password to test if we can remove an Account from our password list
        '''
        self.new_passwords.save_password()
        test_password = Cridential("Facebook","Pluto","turtles") #Add these account to delete it and confirm our delete test

        test_password.save_password()
        self.new_passwords.delete_password() #removing from the list
        self.assertEqual(len(Cridential.password_list),1)


#Test 4: Search Account and display passwords
    def find_password_by_account(self):
        '''
        test to check if we can find password by account or username
        '''
        self.new_passwords.save_password()
        test_password = Cridential("Github","Venus","gitty")
        test_password.save_password()

        found_password = Cridential.find_password_by_account("Github")
        self.assertEqual(found_password.password, test_password.password)


# 5. Confirm if account exists
    def test_password_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_passwords.save_password()
        test_password = Cridential("Github","Venus","gitty")

        test_password.save_password()
        password_exists = Cridential.password_exists("Github")

        self.assertTrue(password_exists)


# 6. Display all contacts
    def test_display_all_passwords(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(Cridential.display_all_passwords(),Cridential.password_list)


# unittest for User
# 1. Test initialization
    def test_initialisation(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user, "Testt")
        self.assertEqual(self.new_user.login_password, "pass")


# 2. Save user logins
    def test_save_user(self):
        """
        test_save_user test case to test if the contact object is saved into
        the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == "__main__":
    unittest.main()
