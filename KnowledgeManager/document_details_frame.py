# 11/19/22

from DocumentManagement.document_deletor import DocumentDeletor
from DocumentManagement.document_editor import DocumentEditor
from DocumentManagement.document_manager import DocumentManager
from DocumentManagement.document_exceptions import FilenameNotFoundError
from globals import DEFAULT_DOCUMENT_REPO_PATH

from tkinter import Button, Entry, Frame, Label, StringVar, Text, ttk
from gui_functions import format_attribute
from gui_resources import *

class DocumentDetailsFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, 
            STANDARD_FRAME_ATTRIBUTES,
            width=300)

        # Reference to the document list frame, so it can be updated
        self.doc_list_frame_ref = None

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


    def set_notifier(self, doc_list_frame_ref):
        self.doc_list_frame_ref = doc_list_frame_ref


    def clear(self):
        # self.name_var = ""
        # self.category_var = ""
        # self.keywords_var = ""

        self.doc_name_entry.delete(0, "end")
        self.category_entry.delete(0, "end")
        self.keywords_entry.delete(0, "end")

        self.contents_text.delete("1.0", "end")

        self.delete_button["state"] = "disabled"
    

    def load_document(self, doc_name):
        self.clear()
        doc_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
        document = doc_manager.get_document_by_name(doc_name)
        self.doc_name_entry.insert(0, format_attribute(document.name))
        self.category_entry.insert(0, format_attribute(document.category))
        self.keywords_entry.insert(0, format_attribute(document.keywords))
        self.contents_text.delete("1.0", "end")
        self.contents_text.insert("1.0", document.contents)

        self.delete_button["state"] = "normal"


    def save_document(self):

        print("Saved document")


    def delete_document(self):
        doc_deletor = DocumentDeletor(DEFAULT_DOCUMENT_REPO_PATH)
        doc_name = self.name_var.get()
        try:
            doc_deletor.delete(doc_name)
        except FilenameNotFoundError:
            print("Document '" + doc_name + "' not found.")

        if self.doc_list_frame_ref is not None:
            self.doc_list_frame_ref.load_documents()

        self.clear()