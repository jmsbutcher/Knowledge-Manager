# 10/29/22

import os
import sys
from pathlib import Path

sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from KnowledgeManager.DocumentManagement.document import Document
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocument(TestBase):

    def test_can_create_document(self):
        doc = Document("")
        self.assertTrue(True)

    
    def test_document_path_matches_constructor_argument(self):
        # "path" argument can be a Path object
        doc = Document(Path(os.getcwd()) / "test_doc.txt")
        self.assertEqual(doc.path, Path(os.getcwd()) / "test_doc.txt")
        # "path" argument can also be a string object
        doc = Document(str(os.getcwd()) + "/test_doc.txt")
        self.assertEqual(doc.path, Path(os.getcwd()) / "test_doc.txt")
