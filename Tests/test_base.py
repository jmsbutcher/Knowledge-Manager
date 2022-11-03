# 9/26/22
#
# Base class for all test modules
#
# - Also takes care of adding the root directory to the system path, 
#   so all test modules can use the global variables shared by the main program.
#
# - Defines standard set up and tear down functions, which can be extended.
#   The functions set up a temporary directory for performing all tests,
#   including folder and file creation/modification operations.

import os
import shutil
import unittest
from pathlib import Path

print(os.getcwd())

# Temporary disposable directory for performing folder and file creation tests
TEST_DIRECTORY_NAME = "test_dir"
TEST_DIRECTORY_PATH = Path.cwd() / Path(TEST_DIRECTORY_NAME)

print("Test directory path: ", TEST_DIRECTORY_PATH)

# Temporary document repo directory within the temporary test directory
TEST_DOCUMENT_REPO_NAME = "test_doc_repo"
TEST_DOCUMENT_REPO_PATH = TEST_DIRECTORY_PATH / TEST_DOCUMENT_REPO_NAME

print("Test directory path: ", TEST_DOCUMENT_REPO_PATH)


def set_up_test_dir():
    if os.path.exists(TEST_DIRECTORY_PATH):
        shutil.rmtree(TEST_DIRECTORY_PATH)
    os.mkdir(TEST_DIRECTORY_PATH)


def tear_down_test_dir():
    shutil.rmtree(TEST_DIRECTORY_PATH)



class TestBase(unittest.TestCase):

    def setUp(self):
        # Set up a test directory "test_dir/" inside the "Tests/" directory
        set_up_test_dir()
        os.chdir(TEST_DIRECTORY_PATH)


    def tearDown(self):
        # Move back into the Test root directory and remove the test directory
        os.chdir("..")
        tear_down_test_dir()

