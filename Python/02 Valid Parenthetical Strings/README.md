# 02 · Valid Parenthetical Strings

**Difficulty:** Easy **Topics:** strings, loops

## Problem

Parentheses come in open-close pairs. A parenthetical string is considered to be valid if all parentheses in the string can be put into pairs.

Write a function `has_valid_parens(s: str) -> bool` that determines if an inputted string is valid.

- Unclosed or unopened parentheses make a string invalid
- An empty string is always considered to be valid
- Nonparentheses characters may be present in the string
- 
## Examples

| Input                         | Output  |
|-------------------------------|---------|
| `"()(())()((()()(())))"`      | `True`  |
| `"(boo!)"`                    | `True`  |
| `"((still)a(valid))string()"` | `True`  |
| `")Woah! What's that?("`      | `False` |
| `">:("`                       | `False` |
| `""`                          | `True`  |

## How to run

Open `exercise.py`, fill in the `has_valid_parens` function, then run:

```bash
python exercise.py
```

If every test passes you'll see `All tests passed!`

## Solution

Try it yourself first! The reference solution is in [`solution.py`](solution.py).
