class Name:
    
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
