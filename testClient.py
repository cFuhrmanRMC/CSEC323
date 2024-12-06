# testClient.py
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGilder
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest
from client import Client

# for testing user input
from unittest.mock import patch

# for password hash testing
import bcrypt

# ignore run tests in alphabetical order
unittest.TestLoader.sortTestMethodsUsing = None

""" Define test TestClient class by extending the unittest.TestCase class"""

class TestClient(unittest.TestCase):
    
    # Base client data for testing
    CLIENT_ONE_FIRSTNAME = "Cole"
    CLIENT_ONE_LASTNAME = "Fuhrman"
    CLIENT_ONE_PHONENUM = "8047292516"
    CLIENT_ONE_ADDRESS = [("1234", "Smith St"), "Ashland", "VA"]
    CLIENT_ONE_PASSWORD = "DO_NOT_STORE_IN_PLAINTEXT!"

    # for testing password hashing
    salt = bcrypt.gensalt()
    bytes = CLIENT_ONE_PASSWORD.encode('utf-8')
    hashedPass = bcrypt.hashpw(bytes, salt)
    CLIENT_ONE_HASH = hashedPass


    
    # The setup method creates a client
    def setUp(self):

        # test to ensure name works correctly (len 1-25, no special chars) / correct type
        invalidFirstNames = ["Dilllllllllllllllllllllllllllllllon", "", "D1ll@n", 5]

        # test to ensure name works correctly (len 1-25, no special chars)
        invalidLastNames = ["VaaaaaaaaaaaaaaaaaaaanGildddddddddder", "", "V@nG1ld3r", 5]

        # test to ensure phone works correctly (no 0 as first num, not too long + no special chars) / correct type
        invalidPhones = ["091020929392s","91020929392s", 50]
    
        # test to ensure address works correctly (must be python list length 3 + must be correct types + must be correct lengths/characters + in list of correct states)
        invalidAddresss = [[("1234", "Smith St"), "Ashland", "PA", "VA"], ["1234 Smith St", "Ashland", "VA"], 
                           [("1234", ""), "Ashland", "VA"], [("1234", "Smith Sttttttttttttttt"), "Ashland", "VA"], [("1234", 30), "Ashland", "VA"],
                           [(1234, "Smith St"), "Ashland", "VA"], [("", "Smith St"), "Ashland", "VA"], [("12333333333334", "Smith St"), "Ashland", "VA"],
                           [("1234", "Smith St%"), "Ashland", "VA"], [("%", "Smith St"), "Ashland", "VA"],
                           [("1234", "Smith St"), 30, "VA"] [("1234", "Smith St"), "", "VA"], [("1234", "Smith St"), "Ashlandddddddddddddddddddddddd", "VA"], 
                           [("1234", "Smith St"), "Ashland%", "VA"], 
                           [("1234", "Smith St"), "Ashland", "PA"], [("1234", "Smith St"), "Ashland", ""], [("1234", "Smith St"), "Ashland", 30]
                           ]
    
        # test to ensure account type works correctly (must be "Checking" or "Savings")
        invalidAccountTypes = ["checking", "savings", 30]

        # test to ensure password works correctly (must be 8-16 chars in length, must not contain invalid chars + correct type
        invalidPasswords = ["pass", "passssssssssssssssss", "password/", "password\\", "password<", "password>","password|", "password ", 30]


        # test invalid first names 
        for i in invalidFirstNames:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client1 = Client(i, "VanGilder", TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)
                

        # test invalid last names
        for i in invalidLastNames:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                 self.client1 = Client("Dillon", i, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)
    
        # test invalid phones
        for i in invalidPhones:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                 self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, i, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)
        
        # test invalid addresses
        for i in invalidAddresss:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, i, "Checking", TestClient.CLIENT_ONE_PASSWORD)
    
        # test invalid account types
        for i in invalidAccountTypes:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, i, TestClient.CLIENT_ONE_PASSWORD)
    
        # test invalid passwords
        for i in invalidPasswords:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", i)

        #setup client
        self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)

    # The test_constructor method tests the constructor 
    def testConstructor(self):

        # test regular constructor function and acessor methods
        self.assertEqual(self.client1.getFirstName(), TestClient.CLIENT_ONE_FIRSTNAME)
        self.assertEqual(self.client1.getLastName(), TestClient.CLIENT_ONE_LASTNAME)        
        self.assertEqual(self.client1.getPhone(), TestClient.CLIENT_ONE_PHONENUM)
        self.assertEqual(str(self.client1.getAddress()), "1234 Smith St, Ashland, VA")
        self.assertEqual(self.client1.getClientNumber(), 100)

        # test password hashing
        salt = bcrypt.gensalt()
        bytes = TestClient.CLIENT_ONE_PASSWORD.encode('utf-8')
        hashedPass = bcrypt.hashpw(bytes, salt)

        self.assertEqual(self.client1._getPassword, hashedPass)
        
        # Test to ensure the client has at least one account upon creation
        accountList = self.client1._getAccounts()
        self.assertEqual(accountList[0].getAccountType(), "Checking")
        self.assertEqual(len(accountList), 1)
        
        # Test to ensure that client is handling bank account numbers 
        self.client1.openAccount("Checking")
        self.assertEqual(accountList[1].getAccountNumber(), 1001)
    
    # test password has been hashed /not stored in plaintext
    def testPasswordHash(self):

        #** NOT DONE

        # test password creation
        self.client2 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)

        # test password type is bytes
        self.assertIsInstance(self.client2._getPassword(), bytes)
        stored = self.client2._getPassword()

        # test password print is not in plain text
        self.assertNotEqual(bcrypt.checkpw(stored, self.CLIENT_ONE_PASSWORD), True)

        # check salt added (length 60)
        self.assertEqual(len(str(stored)), 60)

        # test password is hashed past salt (cannot test, is randomly generated)
        
        hash = ""
        for i in range(24, len(stored)):
            hash = hash + stored[i]

        self.assertEqual(hash, self.CLIENT_ONE_HASH[24:60])

        # test password comparison
        self.assertNotEqual(self.client2._getPassword() == self.CLIENT_ONE_PASSWORD)

    # test changing client data
    def testChangeInfo(self):
    	
    	# new client
        self.client3 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking", TestClient.CLIENT_ONE_PASSWORD)

        # test mutator methods
        
        # test to ensure name works correctly (len 1-25, no special chars) / correct type
        invalidFirstNames = ["Dilllllllllllllllllllllllllllllllon", "", "D1ll@n", 5]

        # test to ensure name works correctly (len 1-25, no special chars)
        invalidLastNames = ["VaaaaaaaaaaaaaaaaaaaanGildddddddddder", "", "V@nG1ld3r", 5]

        # test to ensure phone works correctly (no 0 as first num, not too long + no special chars) / correct type
        invalidPhones = ["091020929392s","91020929392s", 50]
    
        # test to ensure address works correctly (must be python list length 3 + must be correct types + must be correct lengths/characters + in list of correct states)
        invalidAddresss = [[("1234", "Smith St"), "Ashland", "PA", "VA"], ["1234 Smith St", "Ashland", "VA"], 
                           [("1234", ""), "Ashland", "VA"], [("1234", "Smith Sttttttttttttttt"), "Ashland", "VA"], [("1234", 30), "Ashland", "VA"],
                           [(1234, "Smith St"), "Ashland", "VA"], [("", "Smith St"), "Ashland", "VA"], [("12333333333334", "Smith St"), "Ashland", "VA"],
                           [("1234", "Smith St%"), "Ashland", "VA"], [("%", "Smith St"), "Ashland", "VA"],
                           [("1234", "Smith St"), 30, "VA"] [("1234", "Smith St"), "", "VA"], [("1234", "Smith St"), "Ashlandddddddddddddddddddddddd", "VA"], 
                           [("1234", "Smith St"), "Ashland%", "VA"], 
                           [("1234", "Smith St"), "Ashland", "PA"], [("1234", "Smith St"), "Ashland", ""], [("1234", "Smith St"), "Ashland", 30]
                           ]
    
        # test to ensure account type works correctly (must be "Checking" or "Savings")
        invalidAccountTypes = ["checking", "savings", 30]

        # test to ensure password works correctly (must be 8-16 chars in length, must not contain invalid chars + correct type
        invalidPasswords = ["pass", "passssssssssssssssss", "password/", "password\\", "password<", "password>","password|", "password ", 30]


        # test invalid first names 
        for i in invalidFirstNames:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client3.getFullName().updatefirstName(i)
                
        # test invalid last names
        for i in invalidLastNames:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                 self.client3.getFullName().updateLastName(i)
                 
        # test invalid phones
        for i in invalidPhones:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                 self.client3.getPhone().updatePhone(i)
        
        # test invalid addresses
        for i in invalidAddresss:
            # test to ensure asserts occur
            with self.assertRaises(AssertionError):
                self.client3.getAddress().updateAddress(i)
    
    	# change and compare
    	self.client3.getFullName().updatefirstName("Dawg")
    	self.client3.getFullName().updatelastName("Cat")
    	self.client3.getPhone().updatePhone("8045551234")
    	self.client3.getAddress().updateAddress([("751", "Elephant Blvd"), "New Mexico", "VA"])
    
    	# new client for comparison
    	self.client4 = Client("Dawg", "Cat", "8045551234", [("751", "Elephant Blvd"), "New Mexico", "VA"], "Checking", TestClient.CLIENT_ONE_PASSWORD)
    
    	# compare to original
    	assertNotEqual(self.client3.getFullName(), self.client1.getFullName())
    	assertNotEqual(self.client3.getPhone(), self.client1.getPhone())
    	assertNotEqual(self.client3.getAddress(), self.client1.getAddress())
    	
        # test eq methods
        assertNotEqual(self.client3.getFullName() == self.client1)
        assertNotEqual(self.client3.getPhone() == self.client1)
        assertNotEqual(self.client3.getAddress() == self.client1)
        
        # test str/repr methods
        assertEqual(str(self.client3.getFullName()), "Dawg Cat")
        assertEqual(str(self.client3.getPhone()), "8045551234")
        assertEqual(str(self.client3.getAddress()), "751 Elephant Blvd New Mexico, VA")	

		assertEqual(self.client3.getFullName().__repr__(), "Dawg Cat")
        assertEqual(str(self.client3.getPhone()__repr__(), "8045551234")
        assertEqual(str(self.client3.getAddress()__repr__(), "751 Elephant Blvd New Mexico, VA")
        
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
        closeAccountBooleanValue = self.client1.closeAccount(accountList[0].getAccountNumber())
        
        # Test to see that account was close, funds were withdrawn, and correct account was removed from the list
        self.assertEqual(closeAccountBooleanValue, True)
        accountList = self.client1._getAccounts()
        self.assertEqual(len(accountList), 1)
        self.assertEqual(accountList[0].getAccountType(), "Savings")
        
        # Test to ensure client can not close account, if they only have one account
        closeAccountBooleanValue = self.client1.closeAccount(accountList[0].getAccountNumber())
        self.assertEqual(closeAccountBooleanValue, False)

    @patch('testClient.get_input', return_value=CLIENT_ONE_PASSWORD)
    # test changing client password
    def testChangePassword(self, input):

        #** NOT DONE

        # test change password method
        self.client1.changePassword("fake_old_pass")

        # assume error
        self.client1.changePassword()


        # test to ensure new password works correctly (must be 8-16 chars in length, must not contain invalid chars + correct type
        invalidPasswords = ["pass", "passssssssssssssssss", "password/", "password\\", "password<", "password>","password|", "password ", 30]

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
        
    # test str/repr method
    def testToStr(self):
    	
    	fullName = str(self.client1.getFullName())
    	
    	#ensure string forms are equal
    	self.assertEqual(str(self.client1) == "Client\nClient = {}\nClient Number = {}\nAddress: {}\nPhone = {}\n# of accounts: {}\n".format(fullName, self.client1.getClientNumber(), 
    																																	TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, 
    																																	len(self.client1._getAccounts())
    	
		self.assertEqual(self.client1.__repr__() == "Client\nClient = {}\nClient Number = {}\nAddress: {}\nPhone = {}\n# of accounts: {}\n".format(fullName, self.client1.getClientNumber(), 
    																																	TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, 
    																																	len(self.client1._getAccounts())																																
    																																	
        
        
if __name__ == '__main__':
    unittest.main()