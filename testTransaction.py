""" 
Simple Unit Test Example using Python's unittest module and assertions
@author: John McManus
@date: March 19, 2021

Import the unittest module and the Transaction module
Test each method with at least one unit test
"""

import unittest

from transaction import Transaction

""" Define test testTransaction class by extending the unittest.TestCase class"""

class TestTransaction(unittest.TestCase):
    
    DEPOSIT = 2000   # Expected Deposit amount
    WITHDRAWAL = 500  # Expected Withdrawl amount
    FIRST = 100      # Expected first transaction number
    TYPE = "deposit" # Expected Deposit transaction type
    
    # The setup method creates three transactions
    def setUp(self):
        self.transaction1 = Transaction("deposit", TestTransaction.DEPOSIT)
        self.transaction2 = Transaction("withdrawal", TestTransaction.WITHDRAWAL)
        self.transaction3 = Transaction("interest")

    # The test_constructor method tests the constructor 
    def test_constructor(self):
        print("\nTesting the constructor") 
        self.assertEqual(self.transaction1.getAmount(), TestTransaction.DEPOSIT)
        self.assertEqual(self.transaction1.getTNumber(), TestTransaction.FIRST)
        self.assertEqual(self.transaction1.getTType(), TestTransaction.TYPE)
        print("The first transaction: ", self.transaction1)
        print(repr(self.transaction1))


    # Test the __eq__ special method 
    def test_eq(self):
        print("\nTesting the equal special method") 
        self.assertTrue(self.transaction1 == self.transaction1)  

    # Second test of the __eq__ special method    
    def test_eq_2(self):
        print("\nSecond test of the equal special method") 
        self.assertFalse(self.transaction1 == self.transaction2)  

    # Test the __ne__ special method     
    def test_ne(self):
        print("\nTesting the not equal special method ") 
        self.assertTrue(self.transaction1 != self.transaction2)

    # Second test of the __ne__ special method     
    def test_ne_2(self):
        print("\nSecond test of the not equal special method") 
        self.assertFalse(self.transaction1 != self.transaction1)    

    # Test the __add__ special method 
    def test_add(self):
        addTest = self.transaction1 + self.transaction1
        print("\nTesting the addition special method")        
        self.assertEqual(addTest, 4000)

    # Test the __sub__ special method 
    def test_sub(self):
        subTest = self.transaction1 - self.transaction2
        print("\nTesting the subtraction special method")
        self.assertEqual(subTest, 1500)   

    # Test the __sum__ special method     
    def test_sum(self):
        listTransactions = [self.transaction1, self.transaction2, self.transaction3]
        sumTest = sum(listTransactions)
        print("\nTesting the sum special method %d" % sumTest) 
        self.assertEqual(sumTest, (TestTransaction.DEPOSIT + TestTransaction.WITHDRAWAL))   
        
if __name__ == '__main__':
    unittest.main()