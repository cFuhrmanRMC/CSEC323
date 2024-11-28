# testCheckingAccount.py
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest

from checkingAccount import CheckingAccount

# used to test decrpytion accuracy
from datetime import date

""" Define test TestClient class by extending the unittest.TestCase class"""

class TestCheckingAccount(unittest.TestCase):
    
    CHECKING_ONE_BALANCE = 50.0
    CHECKING_TWO_BALANCE = 100.0
    CHECKING_FOUR_BALANCE = 39.0
    INVALID_INPUTS = [-5.00, 5, "string"]


    
    # The setup method creates three checking accounts
    def setUp(self):
        self.checking1 = CheckingAccount(TestCheckingAccount.CHECKING_ONE_BALANCE)
        self.checking2 = CheckingAccount(TestCheckingAccount.CHECKING_TWO_BALANCE)
        self.checking3 = CheckingAccount()
        self.checking4 = CheckingAccount(TestCheckingAccount.CHECKING_FOUR_BALANCE)
        
        # test to ensure assertions function in constructor
        for i in range(len(TestCheckingAccount.INVALID_INPUTS)):
            with self.assertRaises(AssertionError):
                self.checking5 = CheckingAccount(TestCheckingAccount.INVALID_INPUTS[i])
 

    # The testConstructor method tests the constructor 
    def testConstructor(self):
        # test regular constructor function and acessor methods
        self.assertEqual(self.checking1.getBalance(), TestCheckingAccount.CHECKING_ONE_BALANCE)
        self.assertEqual(self.checking1.getAccountType(), "Checking")
        self.assertEqual(self.checking1.getAccountNumber(), 1000)
        self.assertEqual(self.checking3.getBalance(), 0.0)
      
    # The testAddInterest method tests addInterest method, ensuring it was properly overrided from bankAccount   
    def testaddInterest(self):
        # test to check if appropriate interest amount is added, and transaction list is updated
        self.checking1.addInterest()
        self.assertEqual(self.checking1.getBalance(), 50.75)
        
        # test to ensure interest is not added to an account with a balance of 0
        self.checking3.addInterest()
        self.assertEqual(self.checking3.getBalance(), 0.0)
        
        
    # test to ensure the file is encrypted
    def testEncryption(self):
        self.checking1.deposit(10.00)
        
        # test to ensure file is encrpyted
        encryptedFile = open(self.checking1._getFileName(), "r")
        with self.assertRaises(UnicodeDecodeError):
            encryptedFile.readline()
        encryptedFile.close()
        
        # ensure only strings are being encrypted
        with self.assertRaises(AssertionError):
            self.checking1._save_transactions(100)
        
    # test to ensure data integrity is maintained in decrpytion process  
    def testDecryption(self):
        expectedOutput = ["Transaction # 100, amount = $39.00, date " + str(date.today()) +", type: deposit", "Transaction # 101, amount = $10.00, date " + str(date.today()) +", type: withdrawal", "Transaction # 102, amount = $1.02, date " + str(date.today()) +", type: interest"]
        self.checking4.deposit(39.00)
        self.checking4.withdrawal(10.00)
        self.checking4.addInterest()
        actualOutputString = self.checking4._load_transactions()
        

        
        # Converts the decryption output into a list for comparison
        actualOutput = actualOutputString.splitlines()
        
        # test to ensure exepected transactions equal actual transactions
        for i in range(len(expectedOutput)):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput[i], actualOutput[i])
                


        
    # The testWithdrawal method tests the withdrawal method, ensuring it was properly overrided from bankAccount
    def testWithdrawal(self):
        withdrawalBoolean = self.checking2.withdrawal(50.0)
        self.assertEqual(self.checking2.getBalance(), 50.0)
        self.assertEqual(withdrawalBoolean, True)
        
    # test the equality method
    def testEq(self):
        
        self.assertEqual(self.checking1, self.checking1)
        
        self.assertNotEqual(self.checking1, self.checking2)
        
        
    # test to ensure only transaction objects can be saved and subsequently encrypted
    def testAddTransaction(self):
        account = CheckingAccount()
        badInputs = [100, "string", 40.00, account]
        
        with self.assertRaises(AssertionError):
            for i in range(len(badInputs)):
                self.checking1._addTransaction(badInputs[i])

        
        
        
        
        
if __name__ == '__main__':
    unittest.main()
