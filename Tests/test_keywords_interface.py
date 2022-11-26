# 11/25/22

import os

from KnowledgeManager.DocumentManagement.document_creator \
    import DocumentCreator
from KnowledgeManager.DocumentManagement.document import Document
from KnowledgeManager.DocumentManagement.AttributeManagement.keywords_interface \
    import KeywordsInterface

from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestKeywordsInterface(TestBase):

    def setUp(self):
        TestBase.setUp(self)

        self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        self.doc_creator.create_new_text_file_if_doesnt_exist("test")

        self.doc_name = "test"
        self.doc_path = TEST_DOCUMENT_REPO_PATH / (self.doc_name + ".txt")
        self.assertTrue(os.path.exists(self.doc_path))

        self.doc = Document(self.doc_path)
        self.keywords_I = KeywordsInterface(self.doc)
        self.keywords_I.load()
        self.test_keywords = ["kw1", "kw2"] 

    #--------------------------------------------------------------------------

    def test_can_create(self):
        self.assertTrue(True)

    def test_set_keywords(self):
        # Try default keywords
        self.keywords_I.set(self.test_keywords)
        self.assertEqual(self.keywords_I.get(), self.test_keywords)
        # Now try different keywords
        self.keywords_I.set(["kw3"])
        self.assertEqual(self.keywords_I.get(), ["kw3"])

    def test_get_method_returns_empty_list_when_no_keywords(self):
        self.assertEqual(self.keywords_I.get(), [])

    def test_str_method(self):
        self.keywords_I.set(self.test_keywords)
        self.assertEqual(str(self.keywords_I), ', '.join(self.test_keywords))

    def test_str_method_returns_empty_string_when_no_keywords(self):
        self.keywords_I.set([])
        self.assertEqual(str(self.keywords_I), "")

    def test_add_keyword(self):
        self.keywords_I.set(["kw1", "kw2"])
        self.assertEqual(self.keywords_I.get(), ["kw1", "kw2"] )
        self.keywords_I.add("kw3")
        self.assertEqual(self.keywords_I.get(), ["kw1", "kw2", "kw3"] )

    def test_remove_keyword(self):
        self.keywords_I.set(["kw1", "kw2", "kw3"])
        self.assertEqual(self.keywords_I.get(), ["kw1", "kw2", "kw3"] )
        self.keywords_I.remove("kw2")
        self.assertEqual(self.keywords_I.get(), ["kw1", "kw3"] )
        self.keywords_I.remove("kw1")
        self.assertEqual(self.keywords_I.get(), ["kw3"] )
        self.keywords_I.remove("kw3")
        self.assertEqual(self.keywords_I.get(), [] )
        