# testClient.py
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest

from client import Client

""" Define test TestClient class by extending the unittest.TestCase class"""

class TestClient(unittest.TestCase):
    
    CLIENT_ONE_FIRSTNAME = "Cole"
    CLIENT_ONE_LASTNAME = "Fuhrman"
    CLIENT_ONE_PHONENUM = "8047292516"
    CLIENT_ONE_ADDRESS = ["1234SmithSt", "Ashland", "VA"]

    
    # The setup method creates a client
    def setUp(self):
        self.client1 = Client(TestClient.CLIENT_ONE_FIRSTNAME, TestClient.CLIENT_ONE_LASTNAME, TestClient.CLIENT_ONE_PHONENUM, TestClient.CLIENT_ONE_ADDRESS, "Checking")
      
 

    # The test_constructor method tests the constructor 
    def testConstructor(self):
        # test regular constructor function and acessor methods
        self.assertEquals(self.client1.getFirstName(), TestClient.CLIENT_ONE_FIRSTNAME)
        self.assertEquals(self.client1.getLastName(), TestClient.CLIENT_ONE_LASTNAME)        
        self.assertEquals(self.client1.getPhone(), TestClient.CLIENT_ONE_PHONENUM)
        self.assertEquals(str(self.client1.getAddress()), "1234SmithSt Ashland, VA")
        self.assertEquals(self.client1.getClientNumber(), 100)
        
        # Test to ensure the client has at least one account upon creation
        accountList = self.client1._getAccounts()
        self.assertEquals(accountList[0].getAccountType(), "Checking")
        self.assertEquals(len(accountList), 1)
        
        # Test to ensure that client is handling bank account numbers 
        self.client1.openAccount("Checking")
        self.assertEquals(accountList[1].getAccountNumber(), 1001)
        
     
        
        
    # test opening and closing a bank account
    def testOpenAndCloseBankAccount(self):

        self.client1.openAccount("Savings")
        accountList = self.client1._getAccounts()
        
        
        # Test to see if new account was opened
        self.assertEquals(accountList[1].getAccountType(), "Savings")
        self.assertEquals(accountList[0].getAccountType(), "Checking")
        self.assertEquals(len(accountList), 2)
        
        
        
        # make a deposit to the checking account and then attempt to close the account
        accountList[0].deposit(20.00)
        closeAccountBooleanValue = self.client1.closeAccount(accountList[0].getAccountNumber())
        
        # Test to see that account was close, funds were withdrawn, and correct account was removed from the list
        self.assertEquals(closeAccountBooleanValue, True)
        accountList = self.client1._getAccounts()
        self.assertEquals(len(accountList), 1)
        self.assertEquals(accountList[0].getAccountType(), "Savings")
        
        # Test to ensure client can not close account, if they only have one account
        closeAccountBooleanValue = self.client1.closeAccount(accountList[0].getAccountNumber())
        self.assertEquals(closeAccountBooleanValue, False)
        
        
    # test equal method    
    def testEqMethod(self):
        
        self.assertEquals(self.client1, self.client1)
        
        

 
        
        
        
if __name__ == '__main__':
    unittest.main()