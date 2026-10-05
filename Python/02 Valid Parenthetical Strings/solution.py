"""
Exercise 02: Valid Parenthetical String

Determine if a given string has properly paired parentheses. See
README.md for the full problem statement.
"""


def has_valid_parens(s: str) -> bool:
    """
    We can keep track of parenthetical "depth" here--
    In the string (()()):
        We start at depth 0
        ( - increment depth, now at 1
        ( - increment depth, now at 2
        ) - decrement depth, now at 1
        ( - increment depth, now at 2
        ) - decrement depth, now at 1
        ) - decrement depth, now at 0
    In a valid parenthetical string, depth will ALWAYS return to zero
    by the end. If it's not at zero, our string is invalid.
    In the string (():
        We start at depth 0
        ( - increment depth, now at 1
        ( - increment depth, now at 2
        ) - decrement depth, now at 1
    |!| Warning: Depth not equal to zero! |!|
    There's one more edge case to watch out for- If we start with a
    closing parenthesis, our depth is brought below zero. In fact, if
    at ANY point we encounter a depth below zero, we should return
    immediately as the string is invalid
    ())(
        We start at depth 0
        ( - increment depth, now at 1
        ) - decrement depth, now at 0
        ) - decrement depth, now at -1
    |!| Warning: Depth fell below zero! |!|
    So, let's impliment this in code
    """

    # Type hints aren't strictly necessary in Python, however,
    # they make your code more readable and are good practice
    # for languages where type hints are required
    depth: int = 0
    for c in s:
        if c == '(':
            depth += 1
        elif c == ')':
             depth -= 1
             if depth < 0:
                 # |!| Warning: Depth fell below zero! |!|
                 return False
        # If the character is anything else, we don't really care, we can skip it
    if depth == 0:
        # All is good, the string is valid
        return True
    else:
        # |!| Warning: Depth not equal to zero! |!|
        return False
    # The above lines can be simplified to `return depth == 0`, but I
    # wrote it out explicitly here for the sake of calrity



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
