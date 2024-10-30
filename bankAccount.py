# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# Project 1
# CSEC 323



# import transaction class to create and manipulate transactions
from transaction import Transaction

# This module defines the BankAccount class
# A class to represent the data elements and methods required to implement a bank account

class BankAccount:

    _nextAccountNumber = 1000 # private class variable that holds the next account number
    _overdraftFee = 20.00 # private class vairable that holds the overdraft fee
    _interestRate = 0.075 # private class variable that holds the interest rate


    # Constructs a bank account
    # 
    # @param firstName: the first name of the account holder (String, must be between 1 and 25 characters with no special characters)
    # @param lastName: The user's last name (String, must be between 1 and 40 characters with no special characters))  
    # @param balance: The user's initial balance (Floating point, must be a positive float) default set to 0.0
    #
    # @require firstName: must be between 1 and 25 characters with no special characters
    # @require lastName: must be between 1 and 40 characters with no special characters
    # @require balance: must be a positive float
    # @ensure self._balance >= 0.0
    # @ensure unique account number is assigned
    def __init__(self, firstName: str, lastName: str, balance: float = 0.0 ):

        # Preconditions:
        # - firstName must be a valid string of 1-25 alphabetic characters.
        # - lastName must be a valid string of 1-40 alphabetic characters.
        # - balance must be a non-negative float.

        # Postconditions:
        # - A unique account number is assigned.
        # - The initial balance is set or defaulted to 0.0.

        assert 1 <= len(firstName) <= 25 and firstName.isalpha(), "Invalid first name."
        assert 1 <= len(lastName) <= 40 and lastName.isalpha(), "Invalid last name."
        assert isinstance(balance, float), "balance must be a floating point value"
        assert balance >= 0.0, "Initial balance must be non-negative."


        self._firstName = firstName # First name
        self._lastName = lastName # Last name
        self._balance = balance # Account balance
        self._accountNumber = BankAccount._nextAccountNumber # set account number

        #Increase account number by one to update account number
        BankAccount._nextAccountNumber = BankAccount._nextAccountNumber + 1  

        self._overdraftCounter = 0  # Tracks overdraft occurrences
        self._transactionList = []  # List to store transactions

    #   
    # Define special methods
    #

    
    # return the account details in a string readable format
    # @return: The formatted, human readable string of the account
    def __repr__(self) -> str:
        # display first name, last name, account number, balance, and transaction list
        return ("Bank Account\nAccount Holder = %s %s\nAccount Number = %d\nBalance = $%.2f\nTransactions:\n%s \n" %
        (self._firstName, self._lastName, self._accountNumber, self._balance, self.displayTransactions()))


    # return the account details in a string readable format
    # @return: The formatted, human readable string of the account
    def __str__(self) -> str:
        # display first name, last name, account number, balance, and transaction list
        return ("Bank Account\nAccount Holder = %s %s\nAccount Number = %d\nBalance = $%.2f\nTransactions:\n%s \n" %
        (self._firstName, self._lastName, self._accountNumber, self._balance, self.displayTransactions()))

        
    # Checks a BankAccount to see if it is equal to the second BankAccount
    # @param other: the transaction your are comparing the first transaction with
    # @return result: True if this two transaction have the same amount and dates, and tNumber
    def __eq__(self, other) -> bool :
        result = (self._firstName == other._firstName) and (self._lastName == other._lastName) and (self._accountNumber == other._accountNumber) and (self._balance == other._balance) and (self._transactionList == other._transactionList) and (self._overdraftCounter == other._overdraftCounter)
        return result 

    
    ##
    # Define acessor methods
    ##

    # returns the first name of the account holder
    # @return: a string, the first name of the account holder
    def getFirstName(self)->str:
        return self._firstName

    # returns the last name of the account holder
    # @return: a string, the last name of the account holder
    def getLastName(self)->str:
        return self._lastName

    # return the balance of the account
    # @return: a foating point, the balance of the account
    def getBalance(self)->float:
        return self._balance

    # return a list of all transactions
    # @return: a list, a list of the transactions
    def getTransactions(self)->list:
        return self._transactionList

    # returns the account number
    # @return: an integer, the account number
    def getAccountNumber(self)->int:
        return self._accountNumber

    # returns the overdraft counter
    # @return: an integer, the overdraft counter
    def getOverdraftCounter(self)->int:
        return self._overdraftCounter

    # converts the transaction list into a readable string 
    # @return: a string,  transactionString: a string of all of the transactions from the transaction list
    def displayTransactions(self)->str:
        transactionList = self.getTransactions()
        transactionString = ""

        # loop through the transactionList
        for transaction in transactionList:

            # Convert the transaction object to a readable string and add it to the transaction string
            transactionString = transactionString + str(transaction) + "\n"

        return transactionString    

    ##
    # Define mutator methods
    ##

    # increases the overdraftCounter by 1
    # @ensure overdraftCounter is incremented by 1
    def _increaseOverdraftCounter(self):
        self._overdraftCounter = self._overdraftCounter + 1


    # add an amount to the account balance
    # @param amount: the amount being deposited
    # @require amount depositied is a positive floating point value
    # @ensure amount is deposited to the account
    def deposit(self, amount: float):

        assert isinstance(amount, float), "Deposit amount must be a floating point value"
        assert amount > 0, "Deposit amount must be greater than 0"

        # add the amounnt to the account balance
        self._balance = self._balance + amount

        # create a deposit transaction object 
        depositTransaction = Transaction("deposit", amount)

        # apend transaction to the list of transactions
        self.addTransaction(depositTransaction)

        print("Deposited: $%.2f \n" % amount)




    # withdrawal an amount from the account balance
    # @param amount: floating point, the amount to be withdrawn from the account
    # @return: boolean value, true if withdrawal is successful, false if not 
    # @require withdrawl is a positive floating point value
    # @require withdrawl amount is less than or equal to current balance + 250
    # @ensure overdraft fee is applied if account is overdrawn
    # @ensure amount is withdrawn from the account is valid
    def withdrawal(self, amount: float)->bool:
        # Preconditions:
        # - The withdrawal amount must be less than or equal to the current balance + 250 (overdraft limit).

        # Postconditions:
        # - If the account is overdrawn, a penalty is applied and a message is printed.
        assert isinstance(amount, float), "Withdrawal amount must be a floating point value"
        assert amount > 0, "Withdrawal amount must be positive."

        # Check to see if amount is valid
        if amount > self._balance + 250:
            print("Transaction denied. Exceeds overdraft limit.")
            return False

        # Check to see if balance is postive
        elif self._balance > 0:
            withdrawalTransaction = Transaction("withdrawal", amount)
            self.addTransaction(withdrawalTransaction)
            self._balance = self._balance - amount
            print("Withdrawal: $%.2f\n" % amount)

            # Check to see if withdrawal made the balance negative
            if self._balance < 0:
                # if balance is negative apply over draft fee
                self._balance = self._balance - BankAccount._overdraftFee
                self.increaseOverdraftCounter()
                # Create a penalty transaction and add it to the transaction list
                penaltyTransaction = Transaction("penalty", BankAccount._overdraftFee)
                self.addTransaction(penaltyTransaction)
                print("Account is overdrawn. Overdraft fee applied.")

            return True


        else:
            print("Transaction denied.")
            return False


    # calculate and add interest to the account balance
    # @ensure interest is added to the balance
    def addInterest(self):
        # calculate interest and add it to the account balance
        interest = self._balance * BankAccount._interestRate
        self._balance = self._balance + interest

        # create a interest transaction object and add it to the transaction list
        transaction = Transaction("interest", interest)
        self.addTransaction(transaction)

        print("Interest of $%.2f applied." %interest)        

    # transfer an amount from one account to another account
    # @param amount: floating point, the amount to be deposited
    # @param otherAccount: BankAccount, the other account that is transfering an amount to this account
    # @require amount is a postive floating point number
    # @ensure amount is transfered from other account to this account if other account has suffiencent funds
    def transfer(self, amount:float, otherAccount):
        # Preconditions:
        # - The from_account must have sufficient funds or overdraft capacity.

        # Postconditions:
        # - If the transfer is successful, the amount is withdrawn from the 'from_account' and deposited into the 'to_account'.
        assert isinstance(amount, float), "Transfer amount must be a floating point value"
        assert amount > 0.0, "Amount must be positive"

        # check if the withdrawal is successful
        transferStatus = otherAccount.withdrawal(amount)

        # if the withdrawal is successful, deposit the amount into the account
        if(transferStatus):

            # create a transfert transaction object and add it to the transaction list
            transferTransaction = Transaction("transfer", amount)
            self.addTransaction(transferTransaction)

            # deposit the amount to this account
            self.deposit(amount)

            print("Transferred $%.2f from %s to %s." %(amount, otherAccount.getAccountNumber(), self._accountNumber))

        else:
            print("Transfer failed")


    # add a transaction object to the list of transactions
    # @param: transaction, a tranaction object
    # @require transaction is a valid transaction object
    def _addTransaction(self, transaction: Transaction):
        assert isinstance(transaction, Transaction), "transaction must be a valid transaction object"
        self._transactionList.append(transaction)
