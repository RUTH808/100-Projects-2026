import customtkinter as ctk


class HistoryPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Operation History",
            font=("Arial", 16, "bold")
        )

        title.pack(
            pady=10
        )

        self.textbox = ctk.CTkTextbox(
            self,
            width=300,
            height=250
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def refresh(
        self,
        logs
    ):

        self.textbox.delete(
            "1.0",
            "end"
        )

        for item in logs:

            self.textbox.insert(
                "end",
                f"{item}\n"
            )