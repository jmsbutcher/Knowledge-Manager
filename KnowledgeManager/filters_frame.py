# 11/26/22

from tkinter import Button, Frame, Label, ttk, X

from DocumentManagement.document_manager import DocumentManager
from filter_control import FilterControl
from globals import DEFAULT_DOCUMENT_REPO_PATH
from gui_resources import *
from globals import doc_manager


class FiltersFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, 
            STANDARD_PANEL_ATTRIBUTES)

        # Functions meant to carry out updates upon certain actions
        self.notifiers = []

        self.filters_label = Label(self,
            STANDARD_LABEL_ATTRIBUTES,
            text="Filters:")
        self.filters_label.pack(side="left", expand=True)

        self.category_control = FilterControl(self, "Category")
        self.category_control.set_load_function(\
            doc_manager.get_all_categories)
        self.category_control.set_filter_function(\
            doc_manager.filter_by_category)
        self.category_control.set_notifier(self.notify)
        self.category_control.pack(side="left", expand=True)

        self.keyword_control = FilterControl(self, "Keywords")
        self.keyword_control.set_load_function(\
            doc_manager.get_all_keywords)
        self.keyword_control.set_filter_function(\
            doc_manager.filter_by_keyword)
        self.keyword_control.set_notifier(self.notify)
        self.keyword_control.pack(side="left", expand=True)


    def set_notifier(self, notifier_function):
        self.notifiers.append(notifier_function)

    def notify(self):
        for notifier_function in self.notifiers:
            notifier_function()
