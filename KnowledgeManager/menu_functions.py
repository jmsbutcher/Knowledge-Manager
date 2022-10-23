
import os
from pathlib import Path
from DocumentManagers.document_editor import DocumentEditor

from DocumentManagers.document_manager import DocumentManager
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
E   -   Edit document
L   -   List documents
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
    elif choice == "e":
        handle_edit_document()
    elif choice == "l":
        handle_list_documents()
    elif choice == "v":
        handle_view_document()
    # Other choices...


def handle_create_new_document():
    new_doc_name = get_input("Enter new document name: ")
    doc_creator = DocumentCreator(DOCUMENT_FOLDER_PATH)

    try:
        doc_creator.create_new_text_file_if_doesnt_exist(new_doc_name)
    except FilenameAlreadyExistsError:
        print("\n|*|*| ERROR - File with name '{}' already exists.\n".format( \
            new_doc_name))
    else:
        print("New document created.")


def handle_edit_document():
    doc_name = get_input("Enter document to edit:")
    doc_editor = DocumentEditor(DOCUMENT_FOLDER_PATH)
    try:
        doc_editor.open_document_in_text_editor(doc_name)

    except FilenameNotFoundError:
        print("\n|*|*| ERROR - Document '{}' not found.\n".format(doc_name))


def handle_list_documents():
    doc_manager = DocumentManager(DOCUMENT_FOLDER_PATH)
    doc_names = doc_manager.get_list_of_document_names()
    print("\nDocuments:\n")
    for doc_number, doc_name in enumerate(doc_names):
        print ("{:2d} - {}".format(doc_number, doc_name))


def handle_view_document():
    doc_name = get_input("Enter document name:")
    doc_viewer = DocumentViewer(DOCUMENT_FOLDER_PATH)
    try:
        doc_viewer.print_document_to_console(doc_name)

    except FilenameNotFoundError:
        print("\n|*|*| ERROR - Document '{}' not found.\n".format(doc_name))


