import customtkinter as ctk
from tkinter import filedialog
import os
import subprocess

class FileTransmissionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.file_path = None

        label = ctk.CTkLabel(self, text="File Transmission Page")
        label.pack(side="top", fill="x", pady=10)

        self.file_label = ctk.CTkLabel(self, text="No file selected")
        self.file_label.pack(side="top", fill="x", pady=10)

        select_button = ctk.CTkButton(self, text="Select File", command=self.select_file)
        select_button.pack()

        process_button = ctk.CTkButton(self, text="Upload", command=self.process_file)
        process_button.pack()

        button1 = ctk.CTkButton(self, text="Go to Home",
                                command=lambda: controller.show_frame("HomePage"))
        button1.pack()
        button2 = ctk.CTkButton(self, text="Go to Messaging",
                                command=lambda: controller.show_frame("MessagingPage"))
        button2.pack()
        button3 = ctk.CTkButton(self, text="Go to File Receiver",
                                command=lambda: controller.show_frame("FileReceiverPage"))
        button3.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        self.file_label.configure(text=self.file_path if self.file_path else "No file selected")

    def process_file(self):
        if self.file_path:
            # Determine the output file path
            directory, filename = os.path.split(self.file_path)
            name, ext = os.path.splitext(filename)
            output_file = os.path.join(directory, f"Mod{name}{ext}")

            # Run mod_in.py
            subprocess.run(["python", "/home/thevinduk/Transmitix/TKinter/tkinter-frontend-app/Scripts/mod_in.py", self.file_path, output_file])
        else:
            self.file_label.configure(text="No file selected. Please select a file first.")