import customtkinter as ctk
from pages.home import HomePage
from pages.file_transmission import FileTransmissionPage
from pages.messaging import MessagingPage
from pages.file_receiver import FileReceiverPage

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Tkinter Frontend App")
        self.frames = {}

        for F in (HomePage, FileTransmissionPage, MessagingPage, FileReceiverPage):
            page_name = F.__name__
            frame = F(parent=self.root, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()