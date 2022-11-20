# 11/19/22

from Utils.common_functions import ensure_dot_txt_suffix

class InterfaceImplementationError:
    """ Used abstract base class as a concrete class, or 
    derived class failed to override an abstract method"""


class AttributeInterface:
    """ Abstract interface for handling document attribute reading and writing """

    def __init__(self, identifier, document):
        self.identifier = identifier
        self.document = document
        self.doc_path = ensure_dot_txt_suffix(str(self.document.path))

    # pure virtual method - must override
    def __str__(self):
        raise InterfaceImplementationError

    def _load_attribute(self):
        pass

    def _set_attribute(self):
        pass

    def _get_value_after_identifier(self):
        """ Returns string after identifier if found in the doc path
        Example:   #Category: Fiction
                   > returns "Fiction"
        """
        with open(self.doc_path, "r") as doc:
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
        with open(self.doc_path, "r") as doc:
            lines = doc.readlines()

        with open(self.doc_path, "w") as doc:
            replacement_line = self.identifier + " " + value + '\n'
            for line_num, line in enumerate(lines):
                if self.identifier in line:
                    lines[line_num] = replacement_line
                    doc.writelines(lines)
                    return
            
            # If identifier line not found, add it to the beginning
            doc.write(replacement_line)
            doc.writelines(lines)


    # pure virtual method - must override
    def load(self):
        raise InterfaceImplementationError

    # pure virtual method - must override
    def set(self):
        raise InterfaceImplementationError

    # pure virtual method - must override
    def get(self):
        raise InterfaceImplementationError



if __name__ == "__main__":

    import os
    from pathlib import Path

    class Doc:
        def __init__(self, name):
            self.path = Path(os.getcwd()) / name

    test_doc = Doc("test.txt")

    att_int = AttributeInterface("#Category:", test_doc)


    category = att_int._get_value_after_identifier()
    print(category)

    att_int._set_value_after_identifier("gluey")
    
    category = att_int._get_value_after_identifier()
    print(category)

    print("done")
