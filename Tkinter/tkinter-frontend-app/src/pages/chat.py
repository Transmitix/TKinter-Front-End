import customtkinter as ctk
import subprocess
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
        self.connect_button = ctk.CTkButton(self, text="Connect", command=self.loading)
        self.connect_button.grid(row=0, column=1, padx=10, pady=10)

        # # Refresh button
        # self.refresh_button = ctk.CTkButton(self, text="Refresh", command=self.refresh)
        # self.refresh_button.grid(row=1, column=1, padx=10, pady=10)

        # # Chat display area
        # self.chat_display = ctk.CTkTextbox(self, width=500, height=400, state="disabled")
        # self.chat_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Scrollable chat display
        self.chat_display_frame = ctk.CTkScrollableFrame(self, width=500, height=400)
        self.chat_display_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.chat_display_frame.grid_columnconfigure(0, weight=1)  # Ensure bubbles expand to available space

        # Input field
        self.input_field = ctk.CTkEntry(self, width=400, placeholder_text="Type your message here...")
        self.input_field.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Send button
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.grid(row=3, column=2, padx=10, pady=10)

        # Variable to track last received message
        self.last_received_message = None

        # Start periodic refresh for received messages
        self.refresh_received_messages()

    def send_message(self):
        message = self.input_field.get()
        self.file_path = "/home/thevinduk/Repositories/TKinter-Front-End/Chats/Sent/message.txt"
        self.output_file_path = "/home/thevinduk/Repositories/TKinter-Front-End/Chats/Sent/message.txt"
        if message:
            # Write message to a text file
            with open(self.file_path, "w") as file:
                file.write(message)

            # # Display message in the chat display
            # self.chat_display.configure(state="normal")
            # self.chat_display.insert("end", f"You: {message}\n")
            # self.chat_display.configure(state="disabled")
            
            # Display message bubble
            self.add_message_bubble(message, "right")

            # Clear input field
            self.input_field.delete(0, "end")

            # Run mod_in.py script
            try:
                mod_in_cmd = ["python3", "/home/thevinduk/Repositories/TKinter-Front-End/Scripts/mod_in.py", self.file_path , self.output_file_path]
                mod_in_result = subprocess.run(mod_in_cmd, capture_output=True, text=True)
                if mod_in_result.returncode != 0:
                    print(f"Error running mod_in.py: {mod_in_result.stderr}")
                    return
            except Exception as e:
                print(f"Failed to run mod_in.py: {str(e)}")
                return

            # Run nack1.py script
            try:
                # Virtual Channel
                nack1r_cmd = ["python3", "/home/thevinduk/Repositories/TKinter-Front-End/Scripts/Chat_Scripts/QPSK_text_tx_rx.py"]
                # nack1r_cmd = ["python3", "/home/thevinduk/Repositories/TKinter-Front-End/Scripts/Chat_Scripts/nack1.py"]
                nack1r_result = subprocess.run(nack1r_cmd, capture_output=True, text=True)
                if nack1r_result.returncode != 0:
                    print(f"Error running nack1r.py: {nack1r_result.stderr}")
                    return
            except Exception as e:
                print(f"Failed to run nack1r.py: {str(e)}")
                return

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
        # file_path = './TKinter/tkinter-frontend-app/src/scripts/received_chat.txt'

        received_file_path = "/home/thevinduk/Repositories/TKinter-Front-End/Chats/Received/Output.txt"
        mod_out_file_path = "/home/thevinduk/Repositories/TKinter-Front-End/Chats/Received/Processed_Output.txt"

        # if os.path.exists(file_path):
        #     with open(file_path, 'r', encoding='utf-8') as file:
        #         new_message = file.read().strip()

        #     # Display new message only if it is different from the last received message
        #     if new_message and new_message != self.last_received_message:
        #         self.last_received_message = new_message
        #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #         self.add_message_bubble(new_message, "left", timestamp)

        if os.path.exists(received_file_path):
            try:
                # Run modout.py script
                mod_out_cmd = ["python3", "/home/thevinduk/Repositories/TKinter-Front-End/Scripts/mod_out.py", received_file_path, mod_out_file_path]
                mod_out_result = subprocess.run(mod_out_cmd, capture_output=True, text=True)
                if mod_out_result.returncode != 0:
                    print(f"Error running modout.py: {mod_out_result.stderr}")
                    return

                # Read the output from modout.py
                with open(mod_out_file_path, "r") as file:
                    new_message = file.read()

                # Display new message only if it is different from the last received message
                if new_message and new_message != self.last_received_message:
                    self.last_received_message = new_message
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.add_message_bubble(new_message, "left", timestamp)

            except Exception as e:
                print(f"Failed to run modout.py: {str(e)}")

        # Refresh every 30 seconds
        self.after(30000, self.refresh_received_messages)


    
    # def refresh(self):
    #     received_file_path = "/home/thevinduk/Repositories/TKinter-Front-End/Chats/Received/Output.txt"
    #     mod_out_file_path = "/home/thevinduk/Repositories/TKinter-Front-End/Chats/Received/Processed_Output.txt"

    #     if os.path.exists(received_file_path):
    #         try:
    #             # Run modout.py script
    #             mod_out_cmd = ["python3", "/home/thevinduk/Repositories/TKinter-Front-End/Scripts/mod_out.py", received_file_path, mod_out_file_path]
    #             mod_out_result = subprocess.run(mod_out_cmd, capture_output=True, text=True)
    #             if mod_out_result.returncode != 0:
    #                 print(f"Error running modout.py: {mod_out_result.stderr}")
    #                 return

    #             # Read the output from modout.py
    #             with open(mod_out_file_path, "r") as file:
    #                 received_message = file.read()

    #             # Display received message in the chat display
    #             self.chat_display.configure(state="normal")
    #             self.chat_display.insert("end", f"Friend: {received_message}\n")
    #             self.chat_display.configure(state="disabled")

    #         except Exception as e:
    #             print(f"Failed to run modout.py: {str(e)}")
    #     else:
    #         print("No received file found to process.")
        

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

