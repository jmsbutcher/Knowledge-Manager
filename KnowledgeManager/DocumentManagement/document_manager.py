# 10/9/22

from pathlib import Path
import glob
import sys
#sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager/KnowledgeManager")
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from DocumentManagement.AttributeManagement.name_interface import NameInterface
from DocumentManagement.AttributeManagement.content_interface import ContentInterface
from DocumentManagement.AttributeManagement.category_interface import CategoryInterface
from DocumentManagement.AttributeManagement.keywords_interface import KeywordsInterface

from DocumentManagement.document_handler_base import DocumentHandlerBase
from DocumentManagement.document import Document


class DocumentManager(DocumentHandlerBase):
    """ Responsible for listing, loading, and searching for documents """

    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)
        self._list_of_documents = []
        self.load_documents()
        self.active_search_term = ""
        self.active_filters = {"Category":[], "Keywords":[]}
    
    def load_documents(self):
        self._list_of_documents = []
        for doc_path in glob.glob(str(self._document_repo_path) + "/*"):
            new_doc = Document(Path(doc_path))
            NameInterface(new_doc).load()
            ContentInterface(new_doc).load()
            CategoryInterface(new_doc).load()
            KeywordsInterface(new_doc).load()
            self._list_of_documents.append(new_doc)


    def set_active_search_term(self, search_term):
        self.active_search_term = search_term

    def set_active_filters(self, attribute, filters):
        self.active_filters[attribute] = filters

    def add_active_filter(self, attribute, filter):
        if filter is not None and filter != "":
            self.active_filters[attribute].append(filter)

    def remove_active_filter(self, attribute, filter):
        self.active_filters[attribute].remove(filter)

    def get_documents(self):
        """ Return all documents that meet search and filter criteria """
        search_matches = self.search_for_document(self.active_search_term, 
            return_name_only=False)
        print([doc.name for doc in search_matches])
        category_matches = self.filter_by_category(self.active_filters["Category"])
        print([doc.name for doc in category_matches])
        keywords_matches = self.filter_by_keyword(self.active_filters["Keywords"])
        print([doc.name for doc in keywords_matches])
        matches = []
        for d in self._list_of_documents:
            if d in search_matches and \
                d in category_matches and \
                d in keywords_matches:
                matches.append(d)
        return matches


    def get_document_by_name(self, name):
        for doc in self._list_of_documents:
            if name == doc.name:
                return doc 
        raise FileNotFoundError


    def get_list_of_names(self):
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
            doc_names = self.get_list_of_names()
            return [doc_name for doc_name in doc_names \
                 if name_substring in doc_name]
        else:
            return[doc for doc in self._list_of_documents \
                if name_substring in doc.name]


    def filter_by_category(self, category):
        """ Return a list of documents with the given category
        Category can be a single category string or a list of categories
        that are all acceptable. """
        if category is None or category == []:
            return self._list_of_documents
        if isinstance(category, str):
            return [d for d in self._list_of_documents if d.category == category]
        elif isinstance(category, list):
            return [d for d in self._list_of_documents if d.category in category]


    def filter_by_keyword(self, keywords):
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

