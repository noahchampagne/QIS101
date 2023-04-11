#!/usr/bin/env python3
"""caesar_decrypt.py"""

import sys
from pathlib import Path


def main(data_file: Path, key_shift: int) -> None:
    with open(data_file, "rb") as f_in:
        f_bytes: bytearray = bytearray(f_in.read())

        for i in range(0, len(f_bytes)):
            f_bytes[i] = (f_bytes[i] + key_shift) % 256

        print(f_bytes.decode())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You must provide a filename AND a key value")
    else:
        key_shift: int = int(sys.argv[2])
        main(Path(sys.argv[1]), key_shift)
