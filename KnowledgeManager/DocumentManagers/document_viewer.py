# 9/25/22

from .document_handler_base import DocumentHandlerBase
from .document_exceptions import FilenameNotFoundError


class DocumentViewer(DocumentHandlerBase):

    def view_document_by_name(self, filename):
        # Validate filename
        filename = self._ensure_dot_txt_suffix(filename)

        # Return document contents as a string, if found
        if self._filename_exists(filename):
            filepath = self._document_repo_path / filename
            with open(filepath, "r") as f:
                file_contents = f.read()
                return file_contents
        else:
            raise FilenameNotFoundError(filename)