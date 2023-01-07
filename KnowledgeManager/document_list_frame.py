# 11/6/22

from tkinter import BOTH, CENTER, Frame, ttk, VERTICAL, Y

from DocumentManagement.AttributeManagement.name_interface import NameInterface
from DocumentManagement.AttributeManagement.category_interface import CategoryInterface
from DocumentManagement.AttributeManagement.keywords_interface import KeywordsInterface

from DocumentManagement.document_editor import DocumentEditor

from globals import DEFAULT_DOCUMENT_REPO_PATH, doc_manager


class DocumentListFrame(Frame):
    """ 
    Displays document data in tabular form 

    - Each document is listed as a row in the table, with attributes arranged
    in columns (e.g., Name, Author, Date, Category, keyword, etc.)

    - Single-clicking on a row loads the document's attributes and content
    into the preview panel.

    - Double-clicking on a row opens the document in a text editor.
    """

    def __init__(self, master, doc_details_frame_ref):
        Frame.__init__(self, master)
        self.master = master 
        self.doc_details_frame_ref = doc_details_frame_ref

        self.treeview = ttk.Treeview(self.master)

        self.attributes = (
            CategoryInterface, 
            KeywordsInterface
        )

        self.treeview["columns"] = [a.name for a in self.attributes]

         # Treeview's first column is identified by special name "#0" 
        self._init_column("#0", NameInterface.name)
        # The rest are standard and only need their own names
        for attribute in self.attributes:
            self._init_column(attribute.name, attribute.name)

        scrollbar = ttk.Scrollbar(self.master, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill=Y)

        self.treeview.pack(padx=5, pady=5, fill=BOTH, expand=1)
        self.treeview.bind("<<TreeviewSelect>>", self._load_document_details)
        self.treeview.bind("<Double-1>", self._open_document_in_editor)

        self.load_documents()


    def load_documents(self):
        self._clear_list()
        for doc in doc_manager.get_documents():
            vals = [str(att(doc)) for att in self.attributes]
            self.treeview.insert("", "end", text=doc.name, values=vals, tags=CENTER)


    def _init_column(self, col_identifier, attribute_name):
        self.treeview.column(col_identifier, anchor=CENTER)
        self.treeview.heading(col_identifier, text=attribute_name)
        
    def _clear_list(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def _load_document_details(self, event):
        for selected_document in self.treeview.selection():
            document = self.treeview.item(selected_document)
            doc_name = document["text"]
            self.doc_details_frame_ref.load_document(doc_name)

    def _open_document_in_editor(self, event):
        for selected_document in self.treeview.selection():
            document = self.treeview.item(selected_document)
            print(document)
            print(document["text"])
            doc_editor = DocumentEditor(DEFAULT_DOCUMENT_REPO_PATH)
            doc_editor.open_document_in_text_editor(document["text"])

