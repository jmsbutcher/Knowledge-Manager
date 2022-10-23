# 10/9/22

import glob

import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager/KnowledgeManager")

#$from .document_handler_base import DocumentHandlerBase
from DocumentManagers.document_handler_base import DocumentHandlerBase


class DocumentManager(DocumentHandlerBase):

    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)
        self._list_of_documents = self._load_documents() # Document paths
    
    def _load_documents(self):
        documents = []
        for filename in glob.glob(str(self._document_repo_path) + "/*"):
            documents.append(filename)
        return documents

    def get_list_of_document_names(self):
        """ Return a list of all the document names in the knowledge repo """
        # Remove path prefix
        prefix = str(self._document_repo_path) + "\\"
        extracted_document_names = \
            [d.replace(prefix, "") for d in self._list_of_documents]

        # Remove file extension suffix
        extracted_document_names = \
            [d[0:d.find(".")] for d in extracted_document_names if (d.find(".") != -1)]

        return extracted_document_names

