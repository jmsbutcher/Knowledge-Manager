# 10/9/22

from pathlib import Path
import glob
import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager/KnowledgeManager")

from DocumentManagement.AttributeManagement.name_interface import NameInterface
from DocumentManagement.AttributeManagement.content_interface import ContentInterface
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
            new_doc = Document(Path(doc_path))
            NameInterface(new_doc).load()
            ContentInterface(new_doc).load()
            CategoryInterface(new_doc).load()
            KeywordsInterface(new_doc).load()
            documents.append(new_doc)
        return documents


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

    
