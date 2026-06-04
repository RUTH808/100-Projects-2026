import customtkinter as ctk


class ParameterPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent)

        self.sliders = {}

        title = ctk.CTkLabel(
            self,
            text="Parameters",
            font=("Arial", 16, "bold")
        )

        title.pack(
            pady=10
        )

    def clear(self):

        widgets = self.winfo_children()

        for widget in widgets[1:]:

            widget.destroy()

        self.sliders.clear()

    def build(self, params):

        self.clear()

        for name, config in params.items():

            label = ctk.CTkLabel(
                self,
                text=name
            )

            label.pack(
                pady=(10, 0)
            )

            slider = ctk.CTkSlider(
                self,
                from_=config["min"],
                to=config["max"]
            )

            slider.set(
                config["default"]
            )

            slider.pack(
                fill="x",
                padx=10
            )

            value_label = ctk.CTkLabel(
                self,
                text=str(
                    config["default"]
                )
            )

            value_label.pack()

            slider.configure(
                command=lambda v,
                lbl=value_label:
                lbl.configure(
                    text=f"{v:.1f}"
                )
            )

            self.sliders[name] = slider

    def get_values(self):

        values = {}

        for name, slider in self.sliders.items():

            values[name] = slider.get()

        return values