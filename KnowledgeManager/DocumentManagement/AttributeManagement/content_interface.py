# 11/24/22

from .attribute_interface import AttributeInterface


class ContentInterface(AttributeInterface):
    """ 
    Slightly different from the other interfaces because it deals directly with
    the document's contents, which is not denoted by an identifier 
    (i.e., it doesn't have a "#Contents:" identifier.) And so it doesn't use 
    _set- or _get_value_after_identifier.
    """

    name = "Content"

    def __init__(self, document):
        super().__init__(identifier="", document=document)
        self.document = document

    def __str__(self):
        return self.get()


    def load(self):
        self.document.content = self._load_content()

    def set(self, new_content):
        self._overwrite_content(new_content)

    def get(self):
        return self.document.content.strip()


    def _overwrite_content(self, new_content):
        # Gather all attribute lines to be written to top of file
        attribute_lines = []
        lines = self._load_entire_file_lines()
        for line in lines:
            if self._is_attribute_line(line):
                attribute_lines.append(line)

        with open(self.document.path, "w") as doc:
            # Write all attribute lines first to top of file (if any)
            if len(attribute_lines) > 0:
                for line in attribute_lines:
                    doc.write(line)
                # Separate attributes and contents by a blank line 
                doc.write('\n')
            # Write the contents afterward
            doc.write(new_content)
        
        self.load()
        

    def _load_entire_file_lines(self):
        with open(self.document.path, "r") as doc:
            return doc.readlines()

    def _load_content(self):
        """ Get all lines that don't begin with an identifier, 
        excluding special identifier lines like category """
        contents = ""
        with open(self.document.path, "r") as doc:
            for line in doc.readlines():
                if not self._is_attribute_line(line):
                    contents += line
        return contents

    def _is_attribute_line(self, line):
        """ return True if an identifier is detected """
        hash_detected = False
        for ch in line:
            if ch == '#':
                hash_detected = True
            if hash_detected and ch == ':':
                return True 
        return False