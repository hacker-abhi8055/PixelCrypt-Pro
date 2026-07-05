import customtkinter as ctk


class TitleLabel(ctk.CTkLabel):

    def __init__(self, master, text):

        super().__init__(
            master,
            text=text,
            font=("Orbitron", 28, "bold")
        )


class PrimaryButton(ctk.CTkButton):

    def __init__(self, master, text, command=None):

        super().__init__(
            master,
            text=text,
            command=command,
            width=180,
            height=45,
            corner_radius=10
        )