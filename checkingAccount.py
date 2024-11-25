# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# Project 3
# CSEC 323
# checkingAccount.py


from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
from bankAccount import BankAccount
from transaction import Transaction
from client import Client

# The Checking Account class should inherit all the core attributes and methods of the BankAccount class.
class CheckingAccount(BankAccount):
    
    _interestRate = 0.015 # private variable, instance rate for checking
    
    RESETFILE = True # Class constant that wipes file if true

    # Constructs a checking account
    # 
    # @param balance: The user's initial balance (Floating point, must be a positive float) default set to 0.0
    # @ensure: self.interest_rate = 0.015.
    def __init__(self, balance=0.0):
        
        # if statment that wipes the file if selected
        if CheckingAccount.RESETFILE:
            file = open("checking.txt", "w")
            file.close()
        
        super().__init__("Checking", balance)
       
        self.key = b'MySuperSecretKey1222222222222222'  # AES-256 key (32 bytes)
        self.iv = b'MySuperSecretIV1'  # IV (16 bytes)
        
    # @Override Withdrawal an amount from the account
    # @param amount: Amount to withdraw, must be positive and within the account balance.
    # @return: True if withdrawal succeeds, False otherwise.
    def withdrawal(self, amount):
        # Preconditions: Ensure amount is positive and does not exceed balance
        assert amount > 0, "Withdrawal amount must be positive."
        assert amount <= self._balance, "Insufficient funds: Overdrafts are not allowed in CheckingAccount."

        success = super().withdrawal(amount)

        # Postconditions: Ensure balance remains non-negativee
        assert self._balance >= 0, "Balance should not be negative after withdrawal."
        return success
    
    # @Override Calculate interest and add the interest amount to the account balance.
    # Only applies if balance is non-negative.
    def addInterest(self):
        # Preconditions:
        assert self._balance >= 0, "Interest cannot be added to a negative balance."

        # calculate interest and add it to the account balance
        interest = self._balance * CheckingAccount._interestRate
        self._balance = self._balance + interest

        # create a interest transaction object and add it to the transaction list
        super()._addTransaction(Transaction("interest", interest))

             
        # Postconditions: Ensure balance is non-negative after adding interest
        assert self._balance >= 0, "Balance should be non-negative after adding interest."

        
    # Encrypts and writes a single checking account transaction to "checking.txt" for permanent storage.
    # Separate files for accounts
    def _save_transactions(self):
        fileName = "checking_{}.txt".format(self.getAccountNumber())
        with open(fileName, "r+b") as outfile:
             # Validate that the transaction is a string
            assert isinstance(transaction, str), "Transaction data must be a string."
        
            # Encrypt the transaction data
            result = encrypt_AES_CBC(transaction, self.key, self.iv)
        
            # Write encrypted transaction to the file
            outfile.write(str(len(result)).encode() + b"\n")  # Write the length of the encrypted data
            outfile.write(result + b"\n")                   # Write the encrypted transaction
        outfile.close()
        
            
          

    # Reads all encrypted transactions from "checking.txt", decrypts each, and prints to the console.
    def _load_transactions(self) -> str:
        fileName = "checking_{}.txt".format(self.getAccountNumber())
        with open(fileName, "ab") as outfile:
            # Loop to read and decrypt each transaction in the file
            length = infile.readline().rstrip().decode()
            
            result = ""
            
            
            
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
                
            return result
        
    
    # @Override, overides repr method from bankAccount
    # return the account details in a string readable format
    # @return: The formatted, human readable string of the account
    def __repr__(self) -> str:
       # display accountType, account number, balance, and transaction list
        return ("Checking Account\nAccount Number = %d \nBalance = $%.2f \nTransactions: \n%s \n" %
        (self._accountNumber, self._balance, self._load_transactions()))

    # @Override, overides str method from bankAccount
    # return the account details in a string readable format
    # @return: The formatted, human readable string of the account
    def __str__(self) -> str:
        # display accountType, account number, balance, and transaction list
        return ("Checking Account\nAccount Number = %d \nBalance = $%.2f\nTransactions: \n%s \n" %
        (self._accountNumber, self._balance, self._load_transactions())) 
    
    
    # Equality method, checks to ensure checking accounts are equal
    # @Override, overrides eq method from bankAccount
    # @param: other, a checking account object
    def __eq__(self, other):
        return(self.getBalance() == other.getBalance() and self.getAccountNumber() == other.getAccountNumber())
        
                
        
                
        
        
    # Overrides _addTransaction from BankAccount to save each transaction to file immediately.
    # @param transaction: The transaction object to add to the transaction list and save to file. 
    def _addTransaction(self, transaction: Transaction):
        assert isinstance(transaction, Transaction)
        self._save_transactions((str(transaction), " Account Number: " + str(self.getAccountNumber())))
        
        
        
        
# Test function to demonstrate account actions and transaction loading.        
def main():
    # Create a new savings account and perform some transactions
    myAccount = CheckingAccount(39.00)
    myAccount.deposit(39.00) # Test deposit
    myAccount.withdrawal(10.00) # Test withdrawal
     
    print(myAccount)
    
    
    
