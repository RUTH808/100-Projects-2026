import customtkinter as ctk


class StatisticsPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Image Statistics",
            font=("Arial", 16, "bold")
        )

        title.pack(
            pady=10
        )

        self.labels = {}

        fields = [

            "Width",
            "Height",
            "Channels",

            "Mean",
            "Std Dev",

            "Min",
            "Max"
        ]

        for field in fields:

            lbl = ctk.CTkLabel(
                self,
                text=f"{field}: -"
            )

            lbl.pack(
                anchor="w",
                padx=10,
                pady=3
            )

            self.labels[field] = lbl

    def update_stats(
        self,
        stats
    ):

        for key, value in stats.items():

            if key in self.labels:

                self.labels[key].configure(
                    text=f"{key}: {value}"
                )