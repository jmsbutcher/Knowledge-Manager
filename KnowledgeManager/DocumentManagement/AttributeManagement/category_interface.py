# 11/20/22

from .attribute_interface import AttributeInterface


class CategoryInterface(AttributeInterface):

    name = "Category"

    def __init__(self, document):
        super().__init__(identifier="#Category:", document=document)
        self.document = document

    def __str__(self):
        return self.get()


    def load(self):
        self.document.category = self._get_value_after_identifier()

    def set(self, new_category):
        self._set_value_after_identifier(new_category)
        self.load()

    def get(self):
        if self.document.category is None:
            return ""
        return self.document.category
    

    
