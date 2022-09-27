
import io
import os
import shutil
import sys
from pathlib import Path


# ROOT = "C:/Users/James/Documents/Programming/KnowledgeManager"
# sys.path.append(ROOT)

# from globals import ROOT, TEST_PATH


# #------------------------------------------------------------------------------
# # Test directory

# # A temporary, disposable directory for performing folder and file creation tests
# TEST_DIRECTORY_NAME = "test_dir"
# TEST_DIRECTORY_PATH = TEST_PATH / Path(TEST_DIRECTORY_NAME)

# # Put these two functions into the setUp() and tearDown() unittest methods
# def set_up_test_dir():
#     if os.path.exists(TEST_DIRECTORY_PATH):
#         shutil.rmtree(TEST_DIRECTORY_PATH)
#     os.mkdir(TEST_DIRECTORY_PATH)

# def tear_down_test_dir():
#     shutil.rmtree(TEST_DIRECTORY_PATH)


#------------------------------------------------------------------------------
# Capture console output so it can be tested

def capture_output(func, *args):
    """ 
    A decorator that redirects standard output so it can be converted to a string
    
    Input: a function that prints something to the console
    Returns: a string consisting of the console output
    """
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    func(*args)

    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()
