# testCheckingAccount.py
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest

from checkingAccount import CheckingAccount

""" Define test TestClient class by extending the unittest.TestCase class"""

class TestCheckingAccount(unittest.TestCase):
    
    CHECKING_ONE_BALANCE = 50.0
    CHECKING_TWO_BALANCE = 100.0


    
    # The setup method creates three checking accounts
    def setUp(self):
        self.checking1 = CheckingAccount(TestCheckingAccount.CHECKING_ONE_BALANCE)
        self.checking2 = CheckingAccount(TestCheckingAccount.CHECKING_TWO_BALANCE)
        self.checking3 = CheckingAccount()
 

    # The testConstructor method tests the constructor 
    def testConstructor(self):
        # test regular constructor function and acessor methods
        self.assertEqual(self.checking1.getBalance(), TestCheckingAccount.CHECKING_ONE_BALANCE)
        self.assertEqual(self.checking1.getAccountType(), "Checking")
        self.assertEqual(self.checking1.getAccountNumber(), 1000)
        self.assertEqual(self.checking3.getBalance(), 0.0)
      
    # The testAddInterest method tests addInterest method, ensuring it was properly overrided from bankAccount   
    def testAddInterest(self):
        # test to check if appropriate interest amount is added, and transaction list is updated
        self.checking1.addInterest()
        self.assertEqual(len(self.checking1.getTransactions()), 1)
        self.assertEqual(self.checking1.getBalance(), 50.75)
        
        # test to ensure interest is not added to an account with a balance of 0
        self.checking3.addInterest()
        self.assertEqual(self.checking3.getBalance(), 0.0)
        
        
    # test to ensure the file is encrypted
    def testEncryption(self):
        self.checking1.deposit(10.00)
        
        # test to ensure file is encrpyted
        encryptedFile = open("checking.txt", "r")
        with self.assertRaises(UnicodeDecodeError):
            encryptedFile.readline()
        encryptedFile.close()

        
    # The testWithdrawal method tests the withdrawal method, ensuring it was properly overrided from bankAccount
    def testWithdrawal(self):
        withdrawalBoolean = self.checking2.withdrawal(50.0)
        self.assertEqual(self.checking2.getBalance(), 50.0)
        self.assertEqual(withdrawalBoolean, True)
        
    # test the equality method
    def testEq(self):
        
        self.assertEqual(self.checking1, self.checking1)
        
        self.assertNotEqual(self.checking1, self.checking2)

        
        
        
        
        
if __name__ == '__main__':
    unittest.main()