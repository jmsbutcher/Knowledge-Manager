# 11/24/22

import os

from .attribute_interface import AttributeInterface, ensure_dot_txt_suffix


class NameInterface(AttributeInterface):
    """ 
    Slightly different from the other interfaces because it deals directly with
    the document's file name, which is not included in the document's physical
    content denoted by an identifier (i.e., it doesn't have a "#Name:" 
    identifier.) And so it doesn't use _set- or _get_value_after_identifier.
    """

    name = "Name"

    def __init__(self, document):
        super().__init__(identifier="", document=document)
        self.document = document

    def __str__(self):
        return self.get()


    def load(self):
        self.document.name = self._extract_doc_name_from_path()

    def set(self, new_name):
        self._rename_document(new_name)

    def get(self):
        if self.document.name is None:
            return ""
        return self.document.name
    

    def _rename_document(self, new_name):
        old_path = self.document.path
        new_path = self.document.path.parent / ensure_dot_txt_suffix(new_name)
        os.rename(old_path, new_path)
        self.document.path = new_path
        self.load()


    def _extract_doc_name_from_path(self, include_extension=False):
        if include_extension:
            return self.document.path.name
        else:
            return self.document.path.stem
    

