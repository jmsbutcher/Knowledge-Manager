
import os
from pathlib import Path

#from Utils.common_functions import print_banner_line

from DocumentManagers.document_creator import DocumentCreator, FilenameAlreadyExistsError
from DocumentManagers.document_exceptions import FilenameNotFoundError
from DocumentManagers.document_viewer import DocumentViewer

HOME = Path(os.getcwd())
DOCUMENT_FOLDER_NAME = "km_Documents"
DOCUMENT_FOLDER_PATH = HOME / Path(DOCUMENT_FOLDER_NAME)
TEST_FOLDER_NAME = "Tests"
TEST_FOLDER_PATH = HOME / Path(TEST_FOLDER_NAME)


def display_greeting():
    print("""
_-^-__-^-__-^-__-^-__-^-__-^-__-^-__-^-__-^-__-^-_
|                                               |
|  Welcome to your personal knowledge manager!  |   
|                                               |
|                Version 1.0.0                  |
|                   9/17/22                     |
|                                               |
_-^-__-^-__-^-__-^-__-^-__-^-__-^-__-^-__-^-__-^-_
""")


def display_menu():
    print("""
-----------------------------------------------------
Select a choice:
C   -   Create new document
V   -   View document
Q   -   Quit
: """, end="")


def get_input(text):
    return input(text)


def start_menu_loop():
    choice = ""
    while choice.lower() != "q":
        display_menu()
        choice = get_input("")
        handle_choice(choice)


def handle_choice(choice):
    print("Handling choice ", choice)
    choice = choice.lower()
    if choice == "c":
        handle_create_new_document()
    elif choice == "v":
        handle_view_document()
    # Other choices...


def handle_create_new_document():

    new_doc_name = get_input("Enter new document name: ")
    
    doc_creator = DocumentCreator()
    doc_creator.create_new_document_repo_if_doesnt_exist()

    try:
        doc_creator.create_new_text_file_if_doesnt_exist(new_doc_name)
    except FilenameAlreadyExistsError:
        print("\n|*|*| ERROR - File with name '{}' already exists.\n".format( \
            new_doc_name))
    else:
        print("New document created.")


def handle_view_document():
    document_name = get_input("Enter document name:")
    doc_viewer = DocumentViewer()
    try:
        doc_contents = doc_viewer.view_document_by_name(document_name)
        print()
        #print_banner_line(document_name, 50)
        print(doc_contents)
        #print_banner_line(" END ", 50)
    except FilenameNotFoundError:
        print("\n|*|*| ERROR - Document '{}' not found.\n".format(document_name))

