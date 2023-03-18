#!/usr/bin/env python3
"""rsa_demo.py"""


def extended_euclidean(a: int, b: int) -> tuple[int, int]:
    swapped: bool = False
    if a < b:
        a, b = b, a
        swapped = True
    ca: tuple[int, int] = (int(1), int(0))
    cb: tuple[int, int] = (int(0), int(1))
    while b != 0:
        k: int = int(a // b)
        # fmt: off
        a, b, ca, cb = ( # type: ignore
             b, a - b * k,
            (cb), (ca[0] - k * cb[0], ca[1] - k * cb[1]))
        # fmt: on
    if swapped:
        return ca[1], ca[0]  # type: ignore
    else:
        return ca  # type: ignore


def power_modulus(b: int, e: int, n: int) -> int:
    r: int = 1
    for i in range(e.bit_length(), -1, -1):
        r = (r * r) % n
        if (e >> i) & 1:
            r = (r * b) % n
    return r


def generate_keys(p: int, q: int) -> dict[str, tuple[int, int]]:
    n: int = p * q
    totient: int = (p - 1) * (q - 1)
    # e = public encryption exponent (a prime number)
    e: int = 35537
    # d = private encryption exponent
    d: int = extended_euclidean(e, totient)[0]
    if d < 0:
        d += totient
    return {"priv": (d, n), "pub": (e, n)}


def encrypt(m: int, public_key: tuple[int, int]) -> int:
    e: int = public_key[0]
    n: int = public_key[1]
    return power_modulus(m, e, n)


def decrypt(m: int, private_key: tuple[int, int]) -> int:
    d: int = private_key[0]
    n: int = private_key[1]
    return power_modulus(m, d, n)


def main() -> None:
    # Pick two prime numbers
    p: int = 31337
    q: int = 31357

    keys: dict[str, tuple[int, int]] = generate_keys(p, q)
    print(f"RSA Encryption Keys: {keys}")

    private_key: tuple[int, int] = keys["priv"]
    public_key: tuple[int, int] = keys["pub"]

    plaintext: str = "Hi!"
    print(f"Plaintext = {plaintext}")

    b: bytearray = bytearray(plaintext, encoding="utf-8")
    plaintext_int: int = int.from_bytes(b, "big")
    print(f"Plaintext as Integer = {plaintext_int}")

    ciphertext_int: int = encrypt(plaintext_int, private_key)
    print(f"Ciphertext as Integer = {ciphertext_int}")

    plaintext_int = decrypt(ciphertext_int, public_key)
    print(f"Plaintext as Integer = {plaintext_int}")

    b = bytearray(plaintext_int.to_bytes(3, "big"))
    plaintext = b.decode(encoding="utf-8")
    print(f"Plaintext = {plaintext}")


if __name__ == "__main__":
    main()
