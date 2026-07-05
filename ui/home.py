import customtkinter as ctk

from ui.styles import *
from ui.components import *


class HomeWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("PixelCrypt Pro v2.0")

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.configure(fg_color=COLORS["bg"])

        TitleLabel(
            self,
            "🔐 PixelCrypt Pro"
        ).pack(pady=25)

        PrimaryButton(
            self,
            "Select Image"
        ).pack(pady=10)

        PrimaryButton(
            self,
            "Analyze"
        ).pack(pady=10)

        PrimaryButton(
            self,
            "Encrypt"
        ).pack(pady=10)

        PrimaryButton(
            self,
            "Decrypt"
        ).pack(pady=10)