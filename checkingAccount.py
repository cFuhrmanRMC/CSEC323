# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# Project 3
# CSEC 323
# checkingAccount.py


from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
from bankAccount import BankAccount
from transaction import Transaction


# The Checking Account class should inherit all the core attributes and methods of the BankAccount class.
class CheckingAccount(BankAccount):
    
    _interestRate = 0.015 # private variable, instance rate for checking
    
    RESETFILE = True # Class constant that wipes file if true

    # Constructs a checking account
    # 
    # @param balance: The user's initial balance (Floating point, must be a positive float) default set to 0.0
    # @require: balance is positive, floating point numbre
    def __init__(self,accountNumber: int, balance=0.0):
        
        # Validate balance
        assert isinstance(balance, float), "Balance must be a floating point number"
        assert balance >= 0, "Balance must be positive"
        
        # Validate account number
        assert accountNumber >= 1000 and accountNumber <= 9999, "Invalid Account Number"
        assert isinstance(accountNumber, int), "Invalid Account Number"
      
      
        
        # call bank account constructor
        super().__init__("Checking", accountNumber, balance)
        
  
        
        # intialize overdraft counter to 0
        self._overdraftCounter = 0
        
        # clears the file if RESETFILE is True
        if CheckingAccount.RESETFILE:
            file = open("checking_{}.txt".format(self.getAccountNumber()), 'w')
            file.close()
        
        # Instance Variables for encryption
        self.key = b'MySuperSecretKey1222222222222222'  # AES-256 key (32 bytes)
        self.iv = b'MySuperSecretIV1'  # IV (16 bytes)
       
        
    # @Override Withdrawal an amount from the account
    # @param amount: Amount to withdraw, must be positive and within the account balance.
    # @return: True if withdrawal succeeds, False otherwise.
    def withdrawal(self, amount):
        # Preconditions: Ensure amount is positive and does not exceed balance
        assert amount >= 0, "Withdrawal amount must be positive."
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

        # Record the interest transaction
        interestTransaction = super()._createTransaction("interest", interest)
        self._addTransaction(interestTransaction)

             
        # Postconditions: Ensure balance is non-negative after adding interest
        assert self._balance >= 0, "Balance should be non-negative after adding interest."

        
    # Encrypts and writes a single checkings account transaction to "checkings.txt" for permanent storage.
    # Separate files for accounts
    # @param transaction: str, a string 
    # @require transaction param is a string
    # @ensure data is encrypted
    def _save_transactions(self, transaction: str):
        fileName = "checking_{}.txt".format(self.getAccountNumber())
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
        fileName = "checking_{}.txt".format(self.getAccountNumber())
        with open(fileName, "r+b") as infile: 
            # Loop to read and decrypt each transaction in the file
            length = infile.readline().rstrip().decode()
            
            result = ""
            
            try:
                while length != "":
                    length = int(length)
                    data = infile.read(length)
                    decrypted_data = decrypt_AES_CBC(data, self.key, self.iv)
                    
                    
                
                    result = result + decrypted_data + "\n" 
                    
                    # Move to the next transaction
                    infile.readline()
                    length = infile.readline().rstrip().decode()
                    
            except FileNotFoundError:
                print(f"No transaction file found for account {self.getAccountNumber()}.")
            except Exception as e:
                print("Error reading transactions: ", e)
                
       
            
                
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
    # @ensure param is a transaction object
    def _addTransaction(self, transaction: Transaction):
        assert isinstance(transaction, Transaction)
        self._save_transactions((str(transaction)))
   
   
    
    # PRIVATE method, return the file name for an account
    # @return a string, the file name that stores transactions
    def _getFileName(self)->str:
        return "savings_{}.txt".format(self.getAccountNumber())
    

