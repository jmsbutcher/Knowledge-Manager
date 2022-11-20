# 11/19/22

class Attribute:

    def __init__(self, identifier, name, type):

        # How attribute is stored in document - E.g., "#Category:"
        self.identifier = identifier 
        # How attribute is represented as a string - E.g., "Category"
        self.name = name
        # The kind of attribute: "String", "List"
        self.type = type
