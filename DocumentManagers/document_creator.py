# 9/25/22

import os

from .document_base import DocumentBase
from .document_exceptions import FilenameAlreadyExistsError


class DocumentCreator(DocumentBase):

    def create_new_document_folder_if_doesnt_exist(self):
        if not os.path.exists(self._folder_name):
            os.mkdir(self._folder_name)


    def create_new_text_file_if_doesnt_exist(self, filename):
        # Validate filename
        filename = self._ensure_dot_txt_suffix(filename)

        # Make sure file with that name doesn't already exist
        if self._filename_exists(filename):
            raise FilenameAlreadyExistsError(filename)

        # Create the file (file gets closed right after creating it)
        filepath = self._folder_path / filename
        with open(filepath, 'w') as new_text_file:
            pass
