# testClient.py
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGilder
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest
from client import Client
from customerInfo import Name, Phone, Address, Password

# for testing user input
from unittest.mock import patch

# for password hash testing
import bcrypt

# ignore run tests in alphabetical order
unittest.TestLoader.sortTestMethodsUsing = None


""" Define test TestClient class by extending the unittest.TestCase class"""

class TestClient(unittest.TestCase):
    # Base client data for testing\
    CLIENT_ONE_FIRSTNAME = "Cole"
    CLIENT_ONE_LASTNAME = "Fuhrman"
    CLIENT_ONE_PHONENUM = "8047292516"
    CLIENT_ONE_ADDRESS = [("1234", "Smith St"), "Ashland", "VA"]
    CLIENT_ONE_PASSWORD = "abcd1234"

    # for testing password hashing
    salt = bcrypt.gensalt()
    print(salt)
    bytes = CLIENT_ONE_PASSWORD.encode('utf-8')
    hashedPass = bcrypt.hashpw(bytes, salt)
    CLIENT_ONE_HASH = hashedPass


    # The setup method creates a client
    def setUp(self):
        
        # setup client
        self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME,TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)        
        
        # test to ensure name works correctly (len 1-25, no special chars) / correct type
        invalidFirstNames = ["Dilllllllllllllllllllllllllllllllon", "", "D1ll@n", 5]

        # test to ensure name works correctly (len 1-25, no special chars)
        invalidLastNames = ["VaaaaaaaaaaaaaaaaaaaanGildddddddddddddddder", "", "V@nG1ld3r", 5]

        # test to ensure phone works correctly (no 0 as first num, not too long + no special chars) / correct type
        invalidPhones = ["091020929392s", "91020929392s", 50]

        # test to ensure address works correctly (must be python list length 3 + must be correct types + must be correct lengths/characters + in list of correct states)
        invalidAddresss = [(1234, 1234), "Ashland", "VA"]

        # test to ensure account type works correctly (must be "Checking" or "Savings")
        invalidAccountTypes = ["checking", "savings", 30]


        # test to ensure password works correctly (must be 8-16 chars in length, must not contain invalid chars + correct type
        invalidPasswordsAssertion = ["pass", "passssssssssssssssss", 30]
        invalidPasswordsException = ["password/", "password<", "password>", "password|", "password "]



        # test invalid first names
        for i in invalidFirstNames:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client4 = Client(i, "VanGilder", TestClient.CLIENT_ONE_PHONENUM,TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)
        
        # test invalid last names
        for i in invalidLastNames:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client4 = Client("Dillon", i, TestClient.CLIENT_ONE_PHONENUM,
                                      TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)

        # test invalid phones
        for i in invalidPhones:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client4 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME,i, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)

        # test invalid addresses
        for i in invalidAddresss:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client4 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME,TestClient.CLIENT_ONE_PHONENUM, i, "Checking", TestClient.CLIENT_ONE_PASSWORD)

        # test invalid account types
        for i in invalidAccountTypes:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client4 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME,TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, i, TestClient.CLIENT_ONE_PASSWORD)

        # test invalid passwords
        for i in invalidPasswordsAssertion:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):self.client4 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME,TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", i)
            
        for i in invalidPasswordsException:
            # test to ensure excpetion occurs 
            with self.assertRaises(Exception): self.client4 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME,TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", i)







    # The test_constructor method tests the constructor
    def testConstructor(self):

        # test regular constructor function and acessor methods
        self.assertEqual(self.client1.getFirstName(),TestClient.CLIENT_ONE_FIRSTNAME)

        self.assertEqual(self.client1.getLastName(),TestClient.CLIENT_ONE_LASTNAME)

        self.assertEqual(self.client1.getPhone(), Phone(TestClient.CLIENT_ONE_PHONENUM))

        self.assertEqual(str(self.client1.getAddress()),"1234 Smith St, Ashland, VA")

        self.assertEqual(self.client1.getClientNumber(), 100)


        


        # Test to ensure the client has at least one account upon creation

        accountList = self.client1._getAccounts()

        self.assertEqual(accountList[0].getAccountType(), "Checking")

        self.assertEqual(len(accountList), 1)



        # Test to ensure that client is handling bank account numbers

        self.client1.openAccount("Checking")
        self.assertEqual(accountList[1].getAccountNumber(), 1001)


    # test password has been hashed /not stored in plaintext
    def testPasswordHash(self):

        # test password creation
        self.client2 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)

        # test password type is bytes
        self.assertIsInstance(self.client2._getPassword(), bytes)
        stored = self.client2._getPassword()

        # test password print is not in plain text
        self.assertNotEqual(stored, self.CLIENT_ONE_PASSWORD)

        # check salt added (length 60)
        #self.assertEqual(len(str(stored)), 60)

        # test password is hashed

        # change to string
        temp = stored.decode('utf-8')

        # grab salt
        salt = ""
        for i in range(7, 29):
            salt = salt + temp[i]
            
        print(salt)

        # hash original password
        print(temp)
        password = TestClient.CLIENT_ONE_PASSWORD.encode('utf-8')
        hashedPass = bcrypt.hashpw(password, salt.encode('utf-8'))

        # compare
        self.assertEqual(bcrypt.checkpw(hashedPass, self.CLIENT_ONE_HASH), True)


    # test opening and closing a bank account



    def testOpenAndCloseBankAccount(self):
        self.client1.openAccount("Savings")
        accountList = self.client1._getAccounts()

        # Test to see if new account was opened
        self.assertEqual(accountList[1].getAccountType(), "Savings")
        self.assertEqual(accountList[0].getAccountType(), "Checking")
        self.assertEqual(len(accountList), 2)



        # make a deposit to the checking account and then attempt to close the account
        accountList[0].deposit(20.00)
        closeAccountBooleanValue = self.client1.closeAccount(accountList[0])


        # Test to see that account was close, funds were withdrawn, and correct account was removed from the list
        self.assertEqual(closeAccountBooleanValue, True)
        accountList = self.client1._getAccounts()
        self.assertEqual(len(accountList), 1)
        self.assertEqual(accountList[0].getAccountType(), "Savings")


        # Test to ensure client can not close account, if they only have one account

        closeAccountBooleanValue = self.client1.closeAccount(accountList[0])

        self.assertEqual(closeAccountBooleanValue, False)



    @patch('testClient.get_input', return_value=CLIENT_ONE_PASSWORD)

    # test changing client password

    def testChangePassword(self, input):



        # ** NOT DONE



        # test change password method

        self.client1.changePassword("fake_old_pass")



        # assume error

        self.client1.changePassword()



        # test to ensure new password works correctly (must be 8-16 chars in length, must not contain invalid chars + correct type

        invalidPasswords = ["pass", "passssssssssssssssss", "password/",

                            "password\\", "password<", "password>", "password|", "password ", 30]



        # test invalid passwords

        for i in invalidPasswords:

            # test to ensure asserts occur

            with self.assertRaises(AssertionError):

                pass



    # to patch: for getting user input

    def _get_input(text):

        return input(text)



    # test equal method

    def testEqMethod(self):



        # ensure are equal

        self.assertEqual(self.client1 == self.client1)





if __name__ == '__main__':

    unittest.main()

