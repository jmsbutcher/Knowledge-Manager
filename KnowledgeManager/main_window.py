# 11/6/22

from tkinter import BOTH, Button, Entry, Frame, Label, Tk, X, Y

#from DocumentManagement.document_manager import DocumentManager
#from globals import DEFAULT_DOCUMENT_REPO_PATH
from document_list_frame import DocumentListFrame
from gui_functions import add_new_document


STANDARD_PANEL_ATTRIBUTES = {
    "borderwidth":"3", 
    "padx":5, 
    "pady":5, 
    "relief":"groove", 
    "bg":"#DDDDDD"
}

STANDARD_LABEL_ATTRIBUTES = {
    "padx":10, 
    "pady":3, 
    "font":("SegoeUI", 12, "bold")
}

PRIMARY_BUTTON_ATTRIBUTES = {
    "borderwidth":"3", 
    "padx":10, 
    "pady":3, 
    "relief":"groove", 
    "bg":"#88DDDD",
    "font":("SegoeUI", 12, "bold")
}


class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master 

        # ---------------------------------------------------------------------
        # Main Panel - Contains top control panel, filters panel, and doc list
        self.main_panel = Frame(self.master, borderwidth=5,
            relief="ridge", width=400, height=400, bg="gray")
        self.main_panel.pack(fill=BOTH, expand=1, side="left")


        # Top Controls Panel - New Document button, Search Bar
        self.top_controls_panel = Frame(self.main_panel, STANDARD_PANEL_ATTRIBUTES)
        self.top_controls_panel.pack(fill=X)

        self.new_document_button = Button(self.top_controls_panel, 
            PRIMARY_BUTTON_ATTRIBUTES,
            command=self.on_add_new_document,
            text="New Document")
        self.new_document_button.pack(side="left")


        # Search bar - Entry, Search button
        self.search_bar_panel = Frame(self.top_controls_panel)
        self.search_bar_panel.pack(padx=20, pady=5)

        self.search_bar_entry = Entry(self.search_bar_panel, width=30)
        self.search_bar_entry.bind("<Return>", self.get_search_results)
        self.search_bar_entry.pack(side="left", padx=20, pady=5)
    

        # Filters Panel - Add filters to document list results
        self.filters_panel = Frame(self.main_panel,
            STANDARD_PANEL_ATTRIBUTES)
        self.filters_panel.pack(fill=X)

        self.filters_label = Label(self.filters_panel,
            STANDARD_LABEL_ATTRIBUTES,
            text="Filters:")
        self.filters_label.grid(row=0, column=0)


        # Document list frame - Displays list of documents
        self.document_list_frame = DocumentListFrame(self.main_panel)
        self.document_list_frame.pack(fill=BOTH)


        # ---------------------------------------------------------------------
        # Side Panel - Contains individual document details, control, preview

        self.side_panel = Frame(self.master, borderwidth=5,
            relief="ridge", bg="gray", width=300)
        self.side_panel.pack(side="right", fill=Y)


    def on_add_new_document(self):
        add_new_document()
        self.document_list_frame.load_documents()

    def get_search_results(self, evt):
        self.document_list_frame.display_search_results(self.search_bar_entry.get())



root = Tk()
root.title("James's Knowledge Manager - v0.0 - 11/6/22")
MainWindow(root)
root.mainloop()
