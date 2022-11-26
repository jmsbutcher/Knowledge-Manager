# 11/25/22

import os

from KnowledgeManager.DocumentManagement.document_creator \
    import DocumentCreator
from KnowledgeManager.DocumentManagement.document import Document
from KnowledgeManager.DocumentManagement.AttributeManagement.name_interface \
    import NameInterface

from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestNameInterface(TestBase):

    def setUp(self):
        TestBase.setUp(self)

        self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        self.doc_creator.create_new_text_file_if_doesnt_exist("test")

        self.doc_name = "test"
        self.doc_path = TEST_DOCUMENT_REPO_PATH / (self.doc_name + ".txt")
        self.assertTrue(os.path.exists(self.doc_path))

        self.doc = Document(self.doc_path)
        self.name_I = NameInterface(self.doc)
        self.name_I.load()

    #------------------------------------------------------------------------------------

    def test_can_create(self):
        self.assertTrue(True)

    def test_get_name(self):
        self.assertEqual(self.name_I.get(), self.doc_name)

    def test_str_method(self):
        self.assertCountEqual(str(self.name_I), self.doc_name)

    def test_extract_doc_name_from_path(self):
        extracted_doc_name = self.name_I._extract_doc_name_from_path(include_extension=True)
        self.assertEqual(extracted_doc_name, "test.txt")
        extracted_doc_name = self.name_I._extract_doc_name_from_path(include_extension=False)
        self.assertEqual(extracted_doc_name, "test")

    def test_rename_document(self):
        NEW_NAME = "final_document"
        NEW_FILE_PATH = TEST_DOCUMENT_REPO_PATH / (NEW_NAME + ".txt")

        # Rename the document
        self.name_I._rename_document(NEW_NAME)

        # Check if the document's new name is correct
        self.assertEqual(self.name_I.get(), NEW_NAME)

        # Check that the document's file name also changed
        self.assertFalse(os.path.exists(self.doc_path))
        self.assertTrue(os.path.exists(NEW_FILE_PATH))