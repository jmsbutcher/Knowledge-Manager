# 9/25/22

from Utils.common_functions import print_banner_line
from .document_handler_base import DocumentHandlerBase
from .document_exceptions import FilenameNotFoundError


class DocumentViewer(DocumentHandlerBase):

    def __init__(self, document_repo_path):
        super().__init__(document_repo_path)

    def get_document_contents(self, filename):
        """ Return the specified document's contents as a string """
        # Validate filename and add ".txt" if not already there
        filename = self._ensure_dot_txt_suffix(filename)

        # Return document contents as a string, if found
        if self._filename_exists(filename):
            filepath = self._document_repo_path / filename
            with open(filepath, "r") as f:
                file_contents = f.read()
                return file_contents
        else:
            raise FilenameNotFoundError(filename)

    def print_document_to_console(self, filename):
        """ Print the specified document's contents to the console with banners """
        file_contents = self.get_document_contents(filename)

        print()
        print_banner_line(filename)
        print(file_contents)
        print_banner_line(" END ")



