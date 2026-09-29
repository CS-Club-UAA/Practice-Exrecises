# 01 · Run-Length Encoding

**Difficulty:** Easy  **Time:** ~5 minutes  **Topics:** strings, loops

## Problem

Run-length encoding (RLE) is a simple compression technique that replaces runs of repeated characters with the character followed by how many times it repeats.

Write a function `encode(s: str) -> str` that returns the run-length encoding of `s`.

- Each run is written as the **character followed by its count**, even when the count is 1.
- Runs are case-sensitive (`"a"` and `"A"` are different characters).
- An empty string encodes to an empty string.

## Examples

| Input | Output |
|---|---|
| `"aaabbc"` | `"a3b2c1"` |
| `"abc"` | `"a1b1c1"` |
| `"zzzzzzzzzzzz"` | `"z12"` |
| `"aAAa"` | `"a1A2a1"` |
| `""` | `""` |

## How to run

Open `exercise.py`, fill in the `encode` function, then run:

```bash
python exercise.py
```

If every test passes you'll see `All tests passed!`

## Bonus (if you finish early)

Write the reverse: `decode("a3b2c1")` should return `"aaabbc"`. Watch out for counts with more than one digit, like `"z12"`.

## Solution

Try it yourself first! The reference solution is in [`solution.py`](solution.py).
