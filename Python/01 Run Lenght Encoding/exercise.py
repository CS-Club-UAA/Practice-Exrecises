"""
Exercise 01: Run-Length Encoding

Replace each run of repeated characters with the character followed by
its count. See README.md for the full problem statement.
"""


def encode(s: str) -> str:
    # TODO: your code here
    pass


# ---------------------------------------------------------------------
# Tests: run `python exercise.py` to check your answer.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    tests = [
        ("aaabbc", "a3b2c1"),
        ("abc", "a1b1c1"),
        ("zzzzzzzzzzzz", "z12"),
        ("aAAa", "a1A2a1"),
        ("", ""),
        ("x", "x1"),
    ]

    passed = 0
    for given, expected in tests:
        result = encode(given)
        if result == expected:
            passed += 1
        else:
            print(f"FAIL: encode({given!r}) returned {result!r}, expected {expected!r}")

    if passed == len(tests):
        print("All tests passed!")
    else:
        print(f"{passed}/{len(tests)} tests passed.")
