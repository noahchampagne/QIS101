#!/usr/bin/env python3
"""aes_demo.py"""

import os

import aes


def main() -> None:
    # The secret key is 16 bytes long
    secret_key: bytes = os.urandom(16)
    print(f"Secret key = {bytearray(secret_key).hex()}\n")

    # iv = (Random) initialization vector which ensures
    # the same value encrypted multiple times, even with the
    # same secret key, will not always result in the same encrypted value
    iv: bytes = os.urandom(16)

    plaintext: bytes = b"Attack at dawn"
    print("plaintext ", end=" = ")
    print([f"0x{b:02x}" for b in bytearray(plaintext)], sep=", ")
    print(f"{plaintext.decode('ascii')}")
    print()

    ciphertext: bytes = aes.AES(secret_key).encrypt_ctr(plaintext, iv)  # type: ignore
    print("ciphertext", end=" = ")
    print([f"0x{b:02x}" for b in bytearray(ciphertext)], sep=", ")
    print()

    plaintext = aes.AES(secret_key).decrypt_ctr(ciphertext, iv)  # type: ignore
    print("plaintext ", end=" = ")
    print([f"0x{b:02x}" for b in bytearray(plaintext)], sep=", ")
    print(f"{plaintext.decode('ascii')}")


if __name__ == "__main__":
    main()
