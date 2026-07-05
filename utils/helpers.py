"""
Utility Helper Functions
"""

import os


def file_exists(path: str) -> bool:
    return os.path.exists(path)


def get_file_size(path: str) -> float:
    return round(os.path.getsize(path) / 1024, 2)