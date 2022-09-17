
import io
import sys
import unittest
from unittest.mock import patch

sys.path.append("../../KnowledgeManager")

from menu_functions import *

#------------------------------------------------------------------------------


def capture_output(func):
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


#------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

