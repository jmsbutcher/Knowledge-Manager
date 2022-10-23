# 9/18/22

import os

from KnowledgeManager.DocumentManagers.document_creator import DocumentCreator, FilenameAlreadyExistsError
from test_base import TestBase, TEST_DOCUMENT_REPO_PATH


class TestDocumentCreator(TestBase):
    
    def setUp(self):
        TestBase.setUp(self)
        self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
    
    def _doc_folder_exists(self):
        return os.path.exists(self.doc_creator._document_repo_path)

    #------------------------------------------------------------------------------------


    def test_create_document_creator(self):
        #self.doc_creator = DocumentCreator(TEST_DOCUMENT_REPO_PATH)
        self.assertTrue(True)


    def test_create_new_document_folder_if_doesnt_exist(self):
        """ Test that create_new_document_fold... creates a new doc folder """

        # Test that the document folder has been created
        self.assertTrue(self._doc_folder_exists())



    def test_check_if_filename_exists_returns_false_when_doesnt_exist(self):
        """ 
        Test check_if_filename_exists function returns false if a filename
        doesn't exist in the target directory.
        """
        non_existent_filename = "nothing"
        exists = self.doc_creator._filename_exists(non_existent_filename)
        self.assertFalse(exists)
        


    def test_check_if_filename_exists_returns_true_when_does_exist(self):
        """ 
        Test check_if_filename_exists function returns true if a filename
        exists in the target directory.
        """
        filename = "file.txt"
        with open(TEST_DOCUMENT_REPO_PATH / filename, "w"):
            exists = self.doc_creator._filename_exists(filename)
            self.assertTrue(exists)



    def test_create_new_text_file_if_doesnt_exist_with_provided_name(self):
        """ Test that a new text document gets created with the correct name"""

        # Create the file
        TEST_FILE_NAME = "test_document.txt"
        self.doc_creator.create_new_text_file_if_doesnt_exist(TEST_FILE_NAME)

        # Check if the file now exists in the correct location
        TEST_FILE_PATH = TEST_DOCUMENT_REPO_PATH / TEST_FILE_NAME
        self.assertTrue(os.path.exists(TEST_FILE_PATH))


    def test_create_new_text_file_always_ends_with_dot_txt(self):
        """ 
        Test that create_new_text_file... function always puts ".txt" at 
        the end, even if it's not provided.
        """

        # With ".txt" provided explicitly
        TEST_FILE_NAME_1 = "test_document1.txt"
        self.doc_creator.create_new_text_file_if_doesnt_exist(TEST_FILE_NAME_1)
        EXPECTED_FILE_NAME_1 = "test_document1.txt"
        EXPECTED_FILE_PATH_1 = TEST_DOCUMENT_REPO_PATH / EXPECTED_FILE_NAME_1
        self.assertTrue(os.path.exists(EXPECTED_FILE_PATH_1))

        # Without ".txt"
        TEST_FILE_NAME_2 = "test_document2"
        self.doc_creator.create_new_text_file_if_doesnt_exist(TEST_FILE_NAME_2)
        EXPECTED_FILE_NAME_2 = "test_document2.txt"
        EXPECTED_FILE_PATH_2 = TEST_DOCUMENT_REPO_PATH / EXPECTED_FILE_NAME_2
        self.assertTrue(os.path.exists(EXPECTED_FILE_PATH_2))

        # Make sure file without ".txt" extension DOESN'T exist
        TEST_FILE_NAME_3 = "test_document3"
        self.doc_creator.create_new_text_file_if_doesnt_exist(TEST_FILE_NAME_3)
        EXPECTED_FILE_NAME_3 = "test_document3"
        EXPECTED_FILE_PATH_3 = TEST_DOCUMENT_REPO_PATH / EXPECTED_FILE_NAME_3
        self.assertFalse(os.path.exists(EXPECTED_FILE_PATH_3))


    def test_create_new_text_file_if_doesnt_exist_gives_error_message_if_exists(self):
        """
        Test that creating a file that has the same name as an already
        existing file results in an error message and no new file being
        created.
        """

        # Create the file and test that it exists
        TEST_FILE_NAME = "test_document.txt"
        TEST_FILE_PATH = TEST_DOCUMENT_REPO_PATH / TEST_FILE_NAME
        self.doc_creator.create_new_text_file_if_doesnt_exist(TEST_FILE_NAME)
        self.assertTrue(os.path.exists(TEST_FILE_PATH))

        # Try creating a file with the same name, and make sure 
        # an error message gets displayed.
        create_file_again_func = self.doc_creator.create_new_text_file_if_doesnt_exist
        self.assertRaises(FilenameAlreadyExistsError, create_file_again_func, TEST_FILE_NAME)
