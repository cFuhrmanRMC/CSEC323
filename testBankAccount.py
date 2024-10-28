# testBankAccount.py 
# Group: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# CSEC 323-01: Software Security
# Dr. McManus
#

import unittest

from bankAccount import BankAccount

""" Define test testBankAccount class by extending the unittest.TestCase class"""
class TestBankAccount(unittest.TestCase):
	
	
	ACCOUNT_ONE_AMOUNT = 20.0
	ACCOUNT_ONE_FIRSTNAME = "Trace"
	ACCOUNT_ONE_LASTNAME = "Taylor"

	ACCOUNT_TWO_FIRSTNAME = "Dillon"
	ACCOUNT_TWO_LASTNAME = "VanGlider"

	ACCOUNT_THREE_AMOUNT = 50.0
	ACCOUNT_THREE_FIRSTNAME = "Cole"
	ACCOUNT_THREE_LASTNAME = "Fuhrman"



	def setUp(self):
		# Arrange
		self.bankAccountOne = BankAccount(TestBankAccount.ACCOUNT_ONE_FIRSTNAME, TestBankAccount.ACCOUNT_ONE_LASTNAME, TestBankAccount.ACCOUNT_ONE_AMOUNT)
		self.bankAccountTwo = BankAccount(TestBankAccount.ACCOUNT_TWO_FIRSTNAME, TestBankAccount.ACCOUNT_TWO_LASTNAME)

		self.bankAccountThree = BankAccount(TestBankAccount.ACCOUNT_THREE_FIRSTNAME, TestBankAccount.ACCOUNT_THREE_LASTNAME, TestBankAccount.ACCOUNT_THREE_AMOUNT)

		# Maybe write some code that would catch the assert statements thrown by the 
		# creation of a bank account with invalid parameters?

	def testConstructor(self):
		print("\nTesting constructor")

		# Test regular constructor function
		self.assertEqual(self.bankAccountOne.getFirstName(), TestBankAccount.ACCOUNT_ONE_FIRSTNAME)
		self.assertEqual(self.bankAccountOne.getLastName(), TestBankAccount.ACCOUNT_ONE_LASTNAME)
		self.assertEqual(self.bankAccountOne.getBalance(), TestBankAccount.ACCOUNT_ONE_AMOUNT)
	
		self.assertEqual(self.bankAccountOne.getAccountNumber(), 1000)
		self.assertEqual(self.bankAccountOne.getOverdraftCounter(), 0)
	
		#Test for no amount provided and test to ensure account number is increasing
		self.assertEqual(self.bankAccountTwo.getBalance(), 0.0)
		self.assertEqual(self.bankAccountTwo.getAccountNumber(), 1001)
		
	def testEqMethod(self):
		print("\nTesting __eq__ Method")
		self.assertEqual(self.bankAccountOne, self.bankAccountOne)	

	def testDeposit(self):
		print("\nTesting Deposit")
	
		self.bankAccountOne.deposit(30.00)
	
		#test to see if amount was deposited
		self.assertEqual(self.bankAccountOne.getBalance(), 50.00)
	
		#test to see if transaction list was updated
		self.assertEqual(len(self.bankAccountOne.getTransactions()), 1)


	def testWithdrawal(self):
		print("\nTesting Withdrawal")
		self.bankAccountThree.withdrawal(20.0)
		self.assertEqual(self.bankAccountThree.getBalance(), 30.00)
	
	def testAddInterest(self):
		print("\nTesting AddInterest")
		# Apply interest to account
		self.bankAccountThree.addInterest()
		
		# Check that a new transaction for interest was added
		self.assertEqual(len(self.bankAccountThree.getTransactions()), 1)
		
	def testDisplayTransaction(self):
		print("\nTesting DisplayTransaction")
		
		# Deposit and Withdraw
		self.bankAccountOne.deposit(50.0)
		self.bankAccountOne.withdrawal(30.0)
		
		# Check the number of transactions
		self.assertEqual(len(self.bankAccountOne.getTransactions()), 2)
	
	def testTransfer(self):
		print("\nTesting Transfer")
		
		# Transfer an amount from one account to another
		self.bankAccountThree.transfer(10.0, self.bankAccountOne)
		
		# Check balances after transfer
		self.assertEqual(self.bankAccountOne.getBalance(), TestBankAccount.ACCOUNT_ONE_AMOUNT - 10.0)
		self.assertEqual(self.bankAccountThree.getBalance(), TestBankAccount.ACCOUNT_THREE_AMOUNT + 10.0)
	    
		# Check that both accounts' transaction lists are updated
		self.assertEqual(len(self.bankAccountOne.getTransactions()), 2)  # One deposit, one transfer out
		self.assertEqual(len(self.bankAccountThree.getTransactions()), 1)  # One transfer in
		
	def testOverdraftCounter(self):
		print("\nTesting OverdraftCounter")
   
		# Withdraw more than the balance to trigger an overdraft
		self.bankAccountOne.withdrawal(40.0)
		
		# Check that the overdraft fee is applied and overdraft counter is incremented
		self.assertEqual(self.bankAccountOne.getOverdraftCounter(), 1)
	    
		# Check that the correct transactions (withdrawal and overdraft penalty) were added
		self.assertEqual(len(self.bankAccountOne.getTransactions()), 2)
	 		
if __name__ == '__main__':
	unittest.main()