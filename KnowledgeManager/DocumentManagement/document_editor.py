# 10/23/22

import os
import platform
import subprocess
import sys


sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager/KnowledgeManager")

from DocumentManagement.document_handler_base import DocumentHandlerBase
from DocumentManagement.document_exceptions import FilenameNotFoundError


class DocumentEditor(DocumentHandlerBase):
    
    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)

    def open_document_in_text_editor(self, doc_name):
        """ Open the specified document in platform's default text editor """
        # Validate filename and add ".txt" if not already there
        doc_name = self._ensure_dot_txt_suffix(doc_name)

        if not self._filename_exists(doc_name):
            raise FilenameNotFoundError(doc_name)

        filepath = self._document_repo_path / doc_name
        if platform.system() == "Darwin":   # macOS
            subprocess.call(("open", filepath))
        elif platform.system() == "Windows": # Windows
            os.startfile(filepath)
        else:                               # Linux vairants
            subprocess.call(("xdg-open", filepath))
        

