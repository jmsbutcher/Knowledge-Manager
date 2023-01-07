# 11/20/22

from .attribute_interface import AttributeInterface


class KeywordsInterface(AttributeInterface):
    """ Handles getting and setting a document's keywords attribute.
    
    A keyword acts as a "tag" or "label" for the document for helping with
    searching, grouping, and organizing documents.

    A document can have several keywords, and so this interface also includes
    add() and remove() methods, unlike most other atrribute interfaces that can
    only have one value.
    """

    name = "Keywords"

    def __init__(self, document):
        super().__init__(identifier="#Keywords:", document=document)
        self.document = document

    def __str__(self):
        return ", ".join(self.get())


    def load(self):
        kw_str = self._get_value_after_identifier()
        if kw_str is None:
            self.document.keywords = []
        else:
            self.document.keywords = [kw.strip() for kw in kw_str.split(',')]

    def set(self, new_keywords):
        if isinstance(new_keywords, list):
            kw_str = ", ".join(new_keywords)
            self._set_value_after_identifier(kw_str)
        elif isinstance(new_keywords, str):
            self._set_value_after_identifier(new_keywords)
        self.load()

    def get(self):
        return self.document.keywords

    def add(self, new_keyword):
        keywords = self.get()
        keywords.append(new_keyword)
        self.set(keywords)

    def remove(self, keyword_to_remove):
        keywords = self.get()
        keywords.remove(keyword_to_remove)
        self.set(keywords)

    
    

    
