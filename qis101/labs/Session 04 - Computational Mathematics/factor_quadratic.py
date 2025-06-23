#!/usr/bin/env python3
"""factor_quadratic.py  –  factor J x² + K x + L over the integers.

• prints the GCD if one exists
• gives integer factors when possible
• otherwise shows the quadratic-formula roots
"""

import math
from typing import Optional, Tuple


# -------------------------------------------------------------------- helpers
def gcd3(a: int, b: int, c: int) -> int:
    """Greatest common divisor of three integers."""
    return math.gcd(a, math.gcd(b, c))


def nice_quad(a: int, b: int, c: int) -> str:
    """Pretty string for ax²+bx+c."""
    def part(coeff: int, tail: str = "") -> str:
        if coeff == 0:
            return ""
        sign = "+" if coeff > 0 else "−"
        coeff_abs = abs(coeff)
        if tail and coeff_abs == 1:
            body = tail
        else:
            body = f"{coeff_abs}{tail}"
        return f" {sign} {body}"

    first = "x²" if a == 1 else "−x²" if a == -1 else f"{a}x²"
    return (first + part(b, "x") + part(c)).strip().lstrip("+")


def is_square(n: int) -> Tuple[bool, int]:
    """Return (True, √n) if n is a perfect square else (False, –1)."""
    if n < 0:
        return False, -1
    r = math.isqrt(n)
    return r * r == n, r


def _factor_integer(a: int, b: int, c: int
                    ) -> Optional[Tuple[int, int, int, int, int]]:
    """Return (scale, p, q, r, t) such that ax²+bx+c = scale(p x+q)(r x+t)."""
    disc = b * b - 4 * a * c
    ok, root = is_square(disc)
    if not ok:
        return None  # irrational roots ⇒ no integer factorisation

    # two (possibly rational) roots
    num1, num2, den = -b + root, -b - root, 2 * a

    def reduce(num: int, den_: int) -> Tuple[int, int]:
        g = math.gcd(num, den_)
        num //= g
        den_ //= g
        if den_ < 0:       # keep denominator positive
            num, den_ = -num, -den_
        return num, den_

    n1, d1 = reduce(num1, den)
    n2, d2 = reduce(num2, den)

    p, q = d1, -n1          # (d x − n) pattern
    r, t = d2, -n2
    if (p * r) == 0:
        return None

    scale = a // (p * r)
    if scale * p * r != a:   # not an exact integer match
        return None

    return scale, p, q, r, t


# ----------------------------------------------------------------- main API
def factor_quadratic(j: int, k: int, l: int, show_roots: bool = False) -> None:
    """Print a factorisation (or roots) for Jx²+Kx+L."""
    print("Quadratic :", nice_quad(j, k, l))

    g = gcd3(j, k, l)
    if g != 1:
        print("GCD       :", g)

    a, b, c = j // g, k // g, l // g
    res = _factor_integer(a, b, c)

    if res is None:
        print("Factor    : irreducible over ℤ")
        if show_roots:
            disc = b * b - 4 * a * c
            root_d = math.sqrt(disc)
            r1 = (-b + root_d) / (2 * a)
            r2 = (-b - root_d) / (2 * a)
            print(f"Roots     : {r1:.6g}, {r2:.6g}")
    else:
        s, p, q, r, t = res
        front = "" if g * s == 1 else f"{g * s}"
        f1 = f"({p}x {'+' if q >= 0 else '-'} {abs(q)})"
        f2 = f"({r}x {'+' if t >= 0 else '-'} {abs(t)})"
        print("Factor    :", f"{front}{f1}{f2}")
    print()  # blank line between cases


# -------------------------------------------------------------------- demos
def main() -> None:
    # 1. The big one from your slide (irreducible; show its roots)
    factor_quadratic(115_425, 3_254_121, 379_021, show_roots=True)

    # 2. A negative-coefficient example:  −2x² + 7x − 3 = −(2x − 1)(x − 3)
    factor_quadratic(-2, 7, -3, show_roots=True)
    
    factor_quadratic(1, 0, 1)

    # A simple, nicely factorable quadratic
    factor_quadratic(2, 7, 3)


if __name__ == "__main__":
    main()
