#!/usr/bin/env python3
# std_continued_fractions.py

import math

MAX_TERMS = 20


def normalize_cf(cf):
    if len(cf) > 2:
        if cf[-1] == 1 and cf[-2] != 1:
            cf[-2] += 1
            cf.pop(-1)
    return cf


def encode_cf(x):
    cf = []
    while len(cf) < MAX_TERMS:
        cf.append(math.floor(x))
        x = x - math.floor(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


def decode_cf(cf):
    hn, kn = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in cf:
        an, bn = term, 1
        hn = an * h_1 + b_1 * h_2
        kn = an * k_1 + b_1 * k_2
        b_1 = bn
        h_1, h_2 = hn, h_1
        k_1, k_2 = kn, k_1
    return hn / kn


def eval_cf(x):
    cf = encode_cf(x)
    x2 = decode_cf(cf)
    print(f"{x} -> {cf} -> {x2}")


def main():
    eval_cf(3.245)
    eval_cf(math.sqrt(2))
    eval_cf(math.sqrt(113))

    golden_ratio = (1 + math.sqrt(5)) / 2
    eval_cf(golden_ratio)


if __name__ == "__main__":
    main()
