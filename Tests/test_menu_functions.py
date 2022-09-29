# 9/17/22 

from unittest.mock import patch

from common_test_functions import capture_output
from menu_functions import \
    display_greeting, \
    display_menu, \
    handle_create_new_document, \
    handle_view_document
from test_base import TestBase
from DocumentManagers.document_creator import DocumentCreator


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


    @patch('menu_functions.get_input', return_value="doc") # Supplies console input
    def test_handle_create_new_document_confirm_msg(self, input):
        """ Test that confirmation message is displayed to the console """
        output = capture_output(handle_create_new_document)
        self.assertEqual(output, "New document created.\n")


    @patch('menu_functions.get_input', return_value="doc") # Supplies console input
    def test_get_error_msg_when_new_doc_name_already_exists(self, input):
        """ 
        Test that an error message is displayed when trying to
        create a document with a name that already exists.
        """
        output1 = capture_output(handle_create_new_document)
        self.assertEqual(output1, "New document created.\n")

        output2 = capture_output(handle_create_new_document)
        self._assertErrorOutput(output2)


    @patch('menu_functions.get_input', return_value="doc")
    def test_handle_view_document_error_when_document_doesnt_exist(self, input):
        output = capture_output(handle_view_document)
        self._assertErrorOutput(output)


    def test_handle_view_document_prints_doc_to_console(self):
        doc_creator = DocumentCreator()
        doc_creator.create_new_document_folder_if_doesnt_exist()
        doc_creator.create_new_text_file_if_doesnt_exist("")
        doc_creator
    
