# 11/20/22

import os

from KnowledgeManager.DocumentManagement.document_creator import DocumentCreator
from KnowledgeManager.DocumentManagement.document_deletor import DocumentDeletor
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocumentDeletor(TestBase):

    def test_delete_document(self):
        TEST_DOC_NAME = "test_document.txt"
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist(TEST_DOC_NAME)

        # Check that document exists
        TEST_DOC_PATH = TEST_DOCUMENT_REPO_PATH / TEST_DOC_NAME
        self.assertTrue(os.path.exists(TEST_DOC_PATH))

        # Delete the document
        doc_deletor = DocumentDeletor(TEST_DOCUMENT_REPO_PATH)
        doc_deletor.delete(TEST_DOC_NAME)

        # Check that the document no longer exists
        self.assertFalse(os.path.exists(TEST_DOC_PATH))
        