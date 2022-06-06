#!/usr/bin/env python3
# caesar_decrypt.py

import sys


def main(file_name, key_shift):
    with open(file_name, "rb") as f_in:
        f_bytes = bytearray(f_in.read())

        for i in range(0, len(f_bytes)):
            f_bytes[i] = (f_bytes[i] + key_shift) % 256

        print(f_bytes.decode())


if __name__ == "__main__":
    file_name = None
    if len(sys.argv) == 1:
        print("You must provide a filename and a key value")
    else:
        file_name = sys.argv[1]
        key_shift = int(sys.argv[2])
        main(file_name, key_shift)
