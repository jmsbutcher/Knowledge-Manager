# 11/19/22


class InterfaceImplementationError(Exception):
    """ Used abstract base class as a concrete class, or 
    derived class failed to override an abstract method"""


class DocumentPathMissingError(Exception):
    """ Raise when trying to pass a document object to an attribute
    interface when the document's path attribute hasn't been set. """


class AttributeInterface:
    """ Abstract interface for handling document attribute reading and writing
    
        Derive from this interface with a specific document attribute to handle.
        Example: CategoryInterface(AttributeInterface) for handling a document's
        category.

        Input: a Document object
          *** The document object MUST have its path attribute set. This is how
              the attribute interfaces will load the other attributes.

        load() -- loads the document attribute str extracted from the document's
                physical file (defined by the document's [path] attribute) 
                into the local document object's attribute.

        set(new_value) -- overwrite the attribute value, or create it, both in
                the object's local attribute AND on the physical file.

        get() -- return the attribute value stored in the local document object
     """

    def __init__(self, identifier, document):
        self.identifier = identifier
        self.document = document
        if document.path is None or document.path == "":
            raise DocumentPathMissingError

    # pure virtual method - must override
    def __str__(self):
        raise InterfaceImplementationError
    
    # pure virtual method - must override
    def load(self):
        raise InterfaceImplementationError

    # pure virtual method - must override
    def set(self, new_value):
        raise InterfaceImplementationError

    # pure virtual method - must override
    def get(self):
        raise InterfaceImplementationError


    def _get_value_after_identifier(self):
        """ Returns string after identifier if found in the doc path
        Example:   #Category: Fiction
                   > returns "Fiction"
        """
        with open(self.document.path, "r") as doc:
            for line in doc.readlines():
                # Find line that contains identifier, e.g., "#Category:"
                if (line.find(self.identifier) != -1):
                    # Extract the string after the identifier
                    _, _, value = line.partition(self.identifier)
                    value = value.strip(' ')

                    # Return none if field after identifier is empty 
                    # (i.e., just contains a newline)
                    if len(value) > 0:
                        if value [0] == '\n':
                            return None
                    return value.strip()


    def _set_value_after_identifier(self, value):
        """ Writes the provided string value to file line after identifier,
        overwriting any existing value
        Example:    identifier="#Category:"
                    value="Fiction"
                    > writes line to file:
                    #Category: Fiction
        """
        assert(isinstance(value, str))

        lines = []
        with open(self.document.path, "r") as doc:
            lines = doc.readlines()

        with open(self.document.path, "w") as doc:
            replacement_line = self.identifier + " " + value + '\n'
            for line_num, line in enumerate(lines):
                if self.identifier in line:
                    lines[line_num] = replacement_line
                    doc.writelines(lines)
                    return
            
            # If identifier line not found, add it to the beginning
            doc.write(replacement_line)
            doc.writelines(lines)

