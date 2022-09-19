# 9/18/22

import glob
import os
import shutil
import sys
import unittest
from pathlib import Path

ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
sys.path.append(ROOT)

from globals import TEST_PATH
from document_creator import DocumentCreator


#------------------------------------------------------------------------------
# Utility functions

TEST_DIRECTORY_NAME = "test_dir"
TEST_DIRECTORY_PATH = TEST_PATH / Path(TEST_DIRECTORY_NAME)

def set_up_test_dir():
    if os.path.exists(TEST_DIRECTORY_PATH):
        shutil.rmtree(TEST_DIRECTORY_PATH)
    os.mkdir(TEST_DIRECTORY_PATH)


def tear_down_test_dir():
    shutil.rmtree(TEST_DIRECTORY_PATH)

#------------------------------------------------------------------------------


class TestDocumentCreator(unittest.TestCase):

    def test_create_document_creator(self):
        doc_creator = DocumentCreator
        self.assertTrue(True)


    def test_create_new_document_folder_if_doesnt_exist(self):
        """ Test that create_new_document_fold... creates a new doc folder """
        pass

        # set_up_test_dir()
        # os.chdir(TEST_DIRECTORY_PATH)

        # # Test that the folder doesn't exist first ( ../Tests/test_dir/km_documents )
        # self.assertFalse(os.path.exists(DOCUMENT_FOLDER_NAME))

        # # Now call the function to create the folder
        # create_new_document_folder_if_doesnt_exist()

        # # Test that the document folder has been created
        # self.assertTrue(os.path.exists(DOCUMENT_FOLDER_NAME))

        # # Make sure a system error doesn't happen here as a result of
        # # trying to create a folder that already exists
        # output = capture_output(create_new_document_folder_if_doesnt_exist)
        # self.assertEqual(output, "")

        # os.chdir(HOME)
        # tear_down_test_dir()


    def test_check_if_filename_exists_returns_false_when_doesnt_exist(self):
        """ 
        Test check_if_filename_exists function returns true if a filename
        exists in the target directory and false otherwise.
        """
        pass
        # set_up_test_dir()

        # non_existent_filename = "nothing"
        # self.assertFalse(check_if_filename_exists(TEST_DIRECTORY_PATH / non_existent_filename))

        # tear_down_test_dir()


    def test_check_if_filename_exists_returns_true_when_does_exist(self):
        """ 
        Test check_if_filename_exists function returns true if a filename
        exists in the target directory and false otherwise.
        """
        pass
        # set_up_test_dir()

        # filename = "file.txt"
        # with open(TEST_DIRECTORY_PATH / filename, "w") as f:
        #     self.assertTrue(check_if_filename_exists(TEST_DIRECTORY_PATH / filename))

        # tear_down_test_dir()


    def test_create_new_text_file_if_doesnt_exist_with_provided_name(self):
        """ Test that a new text document gets created with the correct name"""
        pass
        # set_up_test_dir()
        # os.chdir(TEST_DIRECTORY_PATH) # HOME / Tests / test_dir

        # # Create a mock documents folder first, as used in handle_create_new_document
        # create_new_document_folder_if_doesnt_exist() # HOME / Tests / test_dir / km_documents

        # # Create the file and test that it exists
        # TEST_FILE_NAME = "test_document"
        # TEST_FILE_PATH = TEST_DIRECTORY_PATH / DOCUMENT_FOLDER_NAME
        # create_new_text_file_if_doesnt_exist(TEST_FILE_PATH, TEST_FILE_NAME) # HOME / Tests / test_dir / km_documents / test_document
        # self.assertTrue(os.path.exists(TEST_FILE_PATH, TEST_FILE_NAME))

        # os.chdir(HOME)
        # tear_down_test_dir()


    def test_create_new_text_file_if_doesnt_exist_gives_error_message_if_exists(self):
        """
        Test that creating a file that has the same name as an already
        existing file results in an error message and no new file being
        created.
        """
        pass
        # set_up_test_dir()
        # os.chdir(TEST_DIRECTORY_PATH)

        # # Create a mock documents folder first, as used in handle_create_new_document
        # create_new_document_folder_if_doesnt_exist()

        # # Create the file and test that it exists
        # TEST_FILE_NAME = "test_document"
        # TEST_FILE_PATH = TEST_DIRECTORY_PATH / DOCUMENT_FOLDER_NAME
        # create_new_text_file_if_doesnt_exist(TEST_FILE_PATH, TEST_FILE_NAME)
        # self.assertTrue(os.path.exists(TEST_FILE_PATH / TEST_FILE_NAME))

        # # Try creating a file with the same name, and make sure an error message
        # # gets displayed.
        # output = capture_output(create_new_text_file_if_doesnt_exist(TEST_FILE_PATH, TEST_FILE_NAME))
        # self.assertIn(output.lower(), "error")

        # os.chdir(HOME)
        # tear_down_test_dir()


#------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
