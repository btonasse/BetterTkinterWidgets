import tkinter as tk
from tkinter import ttk, filedialog
class MainMenu(tk.Menu):
    """
    Subclass of Menu widget that automatically associates it to root
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master = master

        # Associate menu with root
        self.master.config(menu=self)      

class MainWindow(tk.Frame):
    """
    Subclass of Frame intended to be used as the main 'canvas' of the window,
    under which all subframes (and actual widgets) are added.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master = master

        # Add subframes
        # Show widgets
        self.show_widgets()

    def show_widgets(self) -> None:
        '''
        Show child widgets and call the same method for each of them, so each widget enter the grid in succession
        Implement as needed.
        ''' 
        # Configure grid weights
        #self.rowconfigure(0, weight=1)

        # Show each subframe
        # self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        
        # Call the same method of each child frame
        # self.left_frame.show_widgets()
        
        # Update root widget's minsize
        self.master.update_screen_min_size()

class myText(tk.Text):
    """
    Subclass Text widget, adding a default scrollbar and methods for easy content read-write.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master=master
        self.scroll = ttk.Scrollbar(self.master, command=self.yview)
        
        self.config(undo=True, maxundo=10, wrap='word', yscrollcommand=self.scroll.set, padx=4)
    
    def get_all(self) -> str:
        '''
        Get all text in the textbox, trimming out any whitespace after the end
        '''
        return self.get('1.0', 'end').rstrip()
    
    def set_text(self, text: str) -> None:
        '''
        Replaces text on the widget
        '''
        self.clear()
        self.insert('end', text)
        self.edit_reset() # Clear undo stack
    
    def set_from_list(self, lst: list) -> None:
        '''
        Replaces text on the widget with the contents of a list
        '''
        self.clear()
        self.insert('end', '\n'.join(lst))
        self.edit_reset() # Clear undo stack

    def clear(self) -> None:
        '''
        Clear text widget
        '''
        self.delete('1.0', 'end')
        self.edit_reset()

class DynamicLabel(tk.Label):
    """
    Label with set() and get() methods. If no textvariable is provided, an internal StringVar is used.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master = master
        self.value = None
        # Implement set/get and textvariable without the need of an external StringVar
        for kwarg, value in kwargs.items():
            if kwarg == 'textvariable':
                if not isinstance(value, tk.StringVar):
                    raise ValueError(f'Textvariable must be StringVar')
                self.value = value
        if not self.value:
            self.value = tk.StringVar()
            self.config(textvariable=self.value)

    def set(self, txt) -> None:
        self.value.set(txt)
    def get(self) -> None:
        return self.value.get()

class myCheckBox(ttk.Checkbutton):
    """
    Checkbox with an IntVar if no 'variable' argument is passed upon instantiation.
    Also implements get and set methods.
    """
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master = master 
        self.value = None
        for kwarg, value in kwargs.items():
            if kwarg == 'variable':
                if not isinstance(value, tk.IntVar):
                    raise ValueError(f'variable must be IntVar')
                self.value = value
        if not self.value:
            self.value = tk.IntVar()
            self.config(variable=self.value)
    
    def set(self, flag: int) -> None:
        if flag not in [0, 1]:
            raise ValueError(f'Checkbox can only be set to 0 or 1, not {flag}')
        self.value.set(flag)
    def get(self) -> None:
        return self.value.get()

class myEntry(ttk.Entry):
    '''
    Checkbox with an StringVar if no 'textvariable' argument is passed upon instantiation.
    Also implements get and set methods (using self.value attribute).
    Unlike default ttk.Entry, exportselection defaults to 0.
    '''
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master=master
        self.config(exportselection=0)
        self.value = None
        for kwarg, value in kwargs.items():
            if kwarg == 'textvariable':
                if not isinstance(value, tk.StringVar):
                    raise ValueError(f'Textvariable must be StringVar')
                self.value = value
        if not self.value:
            self.value = tk.StringVar()
            self.config(textvariable=self.value)
    
    def set(self, txt) -> None:
        self.value.set(txt)
    def get(self) -> None:
        return self.value.get()

