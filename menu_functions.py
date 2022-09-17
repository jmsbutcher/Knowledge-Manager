
import os


DOCUMENT_FOLDER_NAME = "km_Documents"


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


def handle_create_new_document():
    create_new_document_folder_if_doesnt_exist()
    print("New document created.")


def create_new_document_folder_if_doesnt_exist():
    if not os.path.exists(DOCUMENT_FOLDER_NAME):
        os.mkdir(DOCUMENT_FOLDER_NAME)