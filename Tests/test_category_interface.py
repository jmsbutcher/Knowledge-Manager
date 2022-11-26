# 11/25/22

import os

from KnowledgeManager.DocumentManagement.document_creator \
    import DocumentCreator
from KnowledgeManager.DocumentManagement.document import Document
from KnowledgeManager.DocumentManagement.AttributeManagement.category_interface \
    import CategoryInterface

from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestCategoryInterface(TestBase):

    def setUp(self):
        TestBase.setUp(self)

        self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        self.doc_creator.create_new_text_file_if_doesnt_exist("test")

        self.doc_name = "test"
        self.doc_path = TEST_DOCUMENT_REPO_PATH / (self.doc_name + ".txt")
        self.assertTrue(os.path.exists(self.doc_path))

        self.doc = Document(self.doc_path)
        self.category_I = CategoryInterface(self.doc)
        self.category_I.load()
        self.test_category = "test category"

    #------------------------------------------------------------------------------------

    def test_can_create(self):
        self.assertTrue(True)

    def test_set_category(self):
        # Try default category
        self.category_I.set(self.test_category)
        self.assertEqual(self.category_I.get(), self.test_category)
        # Now try a different category
        self.category_I.set("AnotherCategory")
        self.assertEqual(self.category_I.get(), "AnotherCategory")


    def test_get_method_returns_empty_string_when_no_category(self):
        self.assertEqual(self.category_I.get(), "")

    def test_str_method(self):
        self.category_I.set(self.test_category)
        self.assertEqual(str(self.category_I), self.test_category)

