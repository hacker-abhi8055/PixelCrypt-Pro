import customtkinter as ctk
from ui.styles import *

class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("PixelCrypt Pro")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(fg_color=COLORS["bg"])

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220, fg_color=COLORS["sidebar"])
        self.sidebar.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self.sidebar,
            text="🔐 PixelCrypt",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        ctk.CTkButton(self.sidebar, text="📂 Select Image").pack(pady=10, padx=20)
        ctk.CTkButton(self.sidebar, text="📊 Analyze").pack(pady=10, padx=20)
        ctk.CTkButton(self.sidebar, text="🔒 Encrypt").pack(pady=10, padx=20)
        ctk.CTkButton(self.sidebar, text="🔓 Decrypt").pack(pady=10, padx=20)

        # Main Area
        self.main = ctk.CTkFrame(self, fg_color=COLORS["bg"])
        self.main.pack(side="left", fill="both", expand=True)

        header = ctk.CTkLabel(
            self.main,
            text="PixelCrypt Pro Dashboard",
            font=("Arial", 28, "bold")
        )
        header.pack(pady=20)

        self.status = ctk.CTkLabel(
            self.main,
            text="🟢 Status: Ready",
            font=("Arial", 16)
        )
        self.status.pack(side="bottom", pady=20)