class myListbox(tk.Listbox):
    '''
    Subclass of Listbox with embedded Scrollbar and a better interface to read and write values:
    set_items():
        Pass a list of strings to use them to populate the listbox
        
    '''
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__ (master=master, *args, **kwargs)
        self.master = master
        self.scroll = ttk.Scrollbar(self.master, command=self.yview)
        self.config(exportselection=0, activestyle='none', yscrollcommand=self.scroll.set)
        self.value = None
        for kwarg, value in kwargs.items():
            if kwarg == 'listvariable':
                if not isinstance(value, tk.StringVar):
                    raise ValueError(f'Listvariable must be StringVar')
                self.value = value
        if not self.value:
            self.value = tk.StringVar()
            self.config(listvariable=self.value)
    
    def set_items(self, items: list) -> None:
        '''
        Set list items. List elements must be strings.
        '''
        try:
            as_str = ' '.join(items)
        except TypeError as err:
            raise TypeError("At least one list item is not a string.") from err
        self.value.set(as_str)
    
    def get_selection(self) -> list:
        '''
        Get list selection for listboxes. Always return a list, even if there's only one item selected
        '''
        selected_indices = self.curselection()
        if selected_indices:
            return [self.get(i) for i in selected_indices]
        return [None]
    
    def set_selection(self, items: list) -> None:
        '''
        Activate items in the list given as parameter
        '''
        all_options = self.get(0, 'end')
        for i, option in enumerate(all_options):
            if option in items:
                self.selection_set(i)
            else:
                self.selection_clear(i)
    
    def select_first(self) -> None:
        '''
        Selects first item on the list. Raises IndexError if list is empty.
        '''
        self.selection_clear(0, 'end')
        if not self.get(1): # Index 0 is always a heading, so check index 1
            raise IndexError('List is empty')
        self.selection_set(1)
        self.activate(1) 

    def select_last(self) -> None:
        '''
        Selects last item on the list. Raises IndexError if list is empty.
        '''
        self.selection_clear(0, 'end')
        if not self.get(1): # Index 0 is always a heading, so check index 1
            raise IndexError('List is empty')
        self.selection_set('end')
        self.activate('end')

class myDialogBox(tk.Toplevel):
    '''
    Generic dialogbox class. Not to be instantiated, but subclassed.
    '''
    def __init__(self, master, iconpath: str = None, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.master=master
        if iconpath:
            self.iconbitmap(iconpath)
        self.return_var = dict() 

    
    def save_and_destroy(self) -> None:
        '''
        Implement this when subclassing
        '''
        pass

    def show(self) -> dict:
        '''
        Prevents losing focus until window is destroyed.
        Returns a dictionary with the value of all forms to the caller
        '''
        self.focus_set()
        self.grab_set()
        self.wait_window()
        return self.return_var
    
    def cancel(self) -> None:
        """
        Destroys the window and resets the return variable
        """
        self.return_var = dict()
        self.destroy()

class FileDialogButton(ttk.Button):
    """
    Button that opens a folder selection dialog.
    Has to be instantiated after an associated myEntry, where the path will be displayed. 
    Type is the type of file dialog to be opened. These are Tkinter's filedialog function names without the 'ask' prefix. Eg: directory or openfiles
    """
    def __init__(self, master, entry: myEntry, typ: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.master = master
        self.entry = entry
        self.config(command = self.callback)

        # Set appropriate filedialog function
        try:
            self.filedialog_function = getattr(filedialog, 'ask' + typ)
        except AttributeError as err:
            raise AttributeError("Valid values for 'typ' are the ask function names of Tkinter's filedialog module: openfilename, saveasfilename, directory etc.") from err

    def callback(self):
        """
        Opens the folder dialog
        """
        path = self.filedialog_function()
        self.entry.set(path)