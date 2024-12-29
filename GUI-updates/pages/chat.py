import customtkinter as ctk
import os
from datetime import datetime

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
        self.connect_button = ctk.CTkButton(self, text="Connect", command=self.connect)
        self.connect_button.grid(row=0, column=1, padx=10, pady=10)

        # # Chat display area
        # self.chat_display = ctk.CTkTextbox(self, width=500, height=400, state="disabled")
        # self.chat_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Scrollable chat display
        self.chat_display_frame = ctk.CTkScrollableFrame(self, width=500, height=400)
        self.chat_display_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.chat_display_frame.grid_columnconfigure(0, weight=1)  # Ensure bubbles expand to available space

        # Input field
        self.input_field = ctk.CTkEntry(self, width=400, placeholder_text="Type your message here...")
        self.input_field.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Send button
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, padx=10, pady=10)

        # Variable to track last received message
        self.last_received_message = None

        # Start periodic refresh for received messages
        self.refresh_received_messages()

    def send_message(self):
        message = self.input_field.get()
        if message:
            # # Display message in the chat display
            # self.chat_display.configure(state="normal")
            # self.chat_display.insert("end", f"You: {message}\n")
            # self.chat_display.configure(state="disabled")

            # Display message bubble
            self.add_message_bubble(message, "right")
            
            # Clear input field
            self.input_field.delete(0, "end")
            
            # save text as input file. with preamble and tail. saved to chat_text.txt in scripts
            self.save_text_file(message)

            # now start gnu radio transmitter. 
            # file to be transmitted= 'chat_text.txt'
            ############### add code ##############

    def save_text_file(self, message):
        ###### file path!
        with open('./TKinter/tkinter-frontend-app/src/scripts/preamble_chat.txt', 'rb') as f1: # change file pat for preamble_chat.txt
            preamble = f1.read()
    
        ###### file path!
        with open('./TKinter/tkinter-frontend-app/src/scripts/tail_chat.txt', 'rb') as f2: # change file pat for tail_chat.txt
            tail = f2.read()

        # Create the output file with preamble and end delimiter
        with open('./TKinter/tkinter-frontend-app/src/scripts/chat_text.txt', 'wb') as output_file:    ###### file path!
            output_file.write(preamble)        # Add preamble
            output_file.write(message.encode("utf-8"))      # Add message text
            output_file.write(tail)  # Add end delimiter

        print(f"Preamble and end delimiter added for chat message. saved in chat_text.txt")

    # timer_id = None

    def connect(self):
        # add loading animation or 
        # start running reciever code
        pass

    def add_message_bubble(self, message, alignment, timestamp=None):
        bubble = ctk.CTkFrame(self.chat_display_frame, corner_radius=15)
        bubble.grid_columnconfigure(0, weight=1)

        # Add message label
        message_label = ctk.CTkLabel(bubble, text=message, wraplength=300, fg_color="#d7f7df", text_color="green", corner_radius=15)
        message_label.pack(padx=10, pady=(5, 0))

        # Add timestamp if provided
        if timestamp:
            timestamp_label = ctk.CTkLabel(bubble, text=timestamp, font=("Arial", 8), text_color="gray")
            timestamp_label.pack(padx=10, pady=(0, 5))

        else:
            timestamp_label = ctk.CTkLabel(bubble, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), font=("Arial", 8), text_color="gray")
            timestamp_label.pack(padx=10, pady=(0, 5))

        row_index = len(self.chat_display_frame.winfo_children())
        bubble.grid(row=row_index, column=0, sticky="e" if alignment == "right" else "w", padx=(20, 0) if alignment == "right" else (0, 20), pady=5)

        # Auto-scroll to the bottom
        self.chat_display_frame.update_idletasks()
        self.chat_display_frame._scrollbar.set(1.0, 1.0)

    def refresh_received_messages(self):
        file_path = './TKinter/tkinter-frontend-app/src/scripts/received_chat.txt'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                new_message = file.read().strip()

            # Display new message only if it is different from the last received message
            if new_message and new_message != self.last_received_message:
                self.last_received_message = new_message
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.add_message_bubble(new_message, "left", timestamp)

        # Refresh every 30 seconds
        self.after(30000, self.refresh_received_messages)
