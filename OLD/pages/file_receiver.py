import customtkinter as ctk

class FileReceiverPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = ctk.CTkLabel(self, text="File Receiver Page")
        label.pack(side="top", fill="x", pady=10)
        button1 = ctk.CTkButton(self, text="Go to Home",
                                command=lambda: controller.show_frame("HomePage"))
        button1.pack()
        button2 = ctk.CTkButton(self, text="Go to File Transmission",
                                command=lambda: controller.show_frame("FileTransmissionPage"))
        button2.pack()
        button3 = ctk.CTkButton(self, text="Go to Messaging",
                                command=lambda: controller.show_frame("MessagingPage"))
        button3.pack()