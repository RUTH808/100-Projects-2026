import customtkinter as ctk
import tkinter as tk


class PipelinePanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Pipeline Editor",
            font=("Arial", 16, "bold")
        )

        title.pack(
            pady=10
        )

        self.listbox = tk.Listbox(
            self,
            height=12,
            selectmode=tk.SINGLE
        )

        self.listbox.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def refresh(
        self,
        pipeline
    ):

        self.listbox.delete(
            0,
            tk.END
        )

        for index, step in enumerate(
            pipeline
        ):

            self.listbox.insert(
                tk.END,
                f"{index}: {step['plugin']}"
            )

    def get_selected_index(self):

        selection = (
            self.listbox.curselection()
        )

        if not selection:
            return None

        return selection[0]