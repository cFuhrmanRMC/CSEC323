# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# Project 3
# CSEC 323
# savingsAccount.py
#
from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
from bankAccount import BankAccount  
from transaction import Transaction
from client import Client

# The Savings Account class should inherit all the core attributes and methods of the BankAccount.
class SavingsAccount(BankAccount):

    _interestRate = 0.04 # Interest Rate for savings account
    
    RESETFILE = True  # A class constant that clears the savings.txt file upon creating a Savings Account

    def __init__(self, balance=0.0):
        
        # if statement clears file if RESETFILE is True
        if SavingsAccount.RESETFILE:
            file = open("savings.txt", 'w')
            file.close()
        
        super().__init__("Savings", balance)

        
     
        self.overdraft_count = 0
        self.key = b'MySuperSecretKey1222222222222222'  # AES-256 key (32 bytes)
        self.iv = b'MySuperSecretIV1'  # IV (16 bytes)
        


    
    # Overrides the withdrawal method from BankAccount to implement overdraft limitations specific to savings accounts.
    # Allows up to three overdrafts, with increasing fees, and blocks withdrawals if the account balance is below $100 after 3 overdrafts.
    # @param amount: Amount to withdraw from the account (must be positive).
    # @return: True if withdrawal succeeds, False otherwise.
     
    def withdrawal(self, amount: float)->bool:
        
        # if the account has a balance of over 10000, reset the overdraft count
        if self._balance > 10000.00:
            self._overdraft_count = 0
     
        # Preconditions: Ensure amount is positive and withdrawal is allowed under overdraft rules
        assert amount > 0, "Withdrawal amount must be positive."
        assert self.overdraft_count < 3 or self._balance >= 100, "Cannot withdraw: Balance must be at least $100 after 3 overdrafts."
        
        
        # Check to see if amount is valid
        if amount > self._balance + 250:
            print("Transaction denied. Exceeds overdraft limit.")
            return False
        
        elif amount > self._balance:
            # Apply overdraft fee
            self.overdraft_count += 1
            # The overdraft fee for the first time is $20.
            if self.overdraft_count == 1:
                fee = 20
            # The overdraft fee for the second time is $30. 
            elif self.overdraft_count == 2:
                fee = 30
            # The overdraft fee for the third time is $50.
            else:
                fee = 50
            # Deduct withdrawal amount and fee from balance, and record the transactions    
            self._balance -= amount
            self._balance -= fee
            
            withdrawalTransaction = super()._createTransaction("withdrawal", amount)
            penaltyTransaction = super()._createTransaction("penalty", fee)
            
            self._addTransaction(withdrawalTransaction)
            self._addTransaction(penaltyTransaction)
            print("Overdraft fee applied:", fee) 
            return True
        
        else:
            # If no overdraft, proceed with normal withdrawal
            return super().withdrawal(amount)

        
    


        # Postconditions: Ensure overdraft count is within limit, and balance is >= $100 if overdraft limit is reached
        assert self.overdraft_count <= 3, "Overdraft count should not exceed 3."
        assert self._balance >= 0 or (self.overdraft_count < 3), "Balance should be >= $100 if overdrafts reach the limit of 3."

    # @Override add interest method from bankaccount for savings account sub class
    # Resets overdraft count if balance exceeds $10,000.
    def addInterest(self):
        # Preconditions: Ensure balance is non-negative before adding interest
        assert self._balance >= 0, "Interest cannot be added to a negative balance."
        
        # Calculate and add interest to the balance
        interest = self._balance * SavingsAccount._interestRate
        self._balance = self._balance + interest
        
        # Record the interest transaction
        interestTransaction = super()._createTransaction("interest", interest)
        self._addTransaction(interestTransaction)

        # Postconditions: Reset overdraft count if balance is high enough, ensure overdraft count is non-negative
        if self._balance > 10000:
            self.overdraft_count = 0  # Reset overdraft count if balance exceeds $10,000
        assert self.overdraft_count >= 0, "Overdraft count should be non-negative."
        
        
        # Preconditions:
        assert self._balance >= 0, "Interest cannot be added to a negative balance."
        
        
        
    # Encrypts and writes a single savings account transaction to "savings.txt" for permanent storage.
    # Separate files for accounts
    def _save_transactions(self, transaction: str):
        fileName = "savings_{}.txt".format(self.getAccountNumber())
        with open(fileName, "ab") as outfile:        
            
            # Validate that the transaction is a string
            assert isinstance(transaction, str), "Transaction data must be a string."
        
            # Encrypt the transaction data
            result = encrypt_AES_CBC(transaction, self.key, self.iv)
        
            # Write encrypted transaction to the file
            outfile.write(str(len(result)).encode() + b"\n")  # Write the length of the encrypted data
            outfile.write(result + b"\n")                   # Write the encrypted transaction
        outfile.close()
        
            
          

    # Reads all encrypted transactions from "savings.txt", decrypts each, and prints to the console.
    def _load_transactions(self) -> str:
        fileName = "savings_{}.txt".format(self.getAccountNumber())
        with open(fileName, "r+b") as outfile: 
            # Loop to read and decrypt each transaction in the file
            length = infile.readline().rstrip().decode()
            
            result = ""
            
            try:
                while length != "":
                    length = int(length)
                    data = infile.read(length)
                    decrypted_data = decrypt_AES_CBC(data, self.key, self.iv)
                    
                    #Checks to see if transaction matches associated account number before adding it to the result
                    if str(self.getAccountNumber()) in decrypted_data:
                        result = result + decrypted_data + "\n" 
                    
                    # Move to the next transaction
                    infile.readline()
                    length = infile.readline().rstrip().decode()
                    
            except FileNotFoundError:
                print(f"No transaction file found for account {self.getAccountNumber()}.")
            except Exception as e:
                print("Error reading transactions: ", e)
            
                
            return result
        
    

    # return the account details in a string readable format
    # @return: The formatted, human readable string of the account
    def __repr__(self) -> str:
       # display accountType, account number, balance, and transaction list
        return ("Savings Account\nAccount Number = %d \nBalance = $%.2f \nTransactions: \n%s \n" %
        (self._accountNumber, self._balance, self._load_transactions()))


    # return the account details in a string readable format
    # @return: The formatted, human readable string of the account
    def __str__(self) -> str:
        # display accountType, account number, balance, and transaction list
        return ("Savings Account\nAccount Number = %d \nBalance = $%.2f\nTransactions: \n%s \n" %
        (self._accountNumber, self._balance, self._load_transactions())) 
                
        
                
    
    # Overrides _addTransaction from BankAccount to save each transaction to file immediately.
    # @param transaction: The transaction object to add to the transaction list and save to file. 
    def _addTransaction(self, transaction: Transaction):
        assert isinstance(transaction, Transaction)
        self._save_transactions((str(transaction), " Account Number: " + str(self.getAccountNumber())))
   
   
   
    # Equality method, checks to ensure checking accounts are equal
    # @param other: a savings account object
    # @Override, overrides eq method from bankAccount
    def __eq__(self, other):
        return(self.getBalance() == other.getBalance() and self.getAccountNumber() == other.getAccountNumber())
        
        
# Test function to demonstrate account actions and transaction loading.
def main():
    # Create a new savings account and perform some transactions
    myAccount = SavingsAccount(50.00)
    myAccount.withdrawal(20.00) # Test withdrawal
    myAccount.deposit(30.00) # Test deposit
    myAccount.addInterest() # Test interest addition
  
    print(myAccount)
    
