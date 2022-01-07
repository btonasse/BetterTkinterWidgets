import sys
from pathlib import Path
packagepath = Path(__file__)
sys.path.append(str(packagepath.parent.parent.absolute()) + '/src')

from better_widgets.widgets import myText, DynamicLabel
from better_widgets import App
from tkinter import StringVar, Button, Frame, messagebox

class wTest(App):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("Widgets test")
        self.config(bg="black")
        
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
        self.text_get_btn = Button(self.text_frame, text="Get", command=self.get_all)
        self.text_set_btn = Button(self.text_frame, text="Set", command=self.set_all)
        self.text_listset_btn = Button(self.text_frame, text="List set", command=self.list_set)

        self.label_frame.pack(pady=5, padx=5)
        self.dynamic_lbl_1.pack()
        self.change_btn_1.pack()
        self.dynamic_lbl_2.pack()
        self.change_btn_2.pack()

        self.text_frame.pack(pady=5, padx=5)
        self.text_widget.pack()
        self.text_get_btn.pack()
        self.text_set_btn.pack()
        self.text_listset_btn.pack()


        self.update_screen_min_size()

    def add_sign(self, label: DynamicLabel) -> None:
        label.value += "!"
        self.update_screen_min_size()

    def get_all(self) -> None:
        messagebox.showinfo(message=self.text_widget.value)

    def set_all(self) -> None:
        self.text_widget.value = "Replaced the text with this."

    def list_set(self) -> None:
        self.text_widget.value = ["item 1", 2, {"a", 3}]

if __name__ == '__main__':
    app = wTest()
    app.run()