# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGilder
# Project 2
# CSEC 323

from bankAccount import BankAccount
from customerInfo import Address, Name

# This module defines the Client class
# A class to represent the data elements and methods required to implement a Client

class Client:
    

    _nextClientNumber = 100 # private class variable that holds the next client number

    # Constructs a client
    # 
    # @param firstName: the first name of the account holder (String, must be between 1 and 25 characters with no special characters)
    # @param lastName: The user's last name (String, must be between 1 and 40 characters with no special characters))  
    # @param phone: The user's phone number (String, must be all numeric digits, length is 10, cannot start with “0”))
    # @param address: The user's address (Python list, must be size of 3 with street, city, and state abbreviation))
    # @param accountType: The user's type of inital account (String, must be either "Checking" or "Savings")
    #
    # @require firstName: must be between 1 and 25 characters with no special characters
    # @require lastName: must be between 1 and 40 characters with no special characters
    # @require phone: must be all numeric digits, length is 10, cannot start with “0”))
    # @ensure address: must be size of 3.
    # @ensure accountType: must be either "Checking" or "Savings"
    # @ensure unique client number is assigned
    def __init__(self,firstName: str, lastName: str, phone: str, address: list, accountType: str):
        

        # Preconditions:
        # - firstName must be a valid string of 1-25 alphabetic characters.
        # - lastName must be a valid string of 1-40 alphabetic characters.
        # - phone must be 10-digit phone number (all numeric digits, length is 10, cannot start with “0”).
        # - address must be a valid python list of 3 in size
        # - accountType must be a valid string either "Checking" or "Savings"

        # Postconditions:
        # - A unique client number is assigned.
        # - The client has a list of accounts.
  
        # Ensure valid phone number (does not include dashes)
        assert phone[0] != 0 and len(phone) == 10 and phone.isnumeric(), "Invalid phone number"	
        
        # use Address class to create address
        validAddress = Address(address)
        
        # ensure account type is valid
        assert accountType == "Checking" or accountType == "Savings"
        
        # create account list for client
        self._accounts = []
        
        # Add personal info
        self._name = Name(firstName, lastName)
        self._phone = phone
        self._address = validAddress
        
        # Open new account based on type
        self.openAccount(accountType)

        # Create client Number
        self._clientNumber = Client._nextClientNumber
        
        # Update next client number
        Client._nextClientNumber = Client._nextClientNumber = Client._nextClientNumber + 1

    ##
    # Define acessor methods
    ##


    # returns the phone of the client holder
    # @return: a string, the first name of the client holder
    def getPhone(self)->str:
        return self._phone
       
    # returns the address of the client holder
    # @return: an Address object, the address of the client holder
    def getAddress(self)->Address:
        return self._address
    

     # returns the first name of the client holder
    # @return: a string, the first name of the client holder
    def getFirstName(self)->str:
        return self._name.getFirstName()

    # returns the last name of the client holder
    # @return: a string, the last name of the client holder
    def getLastName(self)->str:
        return self._name.getLastName()
    
    # returns the client number
    # @return: an integer, the client number
    def getClientNumber(self)->int:
        return self._clientNumber
        
    # open an account based on type for the client
    # @param accountType: string, the type of bank account
    # @require accountType is either "Checking" or "Savings"
    # @ensure account is added to list of bank accounts for client
    def openAccount(self, accountType: str):

        # ensure account type is valid
        assert accountType == "Checking" or accountType == "Savings"

        # create a new Bank account + add to list of accounts for client
        self._accounts.append(BankAccount(0.0, accountType))

    # open an account based on type for the client
    # @param accountType: string, the type of bank account
    # @require accountType is either "Checking" or "Savings"
    # @ensure account is added to list of bank accounts for client
    def closeAccount(self, accountNumber: int)->bool:
        
        # To find account in list
        found = False
        i = 0

        # iterate accounts held by client
        while (i < len(self._accounts) and not found):
            
            # identify account number
            temp = self._accounts[i].getAccountNumber()

            # check if correct account
            if accountNumber == temp:
                account = self._accounts[i]
                found = True

        # ensure account number exists
        assert found, "Invalid account number"

        # Get balance + withdrawal all funds from account
        balance = account.getBalance()
        success = account.withdrawal(balance)

        return success

    # return the Client details in a string readable format
    # @return: The formatted, human readable string of the Client
    def displayClientDetails(self):
        # display first name, last name, client number, address, phone, and number of bank accounts on file
        return ("Client\nClient = %s\nClient Number = %d\nAddress: %s\nPhone = %s\n# of accounts: %d \n" %
        (self._name, self._clientNumber, str(self._address), self._phone, len(self._accounts)))

    # Checks a Client to see if it is equal to the second Client
    # @param other: the Client your are comparing the first Client with
    # @return result: True if this two Clients have the same names, client numbers, phones, addresses, and list of bank accounts
    def __eq__(self, other) -> bool :
        result = (self._name == other._name) and (self._clientNumber == other._clientNumber) and (self._address == other._address) and (self._transactionList == other._transactionList) and (self._overdraftCounter == other._overdraftCounter)
        return result 
                
    # return the Client details in a string readable format
    # @return: The formatted, human readable string of the Client
    def __repr__(self) -> str:
        # display first name, last name, client number, address, phone, and number of bank accounts on file
        return ("Client\nClient = %s\nClient Number = %d\nAddress: %s\nPhone = %s\n# of accounts: %d \n" %
        (self._name, self._clientNumber, str(self._address), self._phone, len(self._accounts)))


    # return the Client details in a string readable format
    # @return: The formatted, human readable string of the Client
    def __str__(self) -> str:
       # display first name, last name, client number, address, phone, and number of bank accounts on file
        return ("Client\nClient = %s\nClient Number = %d\nAddress: %s\nPhone = %s\n# of accounts: %d \n" %
        (self._name, self._clientNumber, str(self._address), self._phone, len(self._accounts)))
    


    # ** MAY NOT NEED. IF WE WANT, WE CAN PRINT THE NUMBERS AND TYPE OF ACCOUNTS INSTEAD OF THE TOTAL NUMBER of ACCOUNTS IN THE displayClientDetails, __REPR__ AND __STR__ METHODS

    # converts the bank account list into a readable string 
    # @return: a string,  accountString: a string of all of the bank accounts from the accounts list
    def _displayClientAccounts(self):
        accountList = self._accounts
        accountString = ""

        # loop through the transactionList
        for bankAccount in accountList:

            # Grab the bank account number + type and add it to the  bank account string
            accountString = accountString + str(bankAccount.getAccountNumber()) + " " + bankAccount.getAccountType() + "\n"

        return accountString    


# For testing purposes
if __name__ == '__main__':
    
    address = ["Henry St", "Ashland", "VA"]
    newClient = Client("Johnny", "Cash", "8045559042", address, "Checking")
    print("success")