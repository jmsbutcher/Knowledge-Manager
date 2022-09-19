# 9/17/22 

import io
import sys
import unittest
from unittest.mock import patch

ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
sys.path.append(ROOT)

from menu_functions import *
from globals import TEST_PATH


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


#------------------------------------------------------------------------------


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

        

#------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

