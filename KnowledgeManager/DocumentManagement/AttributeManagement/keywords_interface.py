# 11/20/22

from .attribute_interface import AttributeInterface


class KeywordsInterface(AttributeInterface):

    def __init__(self, document):
        super().__init__(identifier="#Keywords:", document=document)
        self.document = document
        self.name = "Keywords"

    def __str__(self):
        return ", ".join(self.document.keywords)


    def load(self):
        kw_str = self._get_value_after_identifier()
        if kw_str is None:
            self.document.keywords = []
        else:
            self.document.keywords = [kw.strip() for kw in kw_str.split(',')]

    def set(self, keywords):
        if isinstance(keywords, list):
            kw_str = ", ".join(keywords)
            self._set_value_after_identifier(kw_str)
        elif isinstance(keywords, str):
            self._set_value_after_identifier(kw_str)

    def get(self):
        return self.document.keywords

    
    

    
