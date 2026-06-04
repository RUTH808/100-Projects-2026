import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.pack(
            fill="x",
            padx=10,
            pady=10
        )

        title = ctk.CTkLabel(
            self,
            text="OpenCV Image Studio",
            font=("Arial", 28, "bold")
        )

        title.pack()

        subtitle = ctk.CTkLabel(
            self,
            text="App used by Ruth to edit Cat photos 🐱",
            font=("Arial", 12)
        )

        subtitle.pack()