# 9/26/22

import os
import sys
from pathlib import Path

ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
sys.path.append(ROOT)

from globals import DOCUMENT_FOLDER_NAME


class DocumentBase:

    def __init__(self):
        self._folder_name = DOCUMENT_FOLDER_NAME
        self._folder_path = Path(DOCUMENT_FOLDER_NAME)

    def _filename_exists(self, filename):
        #filepath = Path(DocumentBase.FOLDER_NAME) / filename
        filepath = self._folder_path / filename
        if os.path.exists(filepath):
            return True 
        else:
            return False

    def _ensure_dot_txt_suffix(self, filename):
        if filename[-4:] != ".txt":
            filename = filename + ".txt"
        return filename
