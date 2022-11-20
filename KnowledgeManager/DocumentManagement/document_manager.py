# 10/9/22

import glob

import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager/KnowledgeManager")

from DocumentManagement.AttributeManagement.category_interface import CategoryInterface
from DocumentManagement.AttributeManagement.keywords_interface import KeywordsInterface

from DocumentManagement.document_handler_base import DocumentHandlerBase
from DocumentManagement.document import Document


class DocumentManager(DocumentHandlerBase):
    """ Responsible for listing, loading, and searching for documents """

    CATEGORY_IDENTIFIER = "#Category:"
    KEYWORDS_IDENTIFIER = "#Keywords:"

    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)
        self._list_of_documents = self._load_documents() # Document paths
    

    def _load_documents(self):
        documents = []
        for doc_path in glob.glob(str(self._document_repo_path) + "/*"):
            documents.append(self._load_document_from_path(doc_path))
        return documents


    def _load_document_from_path(self, doc_path):
        """ Load a new document object from the text file at [doc_path] """
        doc_name = self._extract_doc_name_from_path(doc_path)
        doc = Document(self._document_repo_path, doc_name)
        #doc.category = self._load_doc_category(doc_path)
        CategoryInterface(doc).load()
        KeywordsInterface(doc).load()
        # category_interface = CategoryInterface(doc)
        # category_interface.load()
        # doc.keywords = self._load_doc_keywords(doc_path)
        doc.contents = self._load_doc_contents(doc_path)
        return doc


    def _load_doc_category(self, doc_path):
        return self._get_value_after_identifier(doc_path, self.CATEGORY_IDENTIFIER)


    def _load_doc_keywords(self, doc_path):
        keywords_string = self._get_value_after_identifier( \
            doc_path, self.KEYWORDS_IDENTIFIER)
        if keywords_string is None:
            return []
        return [keyword.strip() for keyword in keywords_string.split(',')]


    def _load_doc_contents(self, doc_path):
        """ Get all contents, excluding special identifier lines like category """
        contents = ""
        with open(doc_path, "r") as doc:
            for line in doc.readlines():
                if  self.CATEGORY_IDENTIFIER in line or \
                    self.KEYWORDS_IDENTIFIER in line:
                    continue 
                else:
                    contents += line
        return contents
    

    def _get_value_after_identifier(self, doc_path, identifier):
        """ 
        Returns string after identifier if found in the doc path
        
        Example:
            doc_path = "Path/document.txt"
            identifier = "#Category:"
            > opens document.txt:
                ...
                #Category: Fiction
                ...

            > returns "Fiction"
        """
        with open(doc_path, "r") as doc:
            for line in doc.readlines():
                # Find line that contains identifier, e.g., "#Category:"
                if (line.find(identifier) != -1):
                    # Extract the string after the identifier
                    _, _, value = line.partition(identifier)
                    value = value.strip(' ')

                    # Return none if field after identifier is empty 
                    # (i.e., just contains a newline)
                    if len(value) > 0:
                        if value [0] == '\n':
                            return None
                    return value.strip()


    def _extract_doc_name_from_path(self, doc_path, remove_extension=True):
        """ Extracts just the name from the file path
        Example: 
            doc_path = "C:/Users/Documents/my_doc.txt"
            > returns "my_doc"
        """
        # Remove path prefix, e.g.: "C://Documents/doc.txt"  -->  "doc.txt" 
        path_prefix = str(self._document_repo_path) + "\\"
        doc_name_with_extension = str(doc_path).replace(path_prefix, "")

        if remove_extension:
            # Extract all characters up to the first "."
            ext_begin_index = doc_name_with_extension.find(".")
            doc_name = doc_name_with_extension[0 : ext_begin_index]
            return doc_name 
        else:
            return doc_name_with_extension


    def get_documents(self):
        return self._list_of_documents


    def get_document_by_name(self, name):
        for doc in self._list_of_documents:
            if name == doc.name:
                return doc 
        raise FileNotFoundError


    def get_list_of_document_names(self):
        """ Return a list of all the document names in the knowledge repo """
        return [doc.name for doc in self._list_of_documents]


    def get_all_categories(self):
        return list(set([doc.category for doc in self._list_of_documents if doc.category is not None]))


    def get_all_keywords(self):
        keywords_set = set()
        for doc in self._list_of_documents:
            for keyword in doc.keywords:
                keywords_set.add(keyword)
        return list(keywords_set)


    def search_for_document(self, name_substring, return_name_only=True):
        """ 
        Return a list of documents with names 
        that contain the given substring 
        """
        if return_name_only:
            doc_names = self.get_list_of_document_names()
            return [doc_name for doc_name in doc_names \
                 if name_substring in doc_name]
        else:
            return[doc for doc in self._list_of_documents \
                if name_substring in doc.name]


    def filter_documents_by_category(self, category):
        """ Return a list of documents with the given category """
        return [doc for doc in self._list_of_documents if doc.category == category]


    def filter_documents_by_keyword(self, keywords):
        """ 
        Return a list of documents that each have all the keywords listed
        in [keywords] input, which may be either a single keyword string or
        a list of keyword strings.
        """
        matches = []

        # If multiple keywords, filter out documents that don't have ALL keywords
        if (isinstance(keywords, list)):

            for doc in self._list_of_documents.copy():
                all_keywords_present = True
                for keyword in keywords:
                    if keyword not in doc.keywords:
                        all_keywords_present = False
                        break
                if all_keywords_present:
                    matches.append(doc)

        # If just one keyword, filter out documents that don't contain the keyword
        else:

            for doc in self._list_of_documents.copy():
                if keywords in doc.keywords:
                    matches.append(doc)

        return matches



if __name__ == "__main__":

    from pathlib import Path
    import os
    root = Path(os.getcwd())
    doc_repo = root / "KnowledgeManager" / "km_Documents"
    print(doc_repo)

    doc_manager = DocumentManager(doc_repo)

    print(doc_manager.get_list_of_document_names())
    print(doc_manager.filter_documents_by_category("gopher")[0].name)

    
