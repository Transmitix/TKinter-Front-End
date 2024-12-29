import customtkinter as ctk
import os
import webbrowser
from datetime import datetime


class InboxPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title label
        self.title_label = ctk.CTkLabel(self, text="Inbox", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # File list display area
        self.file_listbox = ctk.CTkTextbox(self, width=800, height=400, state="disabled")
        self.file_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Refresh button to reload files
        self.refresh_button = ctk.CTkButton(self, text="Refresh", command=self.load_sent_files)
        self.refresh_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Load the sent files on initialization
        self.sent_files_folder = "Files/received_files"  # Path to the folder where files are stored
        self.load_sent_files()

    def load_sent_files(self):
        # Run modout.py script
        modout_script_path = "Scripts/mod_out.py"
        if os.path.exists(modout_script_path):
            os.system(f"python {modout_script_path}")


        """Load the list of received files from the folder."""
        self.file_listbox.configure(state="normal")
        self.file_listbox.delete("1.0", "end")

        

        # Ensure the directory exists
        if not os.path.exists(self.sent_files_folder):
            os.makedirs(self.sent_files_folder)

        # Get files and their modification times
        files_with_time = []
        for file in os.listdir(self.sent_files_folder):
            filepath = os.path.join(self.sent_files_folder, file)
            if os.path.isfile(filepath):
                mod_time = os.path.getmtime(filepath)
                files_with_time.append((file, mod_time))

        # Sort files by modification time (latest first)
        files_with_time.sort(key=lambda x: x[1], reverse=True)

        if not files_with_time:
            self.file_listbox.insert("end", "No files received yet.\n")
        else:
            for file, mod_time in files_with_time:
                # Format the modification time
                formatted_time = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
                # Add padding, container, and display time
                self.file_listbox.insert("end", "  ┌────────────────────────────\n")
                self.file_listbox.insert("end", f"  │ {formatted_time}  -  {file}\n", "file")
                self.file_listbox.insert("end", "  └────────────────────────────\n\n")

        self.file_listbox.configure(state="disabled")
        self.add_clickable_file_links([file for file, _ in files_with_time])

    def add_clickable_file_links(self, files):
        """Enable clickable links for the files."""
        self.file_listbox.tag_config("file", foreground="light blue", underline=False)
        self.file_listbox.configure(state="normal")

        for file in files:
            start_index = self.file_listbox.search(file, "1.0", stopindex="end")
            if start_index:
                end_index = f"{start_index}+{len(file)}c"
                self.file_listbox.tag_add("file", start_index, end_index)
                self.file_listbox.tag_bind("file", "<Button-1>", lambda event, filename=file: self.open_file(filename))

        self.file_listbox.configure(state="disabled")

    def open_file(self, filename):
        """Open the selected file with the default application."""
        filepath = os.path.join(self.sent_files_folder, filename)
        if os.path.exists(filepath):
            webbrowser.open(filepath)
        else:
            print(f"File not found: {filepath}")