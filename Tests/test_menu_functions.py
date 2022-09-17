
import io
import sys
import unittest
from unittest.mock import patch

sys.path.append("../../KnowledgeManager")

from menu_functions import *

#------------------------------------------------------------------------------


def capture_output(func):
    """ 
    Redirects standard output so it can be converted to a string
    
    Input: a function that prints something to the console
    Returns: a string consisting of the console output
    """
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    func()

    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()



class TestMenu(unittest.TestCase):

    def test_display_greeting(self):
        """ Test that a greeting (non-empty) is displayed to the console """
        output = capture_output(display_greeting)
        self.assertNotEqual(output, "")


    def test_display_menu(self):
        """ Test that a menu (non-empty) is displayed to the console """
        output = capture_output(display_menu)
        self.assertNotEqual(output, "")


    def test_handle_create_new_document_confirm_msg(self):
        """ Test that confirmation message is displayed to the console """
        output = capture_output(handle_create_new_document)
        self.assertEqual(output, "New document created.\n")


    def test_create_new_document_folder_if_doesnt_exist(self):
        """ Test that create_new_document_fold... creates a new doc folder """

        os.mkdir("test_new_doc_folder")
        os.chdir("test_new_doc_folder")
        self.assertFalse(os.path.exists(DOCUMENT_FOLDER_NAME))
        

#------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

