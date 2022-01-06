import tkinter
from tkinter import Tk, messagebox
import better_widgets.widgets as wd

class App(Tk):
    """
    Subclasses the Tk() function, performing an initial configuration of the main window
    and creating template methods for showing widgets, setting bindings and running the app.
    """
    def __init__(self, title: str, iconpath: str = None, menu: bool = True, geometry: str = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.titletext = title
        self.iconpath = iconpath
        # Set appearance
        self.title(self.titletext)
        if iconpath:
            self.iconbitmap(self.iconpath)
        
        # Load menu
        if menu:
            self.menu = wd.MainMenu(self)

        # Set geometry:
        if geometry:
            try:
                self.geometry(geometry)
            except tkinter.TclError as err:
                raise ValueError(f"Wrong geometry string: {geometry}") from err
     
        # Set initial minsize 
        self.update()
        self.initwidth = self.winfo_reqwidth()
        self.initheight = self.winfo_reqheight()
        self.minsize(width=self.initwidth, height=self.initheight)

        # Build a dict with a reference to all non-static widgets
        # Needs to be implemented
        self.all_widgets = self._build_widget_reference_dict()
          
        # Set bindings
        # Needs to be implemented
        self._set_bindings()

    def update_screen_min_size(self) -> None:
        """
        Update minimum screen size depending on all widgets inside it.
        """
        self.update()
        self.minsize(width=self.winfo_reqwidth(), height=self.winfo_reqheight())

    def really_quit(self, title: str = "Quit?", msg: str = "Really quit?") -> None:
        """
        Intercept close window event and ask for confirmation
        """
        if messagebox.askokcancel(title, msg):
            self.destroy()

    def run(self) -> None:
        """
        Run the app.
        """
        self.mainloop()

    def _build_widget_reference_dict(self) -> dict:
        '''
        Builds a dictionary that stores a reference to all non-static widgets to make it easier to access them.
        Implement as needed.
        '''
        widgets = dict()
        # Add widgets here
        return widgets

    def _set_bindings(self) -> None:
        '''
        Initialize bindings of widgets with callbacks. Implement as needed.
        '''
        # Add bindings here

        # Ask to confirmation before closing
        # self.protocol('WM_DELETE_WINDOW', self.really_quit)

    def test_callback(self, caller: tkinter.Widget, logger = None) -> None:
        """
        Debugging method to test widget action callbacks. Accepts a logger instance if you prefer to log the message instead of printing it.
        """
        if logger:
            try:
                logger.debug(f"Test callback called by {caller}")
            except AttributeError:
                print(f"Invalid logger passed to test callback method: {logger}")
        else:
            print(f"Test callback called by {caller}")

def test():
    """
    Simple test window
    """
    app = App("Test window", None, True, None)
    app.run()

if __name__ == '__main__':
    test()