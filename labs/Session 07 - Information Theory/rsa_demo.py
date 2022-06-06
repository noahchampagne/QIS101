#!/usr/bin/env python3
# rsa_demo.py

import numpy as np


def extended_euclidean(a, b):
    swapped = False
    if a < b:
        a, b = b, a
        swapped = True
    ca = (1, 0)
    cb = (0, 1)
    while b != 0:
        k = a // b
        a, b, ca, cb = b, a - b * k, cb, (ca[0] - k * cb[0], ca[1] - k * cb[1])
    if swapped:
        return (ca[1], ca[0])
    else:
        return ca


def power_modulus(b, e, n):
    r = 1
    for i in range(e.bit_length(), -1, -1):
        r = (r * r) % n
        if (e >> i) & 1:
            r = (r * b) % n
    return r


def generate_keys(p, q):
    n = p * q
    totient = (p - 1) * (q - 1)
    # e = public encryption exponent (a prime number)
    e = 35537
    # d = private encryption exponent
    d = extended_euclidean(e, totient)[0]
    if d < 0:
        d += totient
    return {"priv": (d, n), "pub": (e, n)}


def encrypt(m, public_key):
    e = public_key[0]
    n = public_key[1]
    return power_modulus(m, e, n)


def decrypt(m, private_key):
    d = private_key[0]
    n = private_key[1]
    return power_modulus(m, d, n)


def main():
    # Pick two prime numbers
    p = 31337
    q = 31357

    keys = generate_keys(p, q)
    print(f"RSA Encryption Keys: {keys}")

    private_key = keys["priv"]
    public_key = keys["pub"]

    plaintext = "Hi!"
    print(f"Plaintext = {plaintext}")

    b = bytearray(plaintext, encoding="utf-8")
    plaintext_int = int.from_bytes(b, "big")
    print(f"Plaintext as Integer = {plaintext_int}")

    ciphertext_int = encrypt(plaintext_int, private_key)
    print(f"Ciphertext as Integer = {ciphertext_int}")

    plaintext_int = decrypt(ciphertext_int, public_key)
    print(f"Plaintext as Integer = {plaintext_int}")

    b = plaintext_int.to_bytes(3, "big")
    plaintext = b.decode(encoding="utf-8")
    print(f"Plaintext = {plaintext}")


if __name__ == "__main__":
    main()
