
import os
from pathlib import Path

from DocumentManagers.document_creator import DocumentCreator, FilenameAlreadyExistsError

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
    # Other choices ...


def handle_create_new_document():

    new_doc_name = get_input("Enter new document name: ")
    
    doc_creator = DocumentCreator()
    doc_creator.create_new_document_folder_if_doesnt_exist()

    try:
        doc_creator.create_new_text_file_if_doesnt_exist(new_doc_name)
    except FilenameAlreadyExistsError:
        print("\n|*|*| ERROR - File with name '{}' already exists.\n".format( \
            new_doc_name))
    else:
        print("New document created.")

