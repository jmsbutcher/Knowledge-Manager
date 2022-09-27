# 9/26/22

import os
import shutil
import sys
import unittest
from pathlib import Path

ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
sys.path.append(ROOT)

from globals import ROOT, TEST_PATH


# Temporary disposable directory for performing folder and file creation tests
TEST_DIRECTORY_NAME = "test_dir"
TEST_DIRECTORY_PATH = TEST_PATH / Path(TEST_DIRECTORY_NAME)


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
        # Move back into the root directory and remove the test directory
        os.chdir(ROOT)
        tear_down_test_dir()

