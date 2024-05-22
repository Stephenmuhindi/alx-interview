#!/usr/bin/python3
"""
Checks if a byte sequence represents valid UTF-8.
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
