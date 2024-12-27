import customtkinter as ctk
import subprocess

class ChatPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title label
        self.title_label = ctk.CTkLabel(self, text="Chat Now!", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Connect button
        self.connect_button = ctk.CTkButton(self, text="Connect", command=self.loading)
        self.connect_button.grid(row=0, column=1, padx=10, pady=10)

        # Chat display area
        self.chat_display = ctk.CTkTextbox(self, width=500, height=400, state="disabled")
        self.chat_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Input field
        self.input_field = ctk.CTkEntry(self, width=400, placeholder_text="Type your message here...")
        self.input_field.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Upload button
        self.upload_button = ctk.CTkButton(self, text="Upload", command=self.upload)
        self.upload_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Send button
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=2, padx=10, pady=10)

    def send_message(self):
        message = self.input_field.get()
        if message:
            # Display message in the chat display
            self.chat_display.configure(state="normal")
            self.chat_display.insert("end", f"You: {message}\n")
            self.chat_display.configure(state="disabled")
            
            # Clear input field
            self.input_field.delete(0, "end")
    
    def upload(self):
        print("Upload button clicked")
        # Add your upload functionality here

    def loading(self):
        try:
            cmd = ["python3", "/home/thevinduk/Repositories/TKinter-Front-End/Scripts/nack1r.py"]
            print(f"Executing command: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("nack1r.py started successfully")
            else:
                print(f"Error starting nack1r.py: {result.stderr}")
                print(f"Command output: {result.stdout}")
        except Exception as e:
            print(f"Failed to start nack1r.py: {str(e)}")

