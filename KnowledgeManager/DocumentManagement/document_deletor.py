# 11/20/22

import os

from .document_handler_base import DocumentHandlerBase
from .document_exceptions import FilenameNotFoundError


class DocumentDeletor(DocumentHandlerBase):

    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)

    def delete(self, doc_name):
        # Validate that doc_name is a string (not a path) and the doc exists
        assert(isinstance(doc_name, str))
        doc_name = self._ensure_dot_txt_suffix(doc_name)
        if not self._filename_exists(doc_name):
            raise FilenameNotFoundError(doc_name)

        doc_path = self._document_repo_path / doc_name
        os.remove(doc_path)
