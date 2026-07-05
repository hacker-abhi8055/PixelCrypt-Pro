"""
-------------------------------------------------
PixelCrypt Pro

Hash Manager

Author : Abhishek Biradar

Version : 2.0
-------------------------------------------------
"""

import hashlib


class HashManager:
    """
    Handles SHA-256 hashing operations.
    """

    @staticmethod
    def generate(file_path: str) -> str:
        """
        Generate SHA-256 hash for a file.
        """

        sha = hashlib.sha256()

        with open(file_path, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()
        