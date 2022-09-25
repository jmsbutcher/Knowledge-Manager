# 9/17/22 

import os
import sys
import unittest
from unittest.mock import patch

from common_test_functions import \
    TEST_DIRECTORY_PATH, \
    set_up_test_dir, \
    tear_down_test_dir, \
    capture_output

from menu_functions import \
    display_greeting, \
    display_menu, \
    handle_create_new_document


ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
sys.path.append(ROOT)

from globals import ROOT


class TestMenu(unittest.TestCase):

    #------------------------------------------------------------------------------------
    
    def setUp(self):
        # Set up a test directory "test_dir/" inside the "Tests/" directory
        set_up_test_dir()
        os.chdir(TEST_DIRECTORY_PATH)


    def tearDown(self):
        # Move back into the root directory and remove the test directory
        os.chdir(ROOT)
        tear_down_test_dir()


    def assertErrorOutput(self, output):
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
        #self.assertIn("error", output2.lower())
        self.assertErrorOutput(output2)

        

#------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

