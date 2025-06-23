#!/usr/bin/env python3
"""caesar_decrypt.py"""

from pathlib import Path

import numpy as np

file_name = "ciphertext2.txt"
output_name = "plaintext2.txt"

key_shift = 6

file_path = Path(__file__).parent / file_name
with open(file_path, "rb") as f_in:
    f_bytes = bytearray(f_in.read())

for i in np.arange(len(f_bytes)):
    f_bytes[i] = (f_bytes[i] + key_shift) % 256

decoded_text = f_bytes.decode("utf-8", "ignore")
print(decoded_text)


output_path = Path(__file__).parent / output_name
with open(output_path, "w") as f_out:
    f_out.write(decoded_text)

