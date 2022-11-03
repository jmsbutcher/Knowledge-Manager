# 9/25/22

import sys
sys.path.append("C:/Users/James/Documents/Programming/KnowledgeManager")

from KnowledgeManager.DocumentManagement.document_creator import DocumentCreator
from KnowledgeManager.DocumentManagement.document_viewer import DocumentViewer, FilenameNotFoundError
from KnowledgeManager.Utils.common_functions import print_banner_line
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH
from common_test_functions import capture_output


class TestDocumentViewer(TestBase):

    def setUp(self):
        TestBase.setUp(self)

        # Create and initialize a document creator to help with tests
        self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)

        # Create a document viwer to test on
        self.doc_viewer = DocumentViewer(TEST_DOCUMENT_REPO_PATH)

    #------------------------------------------------------------------------------------


    def test_create_document_viewer(self):
        self.doc_viewer = DocumentViewer(TEST_DOCUMENT_REPO_PATH)
        self.assertTrue(True)


    def test_document_viewer_raises_exception_when_doc_name_not_found(self):
        nonexistent_filename = "nothing.txt"
        view_doc_func = self.doc_viewer.get_document_contents
        self.assertRaises(FilenameNotFoundError, view_doc_func, nonexistent_filename)


    def test_document_viewer_returns_doc_contents_string(self):
        """ 
        Test the document viewer's primary function 'view_document_by_name' 
        and make sure it returns the found document's contents as a string.
        """
        # First, create a sample file
        sample_filename = "file"
        self.doc_creator.create_new_text_file_if_doesnt_exist(sample_filename)

        # Add some contents to the file
        sample_text = "This is a sample document."
        with open(self.doc_creator._document_repo_path / (sample_filename + ".txt"), "w") as f:
            f.write(sample_text)

        # Now get the string from the viewer's view method
        text_returned = self.doc_viewer.get_document_contents(sample_filename)

        self.assertEqual(text_returned, sample_text)


    def test_document_viewer_prints_bannered_document_to_console(self):
        """ 
        Test the document viewer's secondary use: print document's contents to
        the console with top and bottom banners.
        """
        # First, create a sample file
        sample_filename = "file"
        self.doc_creator.create_new_text_file_if_doesnt_exist(sample_filename)

        # Add some contents to the file
        sample_text = "This is a sample document."
        with open(self.doc_creator._document_repo_path / (sample_filename + ".txt"), "w") as f:
            f.write(sample_text)

        expected_output = "\n-----------------------file-----------------------\n" + \
            sample_text + "\n---------------------- END -----------------------\n"

        output = capture_output(self.doc_viewer.print_document_to_console, sample_filename)

        self.assertEqual(output, expected_output)

