# 9/25/22

from DocumentManagers.document_creator import DocumentCreator
from DocumentManagers.document_viewer import DocumentViewer, FilenameNotFoundError
from test_base import TestBase


class TestDocumentViewer(TestBase):

    def setUp(self):
        TestBase.setUp(self)

        # Create and initialize a document creator to help with tests
        self.doc_creator = DocumentCreator()
        self.doc_creator.create_new_document_folder_if_doesnt_exist()

        # Create a document viwer to test on
        self.doc_viewer = DocumentViewer()

    #------------------------------------------------------------------------------------


    def test_create_document_viewer(self):
        self.doc_viewer = DocumentViewer()
        self.assertTrue(True)


    def test_document_viewer_raises_exception_when_doc_name_not_found(self):
        nonexistent_filename = "nothing.txt"
        view_doc_func = self.doc_viewer.view_document_by_name
        self.assertRaises(FilenameNotFoundError, view_doc_func, nonexistent_filename)


    def test_document_viewer_returns_doc_contents_string(self):
        """ 
        Test the document viewer's primary function 'view_document_by_name' 
        and make sure it returns the found document's contents as a string.
        """
        # First, create a sample file
        sample_filename = "file"
        self.doc_creator.create_new_document_folder_if_doesnt_exist()
        self.doc_creator.create_new_text_file_if_doesnt_exist(sample_filename)

        # Add some contents to the file
        sample_text = "This is a sample document."
        with open(self.doc_creator._folder_path / (sample_filename + ".txt"), "w") as f:
            f.write(sample_text)

        # Now get the string from the viewer's view method
        text_returned = self.doc_viewer.view_document_by_name(sample_filename)

        self.assertEqual(text_returned, sample_text)

