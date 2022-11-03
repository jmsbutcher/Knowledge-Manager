# 10/29/22

import os
import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from KnowledgeManager.DocumentManagement.document import Document
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocument(TestBase):

    def test_can_create_document(self):
        doc = Document("", "")
        self.assertTrue(True)

    
    def test_document_path_matches_constructor_argument(self):
        doc = Document(os.getcwd(), "test_doc")
        self.assertTrue(doc._repo_path == os.getcwd())


    def test_document_name_matches_constructor_argument(self):
        doc = Document(os.getcwd(), "test_doc")
        self.assertTrue(doc.name == "test_doc")

