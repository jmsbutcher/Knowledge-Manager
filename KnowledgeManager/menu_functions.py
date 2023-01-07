
import os
from pathlib import Path
from DocumentManagement.document_editor import DocumentEditor

from DocumentManagement.document_manager import DocumentManager
from DocumentManagement.document_creator import DocumentCreator, FilenameAlreadyExistsError
from DocumentManagement.document_exceptions import FilenameNotFoundError
from DocumentManagement.document_viewer import DocumentViewer

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
N   -   Create new document
E   -   Edit document
L   -   List documents
V   -   View document
C   -   Filter by category
K   -   Filter by keyword
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
    choice = choice.lower()
    if choice == "n":
        handle_create_new_document()
    elif choice == "e":
        handle_edit_document()
    elif choice == "l":
        handle_list_documents()
    elif choice == "v":
        handle_view_document()
    elif choice == "c":
        handle_filter_by_category()
    elif choice == "k":
        handle_filter_by_keyword()
    elif choice == "q":
        exit
    else:
        print("\n  Invalid choice. Try again.")
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
    doc_name = search_for_document()
    if doc_name is None:
        return

    doc_editor = DocumentEditor(DOCUMENT_FOLDER_PATH)

    try:
        doc_editor.open_document_in_text_editor(doc_name)

    except FilenameNotFoundError:
        print("\n|*|*| ERROR - Document '{}' not found.\n".format(doc_name))


def handle_list_documents():
    doc_manager = DocumentManager(DOCUMENT_FOLDER_PATH)
    doc_names = doc_manager.get_list_of_names()
    print("\nDocuments:\n")
    for doc_number, doc_name in enumerate(doc_names):
        print ("{:2d} - {}".format(doc_number, doc_name))


def handle_view_document():
    # Locate the document by name
    doc_name = search_for_document()
    if doc_name is None:
        return

    doc_viewer = DocumentViewer(DOCUMENT_FOLDER_PATH)

    try:
        doc_viewer.print_document_to_console(doc_name)

    except FilenameNotFoundError:
        print("\n|*|*| ERROR - Document '{}' not found.\n".format(doc_name))


def handle_filter_by_category():
    doc_manager = DocumentManager(DOCUMENT_FOLDER_PATH)
    print("\nAvailable categories: ", ', '.join(doc_manager.get_all_categories()))
    category = get_input("Enter category: ")

    matches = doc_manager.filter_documents_by_category(category)

    print("\nResults:\n")
    for doc_number, doc in enumerate(matches):
        print ("{:2d} - {}".format(doc_number, doc.name))
    print()


def handle_filter_by_keyword():
    doc_manager = DocumentManager(DOCUMENT_FOLDER_PATH)
    print("\nAvailable keywords: ", ', '.join(doc_manager.get_all_keywords()))
    keywords_string = get_input("Enter keywords: ")
    keywords = [keyword.strip() for keyword in keywords_string.split(",")]

    matches = doc_manager.filter_by_keyword(keywords)

    print("\nResults:\n")
    for doc_number, doc in enumerate(matches):
        print ("{:2d} - {}".format(doc_number, doc.name))
    print()


def search_for_document():
    doc_manager = DocumentManager(DOCUMENT_FOLDER_PATH)

    matches = []
    doc_name = ""

    # Keep narrowing down search until exact name match is found 
    while True:

        if doc_name in doc_manager.get_list_of_names():
            return doc_name

        doc_name = get_input("\nSearch for document by name or 'q' to cancel: ")
        if doc_name == "q":
            return None
        elif doc_name in doc_manager.get_list_of_names():
            return doc_name
        else:
            # Get all potential matches that include substring
            matches = doc_manager.search_for_document(doc_name)
            if len(matches) == 0:
                print("\n  No results. Try again.")
            else:
                print("\n  Results:")
                doc_name = prompt_for_choice_by_number(matches)




def prompt_for_choice_by_number(options):
    """
    Display list of options and allow user to choose one by number.
    Return the option chosen, or None if invalid choice or cancel.
      Example: options={"Option A", "Option B", "Option C"}
      Displays to console:
    >>>    1 - Option A
    >>>    2 - Option B
    >>>    3 - Option C
    >>>  Select a number or 'q' to cancel: 2 <-- [User enters '2']

      Returns "Option B"

    """
    for option_number, option in enumerate(options):
        print("  {:2d} - {}".format(option_number + 1, option))

    choice = get_input("\n  Select a number or 'q' to cancel: ")
    if choice == "q":
        return None
    else:
        if choice.isnumeric():
            choice = int(choice) - 1
            if (choice >= 0 and choice < len(options)):
                return options[int(choice)]
        print("\n  Invalid choice.")
        return None
