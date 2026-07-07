import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

from ui.styles import *
from core.image_loader import ImageLoader
from core.image_analyzer import ImageAnalyzer
from utils.helpers import get_file_size


class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("PixelCrypt Pro")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(fg_color=COLORS["bg"])

        self.selected_image_path = None

        # ==========================
        # Sidebar
        # ==========================
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            fg_color=COLORS["sidebar"]
        )
        self.sidebar.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self.sidebar,
            text="🔐 PixelCrypt",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        self.btn_select = ctk.CTkButton(
            self.sidebar,
            text="📂 Select Image",
            command=self.select_image
        )
        self.btn_select.pack(pady=10, padx=20)

        self.btn_analyze = ctk.CTkButton(
            self.sidebar,
            text="📊 Analyze"
        )
        self.btn_analyze.pack(pady=10, padx=20)

        self.btn_encrypt = ctk.CTkButton(
            self.sidebar,
            text="🔒 Encrypt"
        )
        self.btn_encrypt.pack(pady=10, padx=20)

        self.btn_decrypt = ctk.CTkButton(
            self.sidebar,
            text="🔓 Decrypt"
        )
        self.btn_decrypt.pack(pady=10, padx=20)

        # ==========================
        # Main Area
        # ==========================
        self.main = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg"]
        )
        self.main.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        header = ctk.CTkLabel(
            self.main,
            text="PixelCrypt Pro Dashboard",
            font=("Arial", 28, "bold")
        )
        header.pack(pady=10)

        # ==========================
        # Preview Frame
        # ==========================
        self.preview_frame = ctk.CTkFrame(
            self.main,
            width=550,
            height=400,
            fg_color=COLORS["card"]
        )
        self.preview_frame.pack(pady=20)

        self.preview_label = ctk.CTkLabel(
            self.preview_frame,
            text="No Image Selected",
            font=("Arial", 18)
        )
        self.preview_label.pack(expand=True)

        # ==========================
        # Image Information
        # ==========================
        self.info_label = ctk.CTkLabel(
            self.main,
            text="Width : -\nHeight : -\nChannels : -\nSize : -",
            justify="left",
            font=("Arial", 16)
        )
        self.info_label.pack(pady=10)

        # ==========================
        # Status Bar
        # ==========================
        self.status = ctk.CTkLabel(
            self.main,
            text="🟢 Status : Ready",
            font=("Arial", 16)
        )
        self.status.pack(side="bottom", pady=20)

    # =====================================
    # Select Image
    # =====================================

    def select_image(self):

        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp")
            ]
        )

        if not file_path:
            return

        self.selected_image_path = file_path

        # Preview Image
        image = Image.open(file_path)
        image.thumbnail((500, 350))

        photo = ImageTk.PhotoImage(image)

        self.preview_label.configure(
            image=photo,
            text=""
        )

        self.preview_label.image = photo

        # Backend Integration
        loader = ImageLoader(file_path)
        loader.load_image()

        info = loader.get_image_info()

        analyzer = ImageAnalyzer(file_path)
        analyzer.analyze()

        file_size = get_file_size(file_path)

        self.info_label.configure(
            text=(
                f"Width    : {info['Width']}\n"
                f"Height   : {info['Height']}\n"
                f"Channels : {info['Channels']}\n"
                f"Size     : {file_size} KB"
            )
        )

        self.status.configure(
            text="🟢 Image Loaded & Analyzed"
        )