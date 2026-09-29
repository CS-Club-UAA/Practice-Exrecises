"""
Exercise 01: Run-Length Encoding (reference solution)
"""

from itertools import groupby


def encode(s: str) -> str:
    """Loop-based solution: walk the string and count each run."""
    if not s:
        return ""

    result = []
    current = s[0]
    count = 1

    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            result.append(f"{current}{count}")
            current = ch
            count = 1

    result.append(f"{current}{count}")  # don't forget the final run
    return "".join(result)


def encode_groupby(s: str) -> str:
    """One-liner alternative using itertools.groupby."""
    return "".join(f"{ch}{len(list(run))}" for ch, run in groupby(s))


def decode(s: str) -> str:
    """Bonus: reverse the encoding, handling multi-digit counts."""
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        digits = ""
        while i < len(s) and s[i].isdigit():
            digits += s[i]
            i += 1
        result.append(ch * int(digits))
    return "".join(result)


if __name__ == "__main__":
    tests = [
        ("aaabbc", "a3b2c1"),
        ("abc", "a1b1c1"),
        ("zzzzzzzzzzzz", "z12"),
        ("aAAa", "a1A2a1"),
        ("", ""),
        ("x", "x1"),
    ]

    for given, expected in tests:
        assert encode(given) == expected, (given, encode(given))
        assert encode_groupby(given) == expected, (given, encode_groupby(given))
        assert decode(expected) == given, (expected, decode(expected))

    print("All tests passed!")
