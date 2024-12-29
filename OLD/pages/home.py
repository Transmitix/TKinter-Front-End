import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="Home Page")
        label.pack(side="top", fill="x", pady=10)
        button1 = ctk.CTkButton(self, text="Go to File Transmission",
                                command=lambda: controller.show_frame("FileTransmissionPage"))
        button1.pack()
        button2 = ctk.CTkButton(self, text="Go to Messaging",
                                command=lambda: controller.show_frame("MessagingPage"))
        button2.pack()
        button3 = ctk.CTkButton(self, text="Go to File Receiver",
                                command=lambda: controller.show_frame("FileReceiverPage"))
        button3.pack()