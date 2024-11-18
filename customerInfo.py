# Authors: Cole Fuhrman, Bryce Kuberek, Jalen Neck, Trace Taylor, Dillon VanGlider
# Project 2
# CSEC 323
# customerInfo.py
# This file contains the address, name, and phone classes




# This class represents the data elements and methods required to implement an Address
# An Address is defined by a Street, City, and State abbreviation. Street and City are confined by length and without symbols. City cannot have numbers. 
# State abbreviations must be in the list of valid state abbreviations. 
class Address():
    

    # private global variable to declare list of valid states
    _VALID_STATES = {"VA","MD","NJ","PA","DE","NC","WV","DC"}

    # Constructs an address object
    # 
    # @param address, a list for address details
    #
    # @require address: must be 3 in length. First index is street, second the city, third the state abbreviation
    # @ensure name object is created
    def __init__(self, address: list):
        
        # Ensure length of address
        assert len(address) == 3, "Invalid address"

        # Ensure street is tuple
        assert isinstance(address[0], tuple), "Street must be of type tuple with number in first index, street in second"
        
        # Grab details of address/street
        street = address[0]
        streetNo = street[0]
        streetName = street[1]
        city = address[1]
        stateAbbrev = address[2]
    
        # Check street number/street + city + state abbrev
        assert isinstance(streetNo, str), "Street number should be a string"
        assert 1 <= len(streetNo)<= 5 and streetNo.isnumeric(), "Invalid street name"
        assert 1 <= len(streetName)<= 25 and streetName.replace(" ", '').isalpha(), "Invalid street name"
        assert 1 <= len(city)<= 30 and city.isalpha(), "Invalid city name"
        assert len(stateAbbrev) == 2 and stateAbbrev in Address._VALID_STATES, "Invalid state"
        
        # Store data in instance variables
        self._street = street[0] + ' ' + street[1]
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
    
    # Update street information
    # @param newStreet, the new street to change in the Address
    # @require street: must be tuple with first index between 1 and 5 numberic characters with no special characters, second index 
    # between 1 and 25 no special characters. Total of 30 characters
    # @ensure street is updated
    def updateStreet(self, newStreet: tuple)->None:

        # Ensure street is tuple
        assert isinstance(newStreet, tuple), "Street must be of type tuple with number in first index, street in second"

        # check street number + street name
        streetNo = newStreet[0]
        street = newStreet[1]

        assert isinstance(streetNo, str), "Street number should be a string"
        assert 1 <= len(streetNo)<= 5 and streetNo.isnumeric(), "Invalid street name: must be numeric"
        assert 1 <= len(street)<= 25 and street.replace(" ", '').isalpha(), "Invalid street name: cannot contain numnbers"

        # Store data in instance variable
        self._street = streetNo + " " + street

    # Update city information
    # @param newCity, the new street to change in the Address
    # @require city: must be between 1 and 30 characters with no special characters.
    # @ensure city is updated
    def updateCity(self, newCity: str)->None:
        
        # check city
        assert 1 <= len(newCity)<= 30 and newCity.isalpha(), "Invalid city name"
        
        # Store data in instance variable
        self._city = newCity

    # Update state information
    # @param newState, the new state to change in the Address
    # @require state: must be between 2 characters and within set of valid states
    # @ensure state is updated
    def updateState(self, newState: str)->None:
        
        # Check state abbreviation
        assert len(newState) == 2 and newState in Address._VALID_STATES, "Invalid state"

        # Store data in instance variable
        self._state = newState
    
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
    
    # Update first name
    # @param first, the new first name to change in the Name
    # @require firstName: must be between 1 and 25 characters with no special characters
    # @ensure first name is updated
    def updateFirstName(self, first: str)->None:
        
        # check first name
        assert 1 <= len(first) <= 25 and first.isalpha(), "Invalid first name."
        
        # Store data in instance variable
        self._firstName = first

    # Update last name
    # @param first, the new last name to change in the Name
    # @require lastName: must be between 1 and 40 characters with no special characters
    # @ensure last name is updated
    def updateLastName(self, last: str)->None:
        
        # check first name
        assert 1 <= len(last) <= 40 and last.isalpha(), "Invalid last name."
        
        # Store data in instance variable
        self._lastName = last

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
    
    # Update phone number
    # @param phone, the new phone name to change in the Phone
    # @require phone: must be all numeric digits, length is 10, cannot start with “0”
    # @ensure phone is updated
    def updatePhone(self, phone: str)->None:
        
        # Ensure valid phone number (does not include dashes)
        assert phone[0] != 0 and len(phone) == 10 and phone.isnumeric(), "Invalid phone number; remove any dashes"	
        
        # Store data in instance variable
        self._phone = phone
    
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
