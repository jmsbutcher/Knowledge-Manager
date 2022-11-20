# 10/23/22

import os
import sys

sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from KnowledgeManager.DocumentManagement.document_editor import DocumentEditor
from KnowledgeManager.DocumentManagement.document_creator import DocumentCreator
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocumentEditor(TestBase):

    def test_can_create_documentEditor(self):
        doc_editor = DocumentEditor(TEST_DOCUMENT_REPO_PATH)
        self.assertTrue(True)

    def test_rename_document(self):
        OLD_NAME = "test_document.txt"
        OLD_FILE_PATH = TEST_DOCUMENT_REPO_PATH / OLD_NAME
        NEW_NAME = "final_document.txt"
        NEW_FILE_PATH = TEST_DOCUMENT_REPO_PATH / NEW_NAME

        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist(OLD_NAME)
        # Check if the file now exists in the correct location
        self.assertTrue(os.path.exists(OLD_FILE_PATH))

        # Now rename the document
        doc_editor = DocumentEditor(TEST_DOCUMENT_REPO_PATH)
        doc_editor.rename_document(OLD_NAME, NEW_NAME)

        self.assertFalse(os.path.exists(OLD_FILE_PATH))
        self.assertTrue(os.path.exists(NEW_FILE_PATH))

