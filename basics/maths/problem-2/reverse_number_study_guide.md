# Reverse a Number

---

## 1. Name of the Problem

**Reverse a Number**

A foundational digit-manipulation problem: given an integer `n`, reverse its digits and print the result.

---

## 2. Problem Statement

### What is being solved?

Given a non-negative integer `num`, reverse its digits and output the reversed number.

> **Notes:**
> - Leading zeros in the reversed result are dropped automatically (e.g., reversing `1200` gives `21`, not `0021`).
> - The original code handles only non-negative integers (the `while num > 0` loop won't execute for negatives or zero).
> - The refined code handles negatives and zero as well.

---

### Example Input / Output

| Input (`num`) | Expected Output | Explanation                         |
|---------------|-----------------|--------------------------------------|
| `12345`       | `54321`         | Digits reversed one by one           |
| `100`         | `1`             | Leading zeros dropped → `001` → `1`  |
| `0`           | `0`             | Zero reversed is still zero          |
| `-987`        | `-789`          | Sign preserved; digits reversed      |
| `7`           | `7`             | Single digit reversed is itself      |
| `1200`        | `21`            | Trailing zeros become leading zeros  |

---

## 3. Logic Behind the Solution

### Part A — Intuition: How to Think About It

Imagine you have the number `1234` written on paper. To reverse it:

- You pick up the **last digit** (`4`) and place it **first**
- Then pick up `3` and place it next
- Then `2`, then `1`
- Result: `4321`

In code, we extract the **last digit** using `num % 10` (the remainder when dividing by 10), then **attach it** to the growing reversed number using `reverse * 10 + digit`.

**Why `reverse * 10 + digit`?**

Each time we add a new digit, we shift all existing digits one place to the left (multiply by 10) to make room, then add the new digit at the ones place.

Example with `1234`:
```
Step 1: reverse = 0 * 10 + 4  =  4
Step 2: reverse = 4 * 10 + 3  = 43
Step 3: reverse = 43 * 10 + 2 = 432
Step 4: reverse = 432 * 10 + 1 = 4321
```

---

### Part B — Approaches

#### Approach 1: Brute Force (Loop-based Digit Extraction)

- Extract the last digit using `digit = num % 10`
- Build the reversed number digit by digit: `reverse = reverse * 10 + digit`
- Strip the last digit from `num`: `num = num // 10`
- Repeat until `num` becomes `0`

#### Approach 2: Optimized (String Conversion)

- Convert the number to a string
- Reverse the string using Python slicing `[::-1]`
- Convert back to integer (leading zeros are dropped automatically)
- Handle the negative sign separately

#### Edge Cases to Always Handle

| Edge Case              | Expected Behaviour                              |
|------------------------|-------------------------------------------------|
| `num = 0`              | Return `0`                                      |
| `num < 0`              | Reverse digits, preserve the negative sign      |
| Trailing zeros (e.g., `1200`) | Leading zeros drop automatically → `21` |
| Single digit           | Reversed number equals itself                   |

---

## 4. Pseudocode

### Brute Force (Loop-based)

```
FUNCTION reverse_number_brute(num):
    IF num == 0:
        RETURN 0

    is_negative ← (num < 0)
    num ← absolute value of num

    reverse ← 0

    WHILE num > 0:
        digit  ← num MOD 10          ← extract last digit
        reverse ← reverse * 10 + digit  ← append digit to result
        num ← num // 10              ← strip last digit

    IF is_negative:
        RETURN -reverse
    ELSE:
        RETURN reverse
```

### Optimized (String Slicing)

```
FUNCTION reverse_number_optimized(num):
    is_negative ← (num < 0)
    num_str ← string of absolute value of num

    reversed_str ← num_str reversed using slicing [::-1]

    result ← integer of reversed_str   ← leading zeros auto-dropped

    IF is_negative:
        RETURN -result
    ELSE:
        RETURN result
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Reverse a Number
  Approach : Brute Force (Loop) | Optimized (String Slicing)
  Author   : Study Guide Generator
=============================================================
"""


# ─────────────────────────────────────────────
#  APPROACH 1 — Brute Force (Loop-based)
# ─────────────────────────────────────────────

def reverse_number_brute(num: int) -> int:
    """
    Reverse the digits of an integer using a loop and integer division.

    Algorithm:
        1. Extract the last digit with num % 10.
        2. Append it to the reversed number: reverse = reverse * 10 + digit.
        3. Strip the last digit: num = num // 10.
        4. Repeat until num == 0.

    Args:
        num (int): Any integer (positive, negative, or zero).

    Returns:
        int: The digit-reversed integer.

    Time  : O(d) — d = number of digits
    Space : O(1) — only scalar variables used
    """
    # Edge case: zero reversed is zero
    if num == 0:
        return 0

    # Remember and remove the sign
    is_negative = num < 0
    num = abs(num)

    reverse = 0
    while num > 0:
        digit = num % 10               # extract the rightmost digit
        reverse = reverse * 10 + digit # shift left and append digit
        num = num // 10                # drop the rightmost digit

    # Restore negative sign if needed
    return -reverse if is_negative else reverse


# ─────────────────────────────────────────────
#  APPROACH 2 — Optimized (String Slicing)
# ─────────────────────────────────────────────

def reverse_number_string(num: int) -> int:
    """
    Reverse the digits of an integer using Python string slicing.

    Algorithm:
        1. Convert |num| to a string.
        2. Reverse the string with [::-1].
        3. Convert back to int (leading zeros are dropped automatically).
        4. Restore sign.

    Args:
        num (int): Any integer (positive, negative, or zero).

    Returns:
        int: The digit-reversed integer.

    Time  : O(d) — string reversal is proportional to digit count
    Space : O(d) — a reversed string of length d is created
    """
    is_negative = num < 0

    # Work with the absolute value; convert to string and reverse
    reversed_str = str(abs(num))[::-1]

    # int() silently drops any leading zeros (e.g., "0021" → 21)
    result = int(reversed_str)

    return -result if is_negative else result


# ─────────────────────────────────────────────
#  HELPER — Display result neatly
# ─────────────────────────────────────────────

def display_result(original: int, result: int, approach: str) -> None:
    """Print the result in a formatted way."""
    print(f"\n  Original Number  : {original}")
    print(f"  Approach         : {approach}")
    print(f"  Reversed Number  : {result}")
    print("  " + "─" * 35)


# ─────────────────────────────────────────────
#  MAIN — Menu-Driven Program
# ─────────────────────────────────────────────

def main():
    """
    Menu-driven program to reverse a number using two approaches.
    Validates input and lets the user pick their preferred method.
    """
    print("=" * 45)
    print("          REVERSE A NUMBER")
    print("=" * 45)

    # ── Get input ──────────────────────────────
    while True:
        try:
            num = int(input("\nEnter an integer: "))
            break
        except ValueError:
            print("  [Error] Please enter a valid integer.")

    original = num  # save original before modification

    # ── Menu ───────────────────────────────────
    print("\nChoose an approach:")
    print("  1. Brute Force  — Loop + Integer Division")
    print("  2. Optimized    — String Slicing")
    print("  3. All          — Run Both & Compare")

    while True:
        choice = input("\nYour choice (1–3): ").strip()
        if choice in {"1", "2", "3"}:
            break
        print("  [Error] Enter 1, 2, or 3.")

    # ── Execute ────────────────────────────────
    print()
    if choice == "1":
        result = reverse_number_brute(num)
        display_result(original, result, "Brute Force (Loop Division)")

    elif choice == "2":
        result = reverse_number_string(num)
        display_result(original, result, "Optimized (String Slicing)")

    elif choice == "3":
        r1 = reverse_number_brute(num)
        r2 = reverse_number_string(num)
        display_result(original, r1, "Brute Force (Loop Division)")
        display_result(original, r2, "Optimized (String Slicing)")


if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

Using **`num = 1234`** as the primary example.

---

### Dry Run — Brute Force (Loop Division)

> Pre-processing: `is_negative = False`, `num = 1234`, `reverse = 0`

| Step | `num` Before | Operation                        | `digit` | `reverse` Before | `reverse` After | `num` After | Explanation                              |
|------|--------------|----------------------------------|---------|------------------|-----------------|-------------|------------------------------------------|
| 1    | 1234         | `digit = 1234 % 10`              | 4       | 0                | —               | —           | Last digit is `4`                        |
|      | 1234         | `reverse = 0 * 10 + 4`           | 4       | 0                | 4               | —           | Append `4` to reversed                   |
|      | 1234         | `num = 1234 // 10`               | —       | —                | 4               | 123         | Strip last digit                         |
| 2    | 123          | `digit = 123 % 10`               | 3       | 4                | —               | —           | Last digit is `3`                        |
|      | 123          | `reverse = 4 * 10 + 3`           | 3       | 4                | 43              | —           | Shift left, append `3`                   |
|      | 123          | `num = 123 // 10`                | —       | —                | 43              | 12          | Strip last digit                         |
| 3    | 12           | `digit = 12 % 10`                | 2       | 43               | —               | —           | Last digit is `2`                        |
|      | 12           | `reverse = 43 * 10 + 2`          | 2       | 43               | 432             | —           | Shift left, append `2`                   |
|      | 12           | `num = 12 // 10`                 | —       | —                | 432             | 1           | Strip last digit                         |
| 4    | 1            | `digit = 1 % 10`                 | 1       | 432              | —               | —           | Last digit is `1`                        |
|      | 1            | `reverse = 432 * 10 + 1`         | 1       | 432              | 4321            | —           | Shift left, append `1`                   |
|      | 1            | `num = 1 // 10`                  | —       | —                | 4321            | 0           | Strip last digit                         |
| End  | 0            | `while 0 > 0`?                   | —       | —                | 4321            | —           | Condition False → loop exits             |

**Final Result:** `reverse = 4321` ✓

---

### Dry Run — Edge Case: `num = 100` (Trailing Zeros)

> Pre-processing: `is_negative = False`, `num = 100`, `reverse = 0`

| Step | `num` Before | `digit` | Operation                   | `reverse` After | `num` After | Explanation                         |
|------|--------------|---------|-----------------------------|-----------------|-------------|-------------------------------------|
| 1    | 100          | 0       | `reverse = 0 * 10 + 0`      | 0               | 10          | Extracted trailing zero             |
| 2    | 10           | 0       | `reverse = 0 * 10 + 0`      | 0               | 1           | Extracted second zero               |
| 3    | 1            | 1       | `reverse = 0 * 10 + 1`      | 1               | 0           | Extracted the digit `1`             |
| End  | 0            | —       | Loop exits                  | 1               | —           | Leading zeros dropped automatically |

**Final Result:** `1` ✓ (not `001`)

---

### Dry Run — Edge Case: `num = -987`

| Step | Operation                    | Value  | Explanation                              |
|------|------------------------------|--------|------------------------------------------|
| Pre  | `is_negative = (-987 < 0)`   | `True` | Flag the sign                            |
| Pre  | `num = abs(-987)`            | `987`  | Work with the positive value             |
| 1    | `digit = 987 % 10`           | `7`    | Extract `7`; `reverse = 7`; `num = 98`   |
| 2    | `digit = 98 % 10`            | `8`    | Extract `8`; `reverse = 78`; `num = 9`   |
| 3    | `digit = 9 % 10`             | `9`    | Extract `9`; `reverse = 789`; `num = 0`  |
| End  | `is_negative` is True        | `-789` | Restore sign → return `-789`             |

**Final Result:** `-789` ✓

---

### Dry Run — Optimized (String Slicing) for `num = 1234`

| Step | Operation                   | Value      | Explanation                                        |
|------|-----------------------------|------------|----------------------------------------------------|
| 1    | `is_negative = (1234 < 0)`  | `False`    | Positive number, no sign flag needed               |
| 2    | `abs(1234)`                 | `1234`     | No change                                          |
| 3    | `str(1234)`                 | `"1234"`   | Convert integer to string                          |
| 4    | `"1234"[::-1]`              | `"4321"`   | Python reverses the string from right to left      |
| 5    | `int("4321")`               | `4321`     | Convert back to integer                            |
| End  | `return 4321`               | `4321`     | Not negative, return as-is ✓                       |

**Final Result:** `4321` ✓

---

### Dry Run — Optimized (String Slicing) for `num = 100`

| Step | Operation         | Value    | Explanation                                          |
|------|-------------------|----------|------------------------------------------------------|
| 1    | `str(abs(100))`   | `"100"`  | Convert to string                                    |
| 2    | `"100"[::-1]`     | `"001"`  | String reversed character by character               |
| 3    | `int("001")`      | `1`      | `int()` drops leading zeros automatically            |
| End  | `return 1`        | `1`      | ✓                                                    |

**Final Result:** `1` ✓

---

## 7. Time & Space Complexity

### Brute Force — Loop Division

| Metric | Complexity | Reason                                                                                      |
|--------|------------|---------------------------------------------------------------------------------------------|
| Time   | **O(d)**   | The loop runs exactly `d` times — once per digit. `d ≈ log₁₀(num)`                         |
| Space  | **O(1)**   | Only three variables used (`num`, `digit`, `reverse`) — constant space regardless of input  |

- **Best case:** O(1) — single digit input
- **Worst case:** O(d) — input with `d` digits

---

### Optimized — String Slicing

| Metric | Complexity | Reason                                                                                  |
|--------|------------|-----------------------------------------------------------------------------------------|
| Time   | **O(d)**   | `str()` conversion and `[::-1]` slicing both scan all `d` characters                   |
| Space  | **O(d)**   | Two strings of length `d` are created in memory: the original string and its reverse    |

- Same time complexity as brute force, but with added memory overhead
- In practice, extremely fast in Python due to C-level string implementation

---

### Summary Table

| Approach           | Time  | Space | Pros                                  | Cons                                    |
|--------------------|-------|-------|---------------------------------------|-----------------------------------------|
| Brute Force (Loop) | O(d)  | O(1)  | Memory-efficient, builds core intuition | More lines of code                     |
| String Slicing     | O(d)  | O(d)  | Concise, very readable, Pythonic       | Extra memory for string objects         |

---

## 8. Beginner Tips

### 🔑 Core Hacks & Rules of Thumb

1. **`num % 10` always gives you the last digit.**
   This is the single most important pattern in digit-manipulation problems. Memorise it — it applies to reversing, summing digits, checking Armstrong numbers, and more.

2. **`reverse * 10 + digit` is how you build a number digit by digit.**
   Multiplying by 10 "makes room" on the right (shifts all digits one place left), then adding the new digit places it in the ones position. This pattern appears in every "build from digits" problem.

3. **`[::-1]` is Python's string reversal shortcut.**
   `s[::-1]` returns a new string with characters in reverse order. It works on any sequence (strings, lists, tuples). For this problem it gives a one-liner solution.

4. **`int()` silently drops leading zeros.**
   `int("0021")` gives `21`, not `21` with any extra formatting. This is why trailing zeros in the original number (which become leading zeros when reversed) are handled automatically.

5. **Always save the original input before modifying it.**
   The brute force approach destroys `num` during the loop. If you need to display or use the original later, save it in a separate variable at the start (e.g., `original = num`).

6. **Handle the sign before the loop, restore it after.**
   The cleanest pattern: `is_negative = num < 0`, then `num = abs(num)`, run your logic, then `return -result if is_negative else result`.

---

### ⚠️ Edge Case Reminders

| Scenario               | What Goes Wrong Without a Fix             | Fix                                      |
|------------------------|-------------------------------------------|------------------------------------------|
| `num = 0`              | Loop never runs → returns `0` (correct accidentally) | Add `if num == 0: return 0` for clarity |
| `num < 0`              | `%` and `//` behave oddly with negatives in some languages | Use `abs()` before the loop             |
| Trailing zeros (`1200`)| Result `0021` has leading zeros           | `int()` drops them automatically         |
| Single digit           | Loop runs once → returns the digit itself | No special handling needed               |

---

### 📊 Approach Comparison at a Glance

| When to use...       | Reason                                                             |
|----------------------|--------------------------------------------------------------------|
| **Loop (Brute)**     | Interviews, understanding fundamentals, memory-sensitive contexts  |
| **String Slicing**   | Quick scripts, competitive programming, when readability matters   |

---

### 🧠 Patterns This Problem Teaches

Mastering digit reversal unlocks a whole family of problems:

| Problem                  | How It Connects                                                  |
|--------------------------|------------------------------------------------------------------|
| **Palindrome Number**    | A number is a palindrome if `reverse(n) == n`                    |
| **Armstrong Number**     | Sum of each digit raised to power d — uses the same `% 10` loop |
| **Count Digits**         | Same loop structure, just increment a counter instead            |
| **Sum of Digits**        | Accumulate `num % 10` each iteration instead of building reverse |
| **Check Divisibility**   | Reversals used in rules for 11, 9, etc.                          |

> **The `% 10` → process → `// 10` loop is the universal skeleton for all digit-by-digit problems. Change only what you do with the digit.**

---

*End of Study Guide — Reverse a Number*
