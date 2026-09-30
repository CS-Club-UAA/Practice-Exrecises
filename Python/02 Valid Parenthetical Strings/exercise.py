"""
Exercise 02: Valid Parenthetical Strings

Determine if a given string has properly paired parentheses. See
README.md for the full problem statement.
"""


def has_valid_parens(s: str) -> bool:
    # TODO: your code here
    pass


# ---------------------------------------------------------------------
# Tests: run `python exercise.py` to check your answer.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    tests: List[Tuple[str, bool]] = [
        ("()(())()((()()(())))", True),
        ("(boo!)", True),
        ("((still)a(valid))string()", True),
        (")Woah! What's that?(", False),
        (">:(", False),
        ("", True),
    ]

    passed: int = 0
    for given, expected in tests:
        result: bool = has_valid_parens(given)
        if result == expected:
            passed += 1
        else:
            print(f"FAIL: has_valid_parens({given!r}) returned {result!r}, expected {expected!r}")

    if passed == len(tests):
        print("All tests passed!")
    else:
        print(f"{passed}/{len(tests)} tests passed.")
