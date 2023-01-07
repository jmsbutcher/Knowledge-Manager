# 9/26/22

import os
from pathlib import Path

from Utils.common_functions import ensure_dot_txt_suffix

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
        return ensure_dot_txt_suffix(filename)

