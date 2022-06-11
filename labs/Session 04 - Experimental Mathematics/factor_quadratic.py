#!/usr/bin/env python3
# factor_quadratic.py


def factor_quadratic(J, K, L):
    print("Given the quadratic:", end=" ")
    print(f"{J}x^2 + {K}x + {L}")

    for a in range(1, J + 1):
        if J % a == 0:
            c = J // a
            for b in range(1, L + 1):
                if L % b == 0:
                    d = L // b
                    if a * d + b * c == K:
                        print("The factors are:", end=" ")
                        print(f"({a}x + {b})" f"({c}x + {d})")


def main():
    factor_quadratic(115425, 3254121, 379020)


if __name__ == "__main__":
    main()
