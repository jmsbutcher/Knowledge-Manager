# 9/26/22

import os
from pathlib import Path


class DocumentHandlerBase:

    def __init__(self, document_repo_path):
        assert(isinstance(document_repo_path, Path))
        self._document_repo_path = document_repo_path
        self._create_new_document_repo_if_doesnt_exist()

    def _create_new_document_repo_if_doesnt_exist(self):
        if not os.path.exists(self._document_repo_path):
            os.mkdir(self._document_repo_path)

    def _filename_exists(self, filename):
        filepath = self._document_repo_path / filename
        if os.path.exists(filepath):
            return True 
        else:
            return False

    def _ensure_dot_txt_suffix(self, filename):
        if filename[-4:] != ".txt":
            filename = filename + ".txt"
        return filename

