# 11/25/22

import os

from KnowledgeManager.DocumentManagement.document_creator \
    import DocumentCreator
from KnowledgeManager.DocumentManagement.document import Document
from KnowledgeManager.DocumentManagement.AttributeManagement.content_interface \
    import ContentInterface

from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestContentInterface(TestBase):

    def setUp(self):
        TestBase.setUp(self)

        self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        self.doc_creator.create_new_text_file_if_doesnt_exist("test")

        self.doc_name = "test"
        self.doc_path = TEST_DOCUMENT_REPO_PATH / (self.doc_name + ".txt")
        self.assertTrue(os.path.exists(self.doc_path))

        self.doc = Document(self.doc_path)
        self.content_I = ContentInterface(self.doc)
        self.content_I.load()
        self.test_content = "Some test\ncontent\nlines."

    #--------------------------------------------------------------------------

    def test_can_create(self):
        self.assertTrue(True)

    def test_set_content_when_empty_file(self):
        # Try default content
        self.content_I.set(self.test_content)
        self.assertEqual(self.content_I.get(), self.test_content)
        # Now try different content
        self.content_I.set("kw3")
        self.assertEqual(self.content_I.get(), "kw3")

    def test_set_content_with_attributes_doesnt_overwrite_attributes(self):
        with open(self.doc_path, "w") as doc:
            doc.write("#Category: New\n#Keywords: kw1, kw2\n\nRegular contents\nLine2")
        self.content_I.set("New content\nNext Line")

        with open(self.doc_path, "r") as doc:
            self.assertEqual(doc.read(), 
            "#Category: New\n#Keywords: kw1, kw2\n\nNew content\nNext Line")

    def test_get_method_returns_empty_list_when_no_content(self):
        self.assertEqual(self.content_I.get(), "")

    def test_str_method(self):
        self.content_I.set(self.test_content)
        self.assertEqual(str(self.content_I), self.test_content)

    def test_is_attribute_line(self):
        self.assertTrue(self.content_I._is_attribute_line("#Category:"))
        self.assertTrue(self.content_I._is_attribute_line("#Keywords: "))
        self.assertTrue(self.content_I._is_attribute_line("#Category: New"))
        self.assertFalse(self.content_I._is_attribute_line("Category: New"))
        self.assertFalse(self.content_I._is_attribute_line("A regular line"))
        self.assertFalse(self.content_I._is_attribute_line("\n"))
        self.assertFalse(self.content_I._is_attribute_line(""))

    def test_load_content(self):
        with open(self.doc_path, "w") as doc:
            doc.write("#Category: New\n#Keywords: kw1, kw2\nRegular contents\nLine2")
        contents = self.content_I._load_content()
        self.assertEqual(contents, "Regular contents\nLine2")

    def test_load_entire_file_lines(self):
        with open(self.doc_path, "w") as doc:
            doc.write("#Category: New\n#Keywords: kw1, kw2\nRegular contents\nLine2")
        loaded_lines = self.content_I._load_entire_file_lines()
        expected_lines = ["#Category: New\n",
            "#Keywords: kw1, kw2\n",
            "Regular contents\n",
            "Line2"]
        self.assertEqual(loaded_lines, expected_lines)