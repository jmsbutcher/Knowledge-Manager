# 11/19/22

from DocumentManagement.AttributeManagement.name_interface import NameInterface
from DocumentManagement.AttributeManagement.content_interface import ContentInterface
from DocumentManagement.AttributeManagement.category_interface import CategoryInterface
from DocumentManagement.AttributeManagement.keywords_interface import KeywordsInterface

from DocumentManagement.document_deletor import DocumentDeletor
from DocumentManagement.document_exceptions import FilenameNotFoundError

from globals import DEFAULT_DOCUMENT_REPO_PATH, doc_manager

from tkinter import Button, Entry, Frame, Label, StringVar, Text, ttk
from gui_resources import *

class DocumentDetailsFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, 
            STANDARD_FRAME_ATTRIBUTES,
            width=300)

        # Functions meant to carry out updates upon certain actions
        self.notifiers = []

        # Document attribute interfaces
        self.name_I = None
        self.category_I = None
        self.keywords_I = None 
        self.content_I = None

        # ---------------------------------------------------------------------
        # Attributes Panel - Controls for changing document attributes
        self.attributes_panel = Frame(master, STANDARD_PANEL_ATTRIBUTES)
        self.attributes_panel.pack()

        ENTRY_WIDTH = 30

        # Name
        self.doc_name_label = Label(self.attributes_panel, 
            SMALL_LABEL_ATTRIBUTES,
            text="Name")
        self.doc_name_label.grid(row=0, column=0)

        self.name_var = StringVar()
        self.doc_name_entry = Entry(self.attributes_panel, 
            textvariable=self.name_var,
            width=ENTRY_WIDTH)
        self.doc_name_entry.grid(row=0, column=1)

        # Category
        self.doc_category_label = Label(self.attributes_panel,
            SMALL_LABEL_ATTRIBUTES,
            text="Category")
        self.doc_category_label.grid(row=1, column=0)

        self.category_var = StringVar()
        self.category_entry = Entry(self.attributes_panel, 
            textvariable=self.category_var,
            width=ENTRY_WIDTH)
        self.category_entry.grid(row=1, column=1)

        # Keywords
        self.keywords_label = Label(self.attributes_panel,
            SMALL_LABEL_ATTRIBUTES,
            text="Keywords")
        self.keywords_label.grid(row=2, column=0)

        self.keywords_var = StringVar()
        self.keywords_entry = Entry(self.attributes_panel, 
            textvariable=self.keywords_var,
            width=ENTRY_WIDTH)
        self.keywords_entry.grid(row=2, column=1)


        # ---------------------------------------------------------------------
        # Preview Panel - Displays document
        self.preview_panel = Frame(master, STANDARD_PANEL_ATTRIBUTES)
        self.preview_panel.pack()

        self.contents_text = Text(self.preview_panel, 
            font=("SegoeUI", 10),
            wrap="word",
            width=60)
        self.contents_text.pack(side="left")

        self.text_y_scrollbar = ttk.Scrollbar(self.preview_panel,
            orient="vertical", command = self.contents_text.yview)
        self.contents_text["yscrollcommand"] = self.text_y_scrollbar.set
        self.text_y_scrollbar.pack(side="right", fill="y")


        # ---------------------------------------------------------------------
        # Document Actions Panel - Controls for saving and deleting document
        self.doc_actions_panel = Frame(master, STANDARD_PANEL_ATTRIBUTES)
        self.doc_actions_panel.pack()

        self.save_button = Button(self.doc_actions_panel,
            PRIMARY_BUTTON_ATTRIBUTES_MEDIUM,
            text="Save", 
            command=self.save_document)
        self.save_button.pack(side="left", padx=10, pady=5)

        self.delete_button = Button(self.doc_actions_panel,
            SECONDARY_BUTTON_ATTRIBUTES,
            text="Delete", 
            command=self.delete_document)
        self.delete_button.pack(side="right", padx=10, pady=5)


        self.clear()


    def set_notifier(self, notifier_function):
        self.notifiers.append(notifier_function)

    def notify(self):
        for notifier_function in self.notifiers:
            notifier_function()


    def clear(self):
        self.doc_name_entry.delete(0, "end")
        self.category_entry.delete(0, "end")
        self.keywords_entry.delete(0, "end")

        self.contents_text.delete("1.0", "end")

        self.delete_button["state"] = "disabled"
    

    def load_document(self, doc_name):
        self.clear()

        doc = doc_manager.get_document_by_name(doc_name)

        self.name_I = NameInterface(doc)
        self.name_I.load()
        self.doc_name_entry.insert(0, self.name_I.get())

        self.category_I = CategoryInterface(doc)
        self.category_I.load()
        self.category_entry.insert(0, self.category_I.get())

        self.keywords_I = KeywordsInterface(doc)
        self.keywords_I.load()
        self.keywords_entry.insert(0, self.keywords_I.get())

        self.content_I = ContentInterface(doc)
        self.content_I.load()
        self.contents_text.delete("1.0", "end")
        self.contents_text.insert("1.0", self.content_I.get())

        self.delete_button["state"] = "normal"


    def save_document(self):
        self.name_I.set(self.doc_name_entry.get())
        self.category_I.set(self.category_entry.get())
        self.keywords_I.set(self.keywords_entry.get())
        self.content_I.set(self.contents_text.get("1.0", "end"))
        print("Saved document")
        self.notify()


    def delete_document(self):
        doc_deletor = DocumentDeletor(DEFAULT_DOCUMENT_REPO_PATH)
        doc_name = self.name_var.get()
        try:
            doc_deletor.delete(doc_name)
            doc_manager.load_documents()
        except FilenameNotFoundError:
            print("Document '" + doc_name + "' not found.")

        self.notify()
        self.clear()
        