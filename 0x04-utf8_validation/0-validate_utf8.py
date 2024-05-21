#!/usr/bin/python3
"""
Checks if a byte sequence represents valid UTF-8 encoding (variable length).

Iterates through bytes, validates starting bits for character length
(1, 2, 3, or 4 bytes)
and checks continuation bytes (must start with 10).
Returns True if all bytes are valid and
continuation count reaches zero at the end
(complete character sequence), False otherwise.
"""


def validUTF8(data):
    """
    Checks UTF-8 validity of data (list of 1-byte integers).
    """
    expected_continuations = 0
    for byte in data:
        if expected_continuations == 0:
            if (byte >> 5) == 0b110:
                expected_continuations = 1
            elif (byte >> 4) == 0b1110:
                expected_continuations = 2
            elif (byte >> 3) == 0b11110:
                expected_continuations = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_continuations -= 1
    return expected_continuations == 0
