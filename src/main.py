import customtkinter as ctk
from pages.post import PostPage
from pages.sent import SentPage
from pages.chat import ChatPage
from pages.inbox import InboxPage


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TransmittixApp")
        self.frames = {}

        # Create a main container with a navigation pane on the left
        self.main_container = ctk.CTkFrame(self.root)
        self.main_container.grid(row=0, column=0, sticky="nsew")

        # Configure grid layout for the main container
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.main_container.rowconfigure(0, weight=1)
        self.main_container.columnconfigure(1, weight=1)

        # Create navigation pane
        self.nav_pane = ctk.CTkFrame(self.main_container, width=200)
        self.nav_pane.grid(row=0, column=0, sticky="ns")

        # Create content area
        self.content_area = ctk.CTkFrame(self.main_container)
        self.content_area.grid(row=0, column=1, sticky="nsew")

        # Add navigation buttons to the left pane
        nav_buttons = [
            ("Post", "PostPage"),
            ("Inbox", "InboxPage"),
            ("Sent", "SentPage"),
            ("Chat", "ChatPage")
        ]

        for text, page_name in nav_buttons:
            button = ctk.CTkButton(
                master=self.nav_pane,
                text=text,
                command=lambda page=page_name: self.show_frame(page)
            )
            button.pack(pady=10, padx=10, fill="x")

        # Initialize frames for each page
        for F in (PostPage, InboxPage, SentPage, ChatPage):
            page_name = F.__name__
            frame = F(parent=self.content_area, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PostPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    root = ctk.CTk()
    root.geometry("1000x600")
    app = MainApp(root)
    root.mainloop()
