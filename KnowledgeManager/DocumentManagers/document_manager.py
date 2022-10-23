# 10/9/22

import glob

from .document_handler_base import DocumentHandlerBase


class DocumentManager(DocumentHandlerBase):

    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)
        self._list_of_documents = self._load_documents()
    
    def _load_documents(self):
        documents = []
        for filename in glob.glob(str(self._document_repo_path) + "/*"):
            documents.append(filename)
        return documents

