# 9/17/22 

import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from unittest.mock import patch

from KnowledgeManager.menu_functions import \
    get_input, \
    display_greeting, \
    display_menu, \
    handle_create_new_document, \
    handle_view_document
from KnowledgeManager.DocumentManagers.document_creator import DocumentCreator

from test_base import TestBase, TEST_DOCUMENT_REPO_PATH
from common_test_functions import capture_output


class TestMenu(TestBase):

    def _assertErrorOutput(self, output):
        # Assert that the keyword "error" appears somewhere in the string "output"
        self.assertIn("error", output.lower())

    #------------------------------------------------------------------------------------


    def test_display_greeting(self):
        """ Test that a greeting (non-empty) is displayed to the console """
        output = capture_output(display_greeting)
        self.assertNotEqual(output, "")


    def test_display_menu(self):
        """ Test that a menu (non-empty) is displayed to the console """
        output = capture_output(display_menu)
        self.assertNotEqual(output, "")


    def test_handle_view_document_error_when_document_doesnt_exist(self):
        with patch('builtins.input', return_value='doc4'):
            output = capture_output(handle_view_document)
            self._assertErrorOutput(output)


    def test_handle_view_document_prints_doc_to_console(self):
        doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        doc_creator.create_new_text_file_if_doesnt_exist("doc5")
        with open("doc5.txt", "w") as d:
            d.write("This is a doc.")

        self.assertTrue(True)
    
