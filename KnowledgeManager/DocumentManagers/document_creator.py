# 9/25/22

from .document_handler_base import DocumentHandlerBase
from .document_exceptions import FilenameAlreadyExistsError


class DocumentCreator(DocumentHandlerBase):

    def create_new_text_file_if_doesnt_exist(self, filename):
        # Validate filename
        filename = self._ensure_dot_txt_suffix(filename)

        # Make sure file with that name doesn't already exist
        if self._filename_exists(filename):
            raise FilenameAlreadyExistsError(filename)

        # Create the file (file gets closed right after creating it)
        filepath = self._document_repo_path / filename
        with open(filepath, 'w') as new_text_file:
            pass
