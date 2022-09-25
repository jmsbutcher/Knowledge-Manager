# 9/25/22

import os
import sys
from pathlib import Path

ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
sys.path.append(ROOT)

from globals import DOCUMENT_FOLDER_NAME


class DocumentCreator:


    def __init__(self):
        pass


    def create_new_document_folder_if_doesnt_exist(self):
        if not os.path.exists(DOCUMENT_FOLDER_NAME):
            os.mkdir(DOCUMENT_FOLDER_NAME)


    def create_new_text_file_if_doesnt_exist(self, filename):
        # Validate filename
        filename = self._ensure_dot_txt_suffix(filename)

        # Make sure file with that name doesn't already exist
        if self._check_if_filename_exists(filename):
            raise FilenameAlreadyExistsError(filename)

        # Create the file (file gets closed right after creating it)
        filepath = Path(DOCUMENT_FOLDER_NAME) / filename
        with open(filepath, 'w') as new_text_file:
            pass


    
    #------------------------------------------------------------------------------------
    # Helper functions

    def _check_if_filename_exists(self, filename):
        filepath = Path(DOCUMENT_FOLDER_NAME) / filename
        if os.path.exists(filepath):
            return True 
        else:
            return False

    def _ensure_dot_txt_suffix(self, filename):
        if filename[-4:] != ".txt":
            filename = filename + ".txt"
        return filename




class FilenameAlreadyExistsError(Exception):

    def __init__(self, filename):
        self.filename = filename
        super().__init__(self.filename)
