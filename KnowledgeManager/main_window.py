# 11/6/22


from tkinter import BOTH, Button, Entry, Frame, Tk, X, Y

from document_list_frame import DocumentListFrame
from document_details_frame import DocumentDetailsFrame
from filters_frame import FiltersFrame
from gui_functions import add_new_document
from gui_resources import *
from globals import doc_manager


class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master 

        # ---------------------------------------------------------------------
        # Main Window - Contains top control panel, filters panel, and doc list
        self.main_window = Frame(self.master,
            STANDARD_FRAME_ATTRIBUTES,
            width=400, height=400)
        self.main_window.pack(fill=BOTH, expand=1, side="left")


        # Top Controls Panel - New Document button, Search Bar
        self.top_controls_panel = Frame(self.main_window, STANDARD_PANEL_ATTRIBUTES)
        self.top_controls_panel.pack(fill=X)

        self.new_document_button = Button(self.top_controls_panel, 
            PRIMARY_BUTTON_ATTRIBUTES_MEDIUM,
            command=self.on_add_new_document,
            text="New Document")
        self.new_document_button.pack(side="left")


        # Search bar - Entry, Search button
        self.search_bar_panel = Frame(self.top_controls_panel, STANDARD_PANEL_ATTRIBUTES)
        self.search_bar_panel.pack(padx=10, pady=5)

        self.search_bar_entry = Entry(self.search_bar_panel, width=30)
        self.search_bar_entry.bind("<Return>", self.get_search_results)
        self.search_bar_entry.pack(side="left", padx=20, pady=5)

        self.search_button = Button(self.search_bar_panel,
            SECONDARY_BUTTON_ATTRIBUTES,
            command=self.get_search_results,
            text="Search")
        self.search_button.pack(side="right", padx=5, pady=5)
    

        # ---------------------------------------------------------------------
        # Filters Panel - Add filters to document list results

        self.filters_panel = FiltersFrame(self.main_window)
        self.filters_panel.pack(fill=X)


        # ---------------------------------------------------------------------
        # Side Panel - Contains individual document details, control, preview

        self.side_panel = DocumentDetailsFrame(self.master)
        self.side_panel.pack(side="right", fill=Y)


        # ---------------------------------------------------------------------
        # Document list frame - Displays list of documents

        self.document_list_frame = DocumentListFrame(self.main_window, self.side_panel)
        self.document_list_frame.pack(fill=BOTH)

        self.side_panel.set_notifier(self.document_list_frame.load_documents)
        self.filters_panel.set_notifier(self.document_list_frame.load_documents)


    def on_add_new_document(self):
        add_new_document()
        doc_manager.load_documents()
        self.document_list_frame.load_documents()

    def get_search_results(self, *args):
        doc_manager.set_active_search_term(self.search_bar_entry.get())
        doc_manager.load_documents()
        self.document_list_frame.load_documents()



if __name__ == "__main__":
    root = Tk()
    root.title("James's Knowledge Manager - v0.0 - 11/6/22")
    MainWindow(root)
    root.mainloop()
