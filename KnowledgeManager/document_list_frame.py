# 11/6/22

from tkinter import BOTH, CENTER, Frame, Label, Tk, ttk, VERTICAL, Y

from DocumentManagement.document_editor import DocumentEditor
from DocumentManagement.document_manager import DocumentManager
#from DocumentManagement.document import Document
from globals import DEFAULT_DOCUMENT_REPO_PATH


class DocumentListFrame(Frame):
    """ 
    Displays document data in tabular form 

    Each document is listed as a row in the table, with attributes arranged
    in columns (e.g., Name, Author, Date, Category, keyword, etc.)
    """

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master 

        self.treeview = ttk.Treeview(self.master)
        self.treeview["columns"] = (\
            "Category", 
            "Keywords",
            )

        self.treeview.column("#0")
        self.treeview.column("Category", anchor=CENTER)
        self.treeview.column("Keywords", anchor=CENTER)

        self.treeview.heading("#0", text="Name")
        self.treeview.heading("Category", text="Category")
        self.treeview.heading("Keywords", text="Keywords")\

        scrollbar = ttk.Scrollbar(self.master, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill=Y)

        self.treeview.pack(padx=5, pady=5, fill=BOTH, expand=1)
        #self.treeview.bind("<<TreeviewSelect>>", self._document_selected)
        self.treeview.bind("<Double-1>", self._document_selected)

        self.load_documents()


    def load_documents(self, documents=None):
        self._clear_list()
        document_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
        docs_to_load = documents
        # If no list of document specified, load all the document in the repo
        if documents is None:
            docs_to_load = document_manager.get_documents()

        for doc in docs_to_load:

            vals = (\
                self._format_value(doc.category), 
                self._format_value(doc.keywords)
                )
            self.treeview.insert("", "end", text=doc.name, values=vals, tags=CENTER)


    def display_search_results(self, search_term):
        document_manager = DocumentManager(DEFAULT_DOCUMENT_REPO_PATH)
        search_results = document_manager.search_for_document( \
            search_term, return_name_only=False)
        self.load_documents(search_results)


        
    def _clear_list(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)


    def _document_selected(self, event):
        for selected_document in self.treeview.selection():
            document = self.treeview.item(selected_document)
            print(document)
            print(document["text"])
            doc_editor = DocumentEditor(DEFAULT_DOCUMENT_REPO_PATH)
            doc_editor.open_document_in_text_editor(document["text"])


    def _format_value(self, column_value):
        """ 
        Convert table value into appropriate string representation

        - Lists are converted into comma-separated values
        - None is converted into an empty string
        """
        if column_value is None:
            return ""
        elif isinstance(column_value, list):
            return ", ".join(column_value)
        else:
            return column_value


    
