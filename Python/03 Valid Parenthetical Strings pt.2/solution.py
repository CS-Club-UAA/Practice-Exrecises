"""
Exercise 03: Valid Parenthetical Strings pt.2

Determine if a given string has properly paired brackets. See
README.md for the full problem statement.
"""

# This is not necessary, but makes our code nicer to work with
# We know that the bracket stack can ONLY contain these specific
# values, rather than possibly holding any character ever if we
# make a mistake.
from enum import Enum
class Bracket(Enum):
    PARENTHESIS = 0
    SQUARE = 1
    CURLY = 2
    ANGLE = 3

def has_valid_brackets(s: str) -> bool:
    """
    The logic behind this algorithm is largely the same as the previous, except we use a stack to handle the depth
    so we can carry information about what kind of bracket is used, and we exit if the kind of opening bracket doesn't
    match.
    """
    # We will impliment a Stack here with a Deque. A List is another good choice.
    bracket_stack: Deque[Bracket] = []
    for c in s:
        # If we encounter an opening bracket, we push it to the top of the stack
        if c == '(':
            bracket_stack.append(Bracket.PARENTHESIS)
        elif c == '[':
            bracket_stack.append(Bracket.SQUARE)
        elif c == '{':
            bracket_stack.append(Bracket.CURLY)
        elif c == '<':
            bracket_stack.append(Bracket.ANGLE)
        else:
            # Otherwise, check if the character is a closing bracket
            if ")]}>".find(c) > -1:
                # Check if the stack is out of items to pop
                if len(bracket_stack) == 0:
                    # If so, we have an unopened close bracket meaning the string is invalid
                    return False
                else:
                    # Otherwise, it's safe to pop the last item
                    last: Bracket = bracket_stack.pop()
                    # Depending on the bracket, check if the current character matches the closer for that bracket
                    # If it does, we can continue with the bracket pair properly closed
                    # Otherwise, we have a mismatch, and should exit immediately
                    match last:
                        case Bracket.PARENTHESIS:
                            if c != ')':
                                return False
                        case Bracket.SQUARE:
                            if c != ']':
                                return False
                        case Bracket.CURLY:
                            if c != '}':
                                return False
                        case Bracket.ANGLE:
                            if c != '>':
                                return False
        # If it isn't a bracket at all, we can ignore it
    # At this point, if all is good, there should be no more unclosed bracket pairs
    # If not, we have an invalid string
    # Again, this can be simplified easily, but I'll write an if to be explicit
    if len(bracket_stack) == 0:
        return True
    else:
        return False


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
