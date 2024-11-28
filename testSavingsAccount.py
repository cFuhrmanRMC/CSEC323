# testSavingsAccount.py
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest

from savingsAccount import SavingsAccount

# used to test decrpytion accuracy
from datetime import date

""" Define test TestClient class by extending the unittest.TestCase class"""

class TestSavingsAccount(unittest.TestCase):
    
    SAVINGS_ONE_BALANCE = 50.0
    SAVINGS_TWO_BALANCE = 100.0
    SAVINGS_FOUR_BALANCE = 50.0
    
    INVALID_INPUTS = [-5.00, 5, "string"]

    
    # The setup method creates savings accounts
    def setUp(self):
        self.savings1 = SavingsAccount(TestSavingsAccount.SAVINGS_ONE_BALANCE)
        self.savings2 = SavingsAccount(TestSavingsAccount.SAVINGS_TWO_BALANCE)
        self.savings3 = SavingsAccount()
        self.savings4 = SavingsAccount(TestSavingsAccount.SAVINGS_FOUR_BALANCE)
        
        # test to ensure assertions function in constructor
        for i in range(len(TestSavingsAccount.INVALID_INPUTS)):
            with self.assertRaises(AssertionError):
                self.savings5 = SavingsAccount(TestSavingsAccount.INVALID_INPUTS[i])
            
        


    # The testConstructor method tests the constructor 
    def testConstructor(self):
        # test regular constructor function and acessor methods
        self.assertEqual(self.savings1.getBalance(), 50.0)
        self.assertEqual(self.savings1.getAccountType(), "Savings")
        self.assertEqual(self.savings1.getAccountNumber(), 1000)
        self.assertEqual(self.savings3.getBalance(), 0.0)
      
    # The testAddInterest method tests addInterest method, ensuring it was properly overrided from bankAccount   
    def testaddInterest(self):
        # test to check if appropriate interest amount is added, and transaction list is updated
        self.savings1.addInterest()
        self.assertEqual(self.savings1.getBalance(), 52.00)
        
        # test to ensure interest is not added to an account with a balance of 0
        self.savings3.addInterest()
        self.assertEqual(self.savings3.getBalance(), 0.0)
        
    # test to ensure the file is encrypted
    def testEncryption(self):
        self.savings1.deposit(10.00)
        
        # test to ensure file is encrpyted
        encryptedFile = open(self.savings1._getFileName(), "r")
        with self.assertRaises(UnicodeDecodeError):
            encryptedFile.readline()
        encryptedFile.close()
        
        # ensure only strings are being encrypted
        with self.assertRaises(AssertionError):
            self.savings1._save_transactions(100)
      
    # test to ensure data integrity is maintained in decrpytion process  
    def testDecryption(self):
        expectedOutput = ["Transaction # 100, amount = $20.00, date " + str(date.today()) +", type: withdrawal", "Transaction # 101, amount = $30.00, date " + str(date.today()) +", type: deposit", "Transaction # 102, amount = $2.40, date " + str(date.today()) +", type: interest"]
        self.savings4.withdrawal(20.00)
        self.savings4.deposit(30.00)
        self.savings4.addInterest()
        actualOutputString = self.savings4._load_transactions()
        
        # Converts the decryption output into a list for comparison
        actualOutput = actualOutputString.splitlines()
        
        # test to ensure exepected transactions equal actual transactions
        for i in range(len(expectedOutput)):
            with self.subTest(i=i):
                self.assertEqual(expectedOutput[i], actualOutput[i])
                
            
        
        
    # The testWithdrawal method tests the withdrawal method, ensuring it was properly overrided from bankAccount
    def testWithdrawal(self):
        
        # test 1st overdraft
        self.savings2.withdrawal(150.00)
        self.assertEqual(self.savings2.getBalance(), -70.00)
        
        
        # test 2nd overdraft
        self.savings2.withdrawal(30.00)
        self.assertEqual(self.savings2.getBalance(), -130.00)
        
        self.savings2.withdrawal(20.00)
        # ensure that account can not have a withdrawal after 3 overdrafts
        with self.assertRaises(AssertionError):
            self.savings2.withdrawal(20.00)
        
        # ensure that withdrawal can be made after over draft counter is reset    
        self.savings2.deposit(12000.00)
        withdrawalSuccess = self.savings2.withdrawal(100.00)
        self.assertEqual(withdrawalSuccess, True)
        
    # test the equality method
    def testEq(self):
        
        self.assertEqual(self.savings1, self.savings1)
        
        self.assertNotEqual(self.savings1, self.savings2)
        
    # test to ensure only transaction objects can be saved and subsequently encrypted
    def testAddTransaction(self):
        account = SavingsAccount()
        badInputs = [100, "string", 40.00, account]
        
        with self.assertRaises(AssertionError):
            for i in range(len(badInputs)):
                self.savings1._addTransaction(badInputs[i])
        
        
        
if __name__ == '__main__':
    unittest.main()
