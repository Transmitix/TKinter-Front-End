import subprocess
import os
from tkinter import filedialog
import customtkinter as ctk
import threading
import time

class PostPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Configure grid layout
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)  # Title
        self.grid_rowconfigure(1, weight=1)  # Dropbox
        self.grid_rowconfigure(2, weight=0)  # Selected file and upload button
        self.grid_rowconfigure(3, weight=0)  # Send button
        self.grid_columnconfigure(0, weight=1)

        # Title label
        self.title_label = ctk.CTkLabel(self, text="Send a file!", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Connect button
        self.send_button = ctk.CTkButton(self, text="Connect", command=self.loading)
        self.send_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Dropbox area (Row 1)
        self.dropbox_frame = ctk.CTkFrame(self, height=400, width=800, border_width=2, border_color="gray")
        self.dropbox_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.dropbox_label = ctk.CTkLabel(
            self.dropbox_frame,
            # text="Drag and Drop files here\nor click 'Add File' button below",
            text = "Select a file to upload",
            font=("Arial", 14),
            text_color="gray"
        )
        self.dropbox_frame.configure(border_width=2, border_color="gray",)# border_dash=(5, 5))
        self.dropbox_label.place(relx=0.5, rely=0.5, anchor="center")

        # Add File button = select button (Row 1)
        self.select_button = ctk.CTkButton(self.dropbox_frame, text="Select File", command=self.select_file)
        self.select_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.select_button.place(relx=0.5, rely=0.7, anchor="center")
        
        # File display and Upload button (Row 2)
        self.file_label = ctk.CTkLabel(self, text="No file selected", anchor="w")
        self.file_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.process_button = ctk.CTkButton(self, text="Upload", command=self.process_file)
        self.process_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Send button (Row 3)
        self.transmit_button = ctk.CTkButton(self, text="Send File", command=self.transmit_file, width=200)
        self.transmit_button.grid(row=3, column=0, columnspan=3, pady=20, sticky="n")

        # Initialize file-related attributes
        self.selected_file_path = None
        self.output_file_path = None


    def select_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a file")
        if self.file_path:
            self.file_label.configure(text=self.file_path if self.file_path else "No file selected")
            self.file_label.configure(text=self.file_path if self.file_path else "No file selected")
        else:
            self.file_label.configure(text="No file selected")

    def process_file(self):
        if self.file_path:
            # Determine the output file path
            directory, filename = os.path.split(self.file_path)
            name, ext = os.path.splitext(filename)
            self.output_file = os.path.join(directory, f"Mod{name}{ext}")

            # Run mod_in.py
            subprocess.run(["python", "", self.file_path, self.output_file])
        else:
            self.file_label.configure(text="No file selected. Please select a file first.")

    def transmit_file(self):
        if hasattr(self, 'output_file') and self.output_file:
            # Run nack1.py with the output file as the file source
            subprocess.run(["python3", "", "--file_path", self.output_file])
        else:
            self.file_label.configure(text="No output file to transmit. Please process a file first.")
    
    # timer_id = None

    def loading(self):
        pass

    def display_files(self):
        """Display the list of added files."""
        self.file_listbox.configure(state="normal")
        self.file_listbox.delete("1.0", "end")
        if not self.files_to_send:
            self.file_listbox.insert("end", "No files added.\n")
        else:
            for file in self.files_to_send:
                self.file_listbox.insert("end", f"{file}\n")
        self.file_listbox.configure(state="disabled")
