import sys
from pathlib import Path
packagepath = Path(__file__)
sys.path.append(str(packagepath.parent.parent.absolute()) + '/src')

from better_widgets.widgets import myText, DynamicLabel, myCheckBox, myEntry, myListbox
from better_widgets import App
from tkinter import StringVar, Button, Frame, messagebox, Widget
from typing import Union
class wTest(App):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("Widgets test")
        self.config(bg="darkgrey")
        
        # Widgets
        self.label_frame = Frame(self, bg="lightgrey")
        self.test_stringvar = StringVar(value="Label with predetermined textvariable")
        self.dynamic_lbl_1 = DynamicLabel(self.label_frame, textvariable=self.test_stringvar)
        self.change_btn_1 = Button(self.label_frame, text="Add !", command=lambda : self.add_sign(self.dynamic_lbl_1))
        self.dynamic_lbl_2 = DynamicLabel(self.label_frame)
        self.dynamic_lbl_2.value = "Label without predetermined textvariable"
        self.change_btn_2 = Button(self.label_frame, text="Add !", command=lambda : self.add_sign(self.dynamic_lbl_2))

        self.text_frame = Frame(self, bg="white")
        self.text_widget = myText(self.text_frame, width=30, height=5)
        self.text_get_btn = Button(self.text_frame, text="Get", command=lambda : self.get_all(self.text_widget))
        self.text_set_btn = Button(self.text_frame, text="Set", command=lambda : self.set_all(self.text_widget, "Replaced the text with this."))
        self.text_listset_btn = Button(self.text_frame, text="List set", command=self.text_list_set)

        self.check_frame = Frame(self, bg="lightgrey")
        self.checkbox = myCheckBox(self.check_frame)
        self.check_btn = Button(self.check_frame, text="Is checked?", command=self.is_checked)

        self.entry_frame = Frame(self, bg="white")
        self.entry = myEntry(self.entry_frame)
        self.entry_get_btn = Button(self.entry_frame, text="Get", command=lambda : self.get_all(self.entry))
        self.entry_set_btn = Button(self.entry_frame, text="Set", command=lambda : self.set_all(self.entry, "Replaced the text with this."))

        self.list_frame = Frame(self, bg="lightgrey")
        self.listbox = myListbox(self.list_frame, height=4)
        self.listbox.value = ["First", "Second", "Third", "Fourth"]
        self.list_getvals_btn = Button(self.list_frame, text="Get", command=lambda : self.get_all(self.listbox))
        self.list_setvals_btn = Button(self.list_frame, text="Set", command=lambda : self.set_all(self.listbox, ["Newfirst", "Newsecond", "Newthird", "Newfourth"]))
        self.list_selecttwo_btn = Button(self.list_frame, text="Select two", command=self.select_two)
        self.list_selectfirst_btn = Button(self.list_frame, text="Select first", command=self.select_first)

        
        self.label_frame.pack(pady=5, padx=10, fill='both')
        self.dynamic_lbl_1.pack()
        self.change_btn_1.pack()
        self.dynamic_lbl_2.pack()
        self.change_btn_2.pack()

        self.text_frame.pack(pady=5, padx=10, fill='both')
        self.text_widget.pack()
        self.text_get_btn.pack()
        self.text_set_btn.pack()
        self.text_listset_btn.pack()

        self.check_frame.pack(pady=5, padx=10, fill='both')
        self.checkbox.pack()
        self.check_btn.pack()

        self.entry_frame.pack(pady=5, padx=10, fill='both')
        self.entry.pack()
        self.entry_get_btn.pack()
        self.entry_set_btn.pack()

        self.list_frame.pack()
        self.listbox.pack()
        self.list_getvals_btn.pack()
        self.list_setvals_btn.pack()
        self.list_selecttwo_btn.pack()
        self.list_selectfirst_btn.pack()

        self.update_screen_min_size()

    def add_sign(self, label: DynamicLabel) -> None:
        label.value += "!"
        self.update_screen_min_size()

    def get_all(self, widget: Widget) -> None:
        print(repr(widget.value), type((widget.value)))
        messagebox.showinfo(message=widget.value)

    def set_all(self, widget: Widget, value: Union[str, list]) -> None:
        widget.value = value

    def text_list_set(self) -> None:
        self.text_widget.value = ["item 1", 2, {"a", 3}]

    def is_checked(self) -> None:
        if self.checkbox.value:
            isit = "Yes"
        else:
            isit = "No"
        messagebox.showinfo(message=isit)

    def select_two(self) -> None:
        self.listbox.set_selection(["Newfirst", "First", "Newthird", "Third"])
    
    def select_first(self) -> None:
        self.listbox.select_first()





if __name__ == '__main__':
    app = wTest()
    app.run()