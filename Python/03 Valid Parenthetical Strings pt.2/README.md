# 03 · Valid Parenthetical Strings pt. 2

**Difficulty:** Medium **Topics:** strings, loops, data structures

## Problem

This is an extention of 02 Valid Parenthetical Strings. If you have not done that one yet, do it first.

Parentheses are not the only symbols you'll want to match. This problem extends the previous to additionally account for [], {},
and <> (square brackets, curly brackets, and angle brackets respectively).

Write a function `has_valid_brackets(s: str) -> bool` that determines if an inputted string is valid.

- Unclosed or unopened brackets make a string invalid
- An empty string is always considered to be valid
- Nonparentheses characters may be present in the string
- Brackets must be closed with a matching bracket of their type.

## Examples

All examples from the previous exercise have the same outputs. Additionally:

| Input                                   | Output  |
|-----------------------------------------|---------|
| `"[]<>()"`                              | `True`  |
| `"[({{}})<([])>]"`                      | `True`  |
| `"<{you}can>[still, have, (text)here]"` | `True`  |
| `"[(])"`                                | `False` |
| `"[)<](>"`                              | `False` |

## How to run

Open `exercise.py`, fill in the `has_valid_brackets` function, then run:

```bash
python exercise.py
```

If every test passes you'll see `All tests passed!`

## Hint

If you are having trouble, check out [`HINT.md`](HINT.md).

## Solution

Try it yourself first! The reference solution is in [`solution.py`](solution.py).
