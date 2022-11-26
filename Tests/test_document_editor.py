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

