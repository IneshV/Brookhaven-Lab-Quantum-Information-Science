#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""


def main() -> None:
    for celsius in range(-44, 105, 4):
        fahrenheit: float = celsius * 9 / 5 + 32
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")


if __name__ == "__main__":
    main()
