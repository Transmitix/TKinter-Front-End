import customtkinter as ctk

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
        self.send_button = ctk.CTkButton(self, text="Connect", command=self.loading)
        self.send_button.grid(row=0, column=1, padx=10, pady=10)

        # Chat display area
        self.chat_display = ctk.CTkTextbox(self, width=500, height=400, state="disabled")
        self.chat_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Input field
        self.input_field = ctk.CTkEntry(self, width=400, placeholder_text="Type your message here...")
        self.input_field.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Send button
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, padx=10, pady=10)

    def send_message(self):
        message = self.input_field.get()
        if message:
            # Display message in the chat display
            self.chat_display.configure(state="normal")
            self.chat_display.insert("end", f"You: {message}\n")
            self.chat_display.configure(state="disabled")
            
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

    def loading(self):
        # add loading animation or 
        # start running reciever code
        pass
