# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# Project 2
# CSEC 323
# customerInfo.py
# This file contains the address, name, and phone classes




# This class represents the data elements and methods required to implement an Address
# An Address is defined by a Street, City, and State abbreviation. Street and City are confined by length and without symbols. City cannot have numbers. 
# State abbreviations must be in the list of valid state abbreviations. 
class Address():
    

    # Constructs an address object
    # 
    # @param address, a list for address details
    #
    # @require address: must be 3 in length. First index is street, second the city, third the state abbreviation
    # @ensure name object is created
    def __init__(self, address: list):
        
        # Ensure length of address
        assert len(address) == 3, "Invalid address"
        
        # Grab details of address
        street = address[0]
        city = address[1]
        stateAbbrev = address[2]
        
        #list of valid states
        validStates = ["VA","MD","NJ","PA","DE","NC","WV","DC"]
        
        # Check street + city + state abbrev
        assert 1 <= len(street)<= 30 and street.isalnum(), "Invalid street name"
        assert 1 <= len(city)<= 30 and city.isalpha(), "Invalid city name"
        assert len(stateAbbrev) == 2 and stateAbbrev in validStates, "Invalid state"
        
        # Store data in instance variables
        self._street = street
        self._city = city
        self._state = stateAbbrev

    # Return the street information
    # @return street, a string
    def getStreet(self)->str:
        return self._street

    # Return the city information
    # @return city, a string
    def getCity(self)->str:
        return self._city
    
    # Return the state information
    # @return state, a string
    def getState(self)->str:
        return self._state
    
    # @return result: True if this two Addresses have the same streets, citys, and state abbreviations
    def __eq__(self, other) -> bool :
        result = (self._street == other._street) and (self._city == other._city) and (self._state == other._state)
        return result 

    # return the Address details in a string readable format
    # @return: The formatted, human readable string of the Address
    def __str__(self) -> str:
        return "{} {}, {}".format(self._street, self._city, self._state)

    # return the Address details in a string readable format
    # @return: The formatted, human readable string of the Address
    def __repr__(self)->str:
        return "{} {}, {}".format(self._street, self._city, self._state)

# This class represents the data elements and methods required to implement a Name
# A Name is defined by a first and last name with strict parameters on length and characters.
class Name():
    
    # Constructs a name object
    # 
    # @param firstName, a string
    # @param lastName, a string
    #
    # @require firstName: must be between 1 and 25 characters with no special characters
    # @require lastName: must be between 1 and 40 characters with no special characters
    # @ensure name object is created
    def __init__(self, firstName: str, lastName: str):
        
        assert 1 <= len(firstName) <= 25 and firstName.isalpha(), "Invalid first name."
        assert 1 <= len(lastName) <= 40 and lastName.isalpha(), "Invalid last name."
        
        self._firstName = firstName # First name
        self._lastName = lastName # Last name   
        
    # Return the first name
    # @return firstName, a string
    def getFirstName(self):
        return self._firstName
    
    # Return the last name
    # @return lastName, a string
    def getLastName(self):
        return self._lastName
    
    # @return result: True if this two Names have the same firsts and lasts names  
    def __eq__(self, other) -> bool :
        result = (self._firstName == other._firstName) and (self._lastName == other._lastName)
        return result 

    # return the Name in a string readable format
    # @return: The formatted, human readable string of the Name
    def __str__(self) -> str:
        return "{} {}".format(self._firstName, self._lastName)

    # return the Name details in a string readable format
    # @return: The formatted, human readable string of the Name
    def __repr__(self)->str:
        return "{} {}".format(self._firstName, self._lastName)



# This class represents the data elements and methods required to implement a Phone
# A Phone is defined by a string of 10 digits without symbols which cannot start at 0.
class Phone():

    def __init__(self, phone: str):

        # Constructs a name object
        # 
        # @param phone, a string
        #
        # @require phone: must be all numeric digits, length is 10, cannot start with “0”
        # @ensure Phone object is created

        # Ensure valid phone number (does not include dashes)
        assert phone[0] != 0 and len(phone) == 10 and phone.isnumeric(), "Invalid phone number; remove any dashes"	

        self._phone = phone  # Phone Number

    # Return the Phone
    # @return phone, a string
    def getPhone(self)->str:

        return self._phone
    
    # @return result: True if this two Phones are the same
    def __eq__(self, other) -> bool :
        result = (self._phone == other._phone)
        return result 

    # return the Phone in a string readable format
    # @return: The formatted, human readable string of the Phone
    def __str__(self) -> str:
        
        # create new string
        newStr = ""

        # iterate phone number
        i = 0
        while i < len(self._phone):

            # do not add dash at start or end; do add in between 3 numbers
            if i != 0 and i != 9 and i % 3 == 0:
                newStr = newStr + "-"

            # update new string
            newStr = newStr + self._phone[i]
            i = i + 1

        #return formatted string
        return "{}".format(newStr)

    # return the Phone details in a string readable format
    # @return: The formatted, human readable string of the Phone
    def __repr__(self)->str:

        # create new string
        newStr = ""

        # iterate phone number
        i = 0
        while i < len(self._phone):

            # do not add dash at start or end; do add in between 3 numbers
            if i != 0 and i != 9 and i % 3 == 0:
                newStr = newStr + "-"

            # update new string
            newStr = newStr + self._phone[i]
            i = i + 1

        #return formatted string
        return "{}".format(newStr)