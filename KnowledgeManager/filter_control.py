# 11/26/22

from tkinter import Button, Frame, Label, StringVar, Toplevel, ttk

from gui_resources import *
from globals import doc_manager


class FilterControl(Frame):

    def __init__(self, master, filter_name):
        Frame.__init__(self, master, 
            INNER_PANEL_ATTRIBUTES)

        # Needed to access the correct doc_manager active filter dict entry
        self.filter_name = filter_name

        # Functions meant to carry out updates upon certain actions
        self.notifiers = []

        self.add_button = Button(self,
            SECONDARY_BUTTON_ATTRIBUTES,
            text="Add",
            command=self.open_filter_selector)
        self.add_button.pack()

        self.active_filters_frame = Frame(self,
            INNER_PANEL_ATTRIBUTES)
        self.active_filters_frame.pack()


    def set_notifier(self, notifier_function):
        self.notifiers.append(notifier_function)

    def notify(self):
        for notifier_function in self.notifiers:
            notifier_function()


    def load(self):
        """ Use the load function to load all the filters to select from """
        self.filter_set = self.load_function()

    def open_filter_selector(self, *args):
        """ Open a combobox allowing user to select a filter to add """
        self.load()

        new_filter = FilterSelectDialog(self, self.filter_set).show()

        if new_filter is not None:
            self.add_active_filter(new_filter)


    def add_active_filter(self, new_filter):
        doc_manager.add_active_filter(self.filter_name, new_filter)
        self.refresh_active_filters_buttons()
        self.notify()

    def remove_active_filter(self, filter_to_remove):
        doc_manager.remove_active_filter(self.filter_name, filter_to_remove)
        self.refresh_active_filters_buttons()
        self.notify()

        
    def refresh_active_filters_buttons(self):
        # Destroy all existing filter buttons
        for filter_button in self.active_filters_frame.winfo_children():
            filter_button.destroy()
        # Now add a filter button for each active filter
        for filter in doc_manager.active_filters[self.filter_name]:
            filter_button = ActiveFilterBadge(self.active_filters_frame, 
                filter, self.remove_active_filter)
            filter_button.pack(pady=1)

    def set_load_function(self, load_function):
        self.load_function = load_function

    def set_filter_function(self, filter_function):
        self.filter_function = filter_function


class ActiveFilterBadge(Button):
    def __init__(self, master, filter, remove_filter_function):
        Button.__init__(self, master, 
            BADGE_BUTTON_ATTRIBUTES,
            text=filter,
            command=self.remove_filter)
        self.remove_filter_function = remove_filter_function
        self.filter = filter

    def remove_filter(self):
        self.remove_filter_function(self.filter)
        self.destroy()



class FilterSelectDialog(Toplevel):
    """ Pop up window where user can select a filter to add """
    def __init__(self, master, filter_set):
        Toplevel.__init__(self, master)

        self.current_selection = StringVar()
        self.filters_menu = ttk.Combobox(self,
            textvariable=self.current_selection)
        self.filters_menu["values"] = filter_set

        self.filters_menu.bind("<<ComboboxSelected>>", self.on_add)
        self.filters_menu.bind("<Button-1>", self.on_drop)

        self.filters_menu.pack(padx=5, pady=5)

        # Position the filters pop up window right over the button
        x = master.winfo_rootx() - 60
        y = master.winfo_rooty() - 35
        self.geometry("+{x}+{y}".format(x=x, y=y))

        self.title("Select filter")
        self.transient(master=master)

    def on_drop(self, event=None):
        """ Make it so that clicking the empty space in the combobox
        makes it open as a drop down instead of setting keyboard focus."""
        self.event_generate("<Down>")

    def on_add(self, event=None):
        self.destroy()

    def show(self):
        self.filters_menu.focus()
        self.wait_window()
        return self.current_selection.get()



