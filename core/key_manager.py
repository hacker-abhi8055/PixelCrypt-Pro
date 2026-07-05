"""
--------------------------------------------
PixelCrypt Pro

Key Manager

Author : Abhishek Biradar
Version : 2.0
--------------------------------------------
"""

import secrets


class KeyManager:
    """
    Generate and manage encryption keys.
    """

    @staticmethod
    def generate_key(length: int = 32) -> str:
        """
        Generate a random hexadecimal key.

        Args:
            length: Number of random bytes.

        Returns:
            Hexadecimal key string.
        """
        return secrets.token_hex(length)