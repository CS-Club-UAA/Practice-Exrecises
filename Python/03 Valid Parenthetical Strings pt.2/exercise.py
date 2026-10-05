"""
Exercise 03: Valid Parenthetical Strings pt.2

Determine if a given string has properly paired brackets. See
README.md for the full problem statement.
"""


def has_valid_brackets(s: str) -> bool:
    # TODO: your code here
    pass


# ---------------------------------------------------------------------
# Tests: run `python exercise.py` to check your answer.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    tests: List[Tuple[str, bool]] = [
        # old tests
        ("()(())()((()()(())))", True),
        ("(boo!)", True),
        ("((still)a(valid))string()", True),
        (")Woah! What's that?(", False),
        (">:(", False),
        ("", True),

        # new tests
        ("[]<>()", True),
        ("[({{}})<([])>]", True),
        ("<{you}can>[still, have, (text)here]", True),
        ("[(])", False),
        ("[)<](>", False),
    ]

    passed: int = 0
    for given, expected in tests:
        result: bool = has_valid_brackets(given)
        if result == expected:
            passed += 1
        else:
            print(f"FAIL: has_valid_brackets({given!r}) returned {result!r}, expected {expected!r}")

    if passed == len(tests):
        print("All tests passed!")
    else:
        print(f"{passed}/{len(tests)} tests passed.")
