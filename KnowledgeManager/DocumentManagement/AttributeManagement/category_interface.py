# 11/20/22

from .attribute_interface import AttributeInterface


class CategoryInterface(AttributeInterface):

    def __init__(self, document):
        super().__init__(identifier="#Category:", document=document)
        self.document = document
        self.name = "Category"

    def __str__(self):
        return self.document.category


    def load(self):
        self.document.category = self._get_value_after_identifier()

    def set(self, category):
        self._set_value_after_identifier(category)

    def get(self):
        return self.document.category
    

    
