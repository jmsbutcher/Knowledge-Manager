# 11/6/22

from tkinter import BOTH, CENTER, Frame, Label, Tk, ttk, VERTICAL, Y

from DocumentManagement.AttributeManagement.name_interface import NameInterface
from DocumentManagement.AttributeManagement.content_interface import ContentInterface
from DocumentManagement.AttributeManagement.category_interface import CategoryInterface
from DocumentManagement.AttributeManagement.keywords_interface import KeywordsInterface

from DocumentManagement.document_editor import DocumentEditor
from DocumentManagement.document_manager import DocumentManager

from globals import DEFAULT_DOCUMENT_REPO_PATH

from document_details_frame import DocumentDetailsFrame


class DocumentListFrame(Frame):
    """ 
    Displays document data in tabular form 

    Each document is listed as a row in the table, with attributes arranged
    in columns (e.g., Name, Author, Date, Category, keyword, etc.)
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
        print([a.name for a in self.attributes])
        self.treeview["columns"] = [a.name for a in self.attributes]
         # Treeview's first column is identified by special name "#0" 
        self._init_column("#0", NameInterface.name)
        # The rest are standard and only need their own names
        for attribute in self.attributes:
            self._init_column(attribute.name, attribute.name)

        # self.treeview["columns"] = (\
        #     "Category", 
        #     "Keywords",
        #     )

        # self.treeview.column("#0")
        # self.treeview.column("Category", anchor=CENTER)
        # self.treeview.column("Keywords", anchor=CENTER)

        # self.treeview.heading("#0", text="Name")
        # self.treeview.heading("Category", text="Category")
        # self.treeview.heading("Keywords", text="Keywords")\

        scrollbar = ttk.Scrollbar(self.master, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill=Y)

        self.treeview.pack(padx=5, pady=5, fill=BOTH, expand=1)
        self.treeview.bind("<<TreeviewSelect>>", self._load_document_details)
        self.treeview.bind("<Double-1>", self._open_document_in_editor)

        self.load_documents()


    def _init_column(self, col_identifier, attribute_name):
        #self.treeview["columns"] = list(self.treeview["columns"]).append(col_identifier)
        self.treeview.column(col_identifier, anchor=CENTER)
        self.treeview.heading(col_identifier, text=attribute_name)


    def load_documents(self, documents=None):
        self._clear_list()
        document_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
        docs_to_load = documents
        # If no list of document specified, load all the document in the repo
        if documents is None:
            docs_to_load = document_manager.get_documents()

        if docs_to_load is not None:
            for doc in docs_to_load:
                vals = [att(doc).get() for att in self.attributes]
                self.treeview.insert("", "end", text=doc.name, values=vals, tags=CENTER)


    def display_search_results(self, search_term):
        document_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
        search_results = document_manager.search_for_document( \
            search_term, return_name_only=False)
        self.load_documents(search_results)

        
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

