import subprocess
import os
from tkinter import filedialog
import customtkinter as ctk

class FileTransmissionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.file_path = None

        select_button = ctk.CTkButton(self, text="Select File", command=self.select_file)
        select_button.pack()

        self.file_label = ctk.CTkLabel(self, text="No file selected")
        self.file_label.pack()

        process_button = ctk.CTkButton(self, text="Upload", command=self.process_file)
        process_button.pack()

        transmit_button = ctk.CTkButton(self, text="Transmit", command=self.transmit_file)
        transmit_button.pack()

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
            self.output_file = os.path.join(directory, f"Mod{name}{ext}")

            # Run mod_in.py
            subprocess.run(["python", "/home/thevinduk/Transmitix/TKinter/tkinter-frontend-app/Scripts/mod_in.py", self.file_path, self.output_file])
        else:
            self.file_label.configure(text="No file selected. Please select a file first.")

    def transmit_file(self):
        if hasattr(self, 'output_file') and self.output_file:
            # Run nack1.py with the output file as the file source
            subprocess.run(["python3", "/home/thevinduk/Transmitix/TKinter/tkinter-frontend-app/Scripts/nack1.py", "--file_path", self.output_file])
        else:
            self.file_label.configure(text="No output file to transmit. Please process a file first.")