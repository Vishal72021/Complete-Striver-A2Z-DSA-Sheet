# Palindrome Number

---

## 1. Name of the Problem

**Palindrome Number**

A classic number-theory problem: given an integer `n`, determine whether it reads the same forwards and backwards.

---

## 2. Problem Statement

### What is being solved?

Given an integer `num`, check whether it is a **palindrome** — a number whose digit sequence is identical when reversed.

> **Notes:**
> - The original code handles only **positive** integers (the `while num > 0` loop skips negatives and zero).
> - By mathematical convention, **negative numbers are never palindromes** (the `-` sign breaks the symmetry).
> - **0 is a palindrome** — it reads the same both ways.
> - Numbers with **trailing zeros** (other than `0` itself) can never be palindromes, because the reversed form would have a leading zero, making it a smaller number (e.g., `100` reversed is `1` ≠ `100`).

---

### Example Input / Output

| Input (`num`) | Reversed | Is Palindrome? | Explanation                            |
|---------------|----------|----------------|----------------------------------------|
| `121`         | `121`    | ✅ Yes          | Reads the same forwards and backwards  |
| `12321`       | `12321`  | ✅ Yes          | Symmetric digit sequence               |
| `123`         | `321`    | ❌ No           | `321 ≠ 123`                            |
| `0`           | `0`      | ✅ Yes          | Zero is its own mirror                 |
| `-121`        | N/A      | ❌ No           | Negatives are never palindromes        |
| `1221`        | `1221`   | ✅ Yes          | Even-length palindrome                 |
| `100`         | `1`      | ❌ No           | Trailing zero creates mismatch         |

---

## 3. Logic Behind the Solution

### Part A — Intuition: How to Think About It

A palindrome is a **mirror number**. The digit at position 1 must equal the digit at the last position, position 2 must equal the second-to-last, and so on.

The simplest way to check this: **reverse the number** and compare it to the original.

- If `reverse == original` → palindrome ✅
- If `reverse ≠ original` → not a palindrome ❌

> **The key insight:** We already know how to reverse a number (from the previous problem). Palindrome checking is just **one extra comparison** on top of that.

**Visualising `121`:**

```
Original : 1  2  1
           ↕     ↕
Reversed : 1  2  1   ← identical ✅
```

**Visualising `123`:**

```
Original : 1  2  3
           ↕     ↕
Reversed : 3  2  1   ← different ❌
```

---

### Part B — Approaches

#### Approach 1: Brute Force (Reverse & Compare)

- Save the original number before modification
- Reverse the number digit by digit using `% 10` and `// 10`
- Compare the reversed number to the saved original
- **Edge cases:** handle negatives (always false), zero (always true), and trailing zeros (auto-handled by reversal)

#### Approach 2: Optimized (String Conversion & Slicing)

- Convert the number to a string
- Compare the string to its reverse using `str == str[::-1]`
- No manual reversal loop needed
- Handles all cases cleanly in one line

#### Approach 3: Half-Reversal (Most Efficient — Interview Favourite)

- Only reverse **half** the digits
- Compare the reversed half against the remaining half
- **Why?** You do half the work, and you avoid overflow issues in languages with fixed integer sizes
- Works because a palindrome's first half mirrors its second half exactly

#### Edge Cases to Always Handle

| Edge Case               | Expected Behaviour                                        |
|-------------------------|-----------------------------------------------------------|
| `num < 0`               | Always `False` — negatives cannot be palindromes          |
| `num == 0`              | Always `True` — zero is a palindrome                      |
| Trailing zero (`num % 10 == 0`) | Always `False` (except `num == 0`)              |
| Single digit (`0–9`)    | Always `True` — any single digit is a palindrome          |
| Even-length palindrome  | Works the same — e.g., `1221`                             |

---

## 4. Pseudocode

### Brute Force (Reverse & Compare)

```
FUNCTION is_palindrome_brute(num):
    IF num < 0:
        RETURN False              ← negatives are never palindromes

    IF num == 0:
        RETURN True               ← zero is always a palindrome

    original ← num
    reverse  ← 0

    WHILE num > 0:
        digit   ← num MOD 10
        reverse ← reverse * 10 + digit
        num     ← num // 10

    RETURN (reverse == original)
```

### Optimized (String Comparison)

```
FUNCTION is_palindrome_string(num):
    IF num < 0:
        RETURN False

    s ← string representation of num
    RETURN (s == reverse of s)       ← s == s[::-1]
```

### Half-Reversal (Most Efficient)

```
FUNCTION is_palindrome_half(num):
    IF num < 0:
        RETURN False

    IF num != 0 AND num MOD 10 == 0:
        RETURN False              ← trailing zero means not palindrome

    reversed_half ← 0

    WHILE num > reversed_half:    ← stop at the midpoint
        digit         ← num MOD 10
        reversed_half ← reversed_half * 10 + digit
        num           ← num // 10

    ← For even-length: num == reversed_half
    ← For odd-length:  num == reversed_half // 10  (discard middle digit)
    RETURN (num == reversed_half) OR (num == reversed_half // 10)
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Palindrome Number
  Approach : Brute Force (Reverse & Compare)
             Optimized  (String Slicing)
             Efficient  (Half-Reversal)
  Author   : Study Guide Generator
=============================================================
"""


# ─────────────────────────────────────────────
#  APPROACH 1 — Brute Force (Reverse & Compare)
# ─────────────────────────────────────────────

def is_palindrome_brute(num: int) -> bool:
    """
    Check if a number is a palindrome by reversing it fully and comparing.

    Algorithm:
        1. Reject negatives immediately.
        2. Save the original value.
        3. Reverse the number digit by digit.
        4. Compare reversed to original.

    Args:
        num (int): Any integer.

    Returns:
        bool: True if num is a palindrome, False otherwise.

    Time  : O(d) — d = number of digits
    Space : O(1) — only scalar variables
    """
    # Negatives are never palindromes
    if num < 0:
        return False

    # Zero is always a palindrome
    if num == 0:
        return True

    original = num   # save before modification
    reverse  = 0

    while num > 0:
        digit   = num % 10               # extract last digit
        reverse = reverse * 10 + digit   # append digit to reversed number
        num     = num // 10              # strip last digit

    return reverse == original


# ─────────────────────────────────────────────
#  APPROACH 2 — Optimized (String Slicing)
# ─────────────────────────────────────────────

def is_palindrome_string(num: int) -> bool:
    """
    Check if a number is a palindrome using string reversal.

    Algorithm:
        1. Reject negatives immediately.
        2. Convert to string and compare with its reverse.

    Args:
        num (int): Any integer.

    Returns:
        bool: True if num is a palindrome, False otherwise.

    Time  : O(d) — string reversal scans all d characters
    Space : O(d) — reversed string stored in memory
    """
    if num < 0:
        return False

    s = str(num)
    return s == s[::-1]   # compare string to its reverse


# ─────────────────────────────────────────────
#  APPROACH 3 — Efficient (Half-Reversal)
# ─────────────────────────────────────────────

def is_palindrome_half(num: int) -> bool:
    """
    Check if a number is a palindrome by reversing only half of it.

    Algorithm:
        1. Reject negatives and numbers with trailing zeros.
        2. Reverse digits of the right half while the left half > right half.
        3. At midpoint: for even length  → left == right
                        for odd length   → left == right // 10 (skip middle digit)

    Args:
        num (int): Any integer.

    Returns:
        bool: True if num is a palindrome, False otherwise.

    Time  : O(d/2) — only half the digits are processed
    Space : O(1)
    """
    # Negatives are never palindromes
    if num < 0:
        return False

    # Numbers ending in 0 (except 0 itself) cannot be palindromes
    # because leading zeros are not valid → reversed would be smaller
    if num != 0 and num % 10 == 0:
        return False

    reversed_half = 0

    # Reverse until the right half catches up to the left half
    while num > reversed_half:
        digit         = num % 10
        reversed_half = reversed_half * 10 + digit
        num           = num // 10

    # Even-length: e.g., 1221 → num=12, reversed_half=12
    # Odd-length : e.g., 12321 → num=12, reversed_half=123 → 123//10=12
    return num == reversed_half or num == reversed_half // 10


# ─────────────────────────────────────────────
#  HELPER — Display result neatly
# ─────────────────────────────────────────────

def display_result(original: int, result: bool, approach: str) -> None:
    """Print the palindrome check result in a formatted way."""
    verdict = "✅ PALINDROME" if result else "❌ NOT a Palindrome"
    print(f"\n  Number   : {original}")
    print(f"  Approach : {approach}")
    print(f"  Result   : {verdict}")
    print("  " + "─" * 38)


# ─────────────────────────────────────────────
#  MAIN — Menu-Driven Program
# ─────────────────────────────────────────────

def main():
    """
    Menu-driven program to check if a number is a palindrome.
    Offers three approaches with input validation.
    """
    print("=" * 48)
    print("           PALINDROME NUMBER CHECK")
    print("=" * 48)

    # ── Get input ──────────────────────────────
    while True:
        try:
            num = int(input("\nEnter an integer: "))
            break
        except ValueError:
            print("  [Error] Please enter a valid integer.")

    original = num

    # ── Menu ───────────────────────────────────
    print("\nChoose an approach:")
    print("  1. Brute Force  — Reverse & Compare")
    print("  2. Optimized    — String Slicing")
    print("  3. Efficient    — Half-Reversal (Interview Favourite)")
    print("  4. All          — Run All Three & Compare")

    while True:
        choice = input("\nYour choice (1–4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            break
        print("  [Error] Enter a number between 1 and 4.")

    # ── Execute ────────────────────────────────
    print()
    if choice == "1":
        result = is_palindrome_brute(num)
        display_result(original, result, "Brute Force (Reverse & Compare)")

    elif choice == "2":
        result = is_palindrome_string(num)
        display_result(original, result, "Optimized (String Slicing)")

    elif choice == "3":
        result = is_palindrome_half(num)
        display_result(original, result, "Efficient (Half-Reversal)")

    elif choice == "4":
        r1 = is_palindrome_brute(num)
        r2 = is_palindrome_string(num)
        r3 = is_palindrome_half(num)
        display_result(original, r1, "Brute Force (Reverse & Compare)")
        display_result(original, r2, "Optimized (String Slicing)")
        display_result(original, r3, "Efficient (Half-Reversal)")


if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

---

### Dry Run — Brute Force: `num = 121` (Palindrome ✅)

> Pre-processing: `original = 121`, `reverse = 0`

| Step | `num` Before | `digit` | Operation                   | `reverse` Before | `reverse` After | `num` After | Explanation                     |
|------|--------------|---------|-----------------------------|------------------|-----------------|-------------|---------------------------------|
| 1    | 121          | 1       | `digit = 121 % 10`          | 0                | —               | —           | Last digit is `1`               |
|      | 121          | 1       | `reverse = 0 * 10 + 1`      | 0                | 1               | —           | Append `1` to reverse           |
|      | 121          | —       | `num = 121 // 10`           | —                | 1               | 12          | Strip last digit                |
| 2    | 12           | 2       | `digit = 12 % 10`           | 1                | —               | —           | Last digit is `2`               |
|      | 12           | 2       | `reverse = 1 * 10 + 2`      | 1                | 12              | —           | Append `2`                      |
|      | 12           | —       | `num = 12 // 10`            | —                | 12              | 1           | Strip last digit                |
| 3    | 1            | 1       | `digit = 1 % 10`            | 12               | —               | —           | Last digit is `1`               |
|      | 1            | 1       | `reverse = 12 * 10 + 1`     | 12               | 121             | —           | Append `1`                      |
|      | 1            | —       | `num = 1 // 10`             | —                | 121             | 0           | Strip last digit                |
| End  | 0            | —       | `while 0 > 0`? → False      | —                | 121             | —           | Loop exits                      |
| ✅   | —            | —       | `121 == 121`?               | —                | —               | —           | **True → Palindrome**           |

**Final Result:** `True` ✅

---

### Dry Run — Brute Force: `num = 123` (Not a Palindrome ❌)

> Pre-processing: `original = 123`, `reverse = 0`

| Step | `num` Before | `digit` | `reverse` After | `num` After | Explanation               |
|------|--------------|---------|-----------------|-------------|---------------------------|
| 1    | 123          | 3       | 3               | 12          | Extracted `3`             |
| 2    | 12           | 2       | 32              | 1           | Extracted `2`             |
| 3    | 1            | 1       | 321             | 0           | Extracted `1`             |
| End  | 0            | —       | 321             | —           | Loop exits                |
| ❌   | —            | —       | `321 == 123`?   | —           | **False → Not Palindrome** |

**Final Result:** `False` ❌

---

### Dry Run — Edge Cases Summary

| Input  | `original` | `reverse` | `reverse == original` | Result |
|--------|------------|-----------|-----------------------|--------|
| `0`    | 0          | —         | Early return `True`   | ✅     |
| `-121` | -121       | —         | Early return `False`  | ❌     |
| `100`  | 100        | 1         | `1 == 100`? No        | ❌     |
| `7`    | 7          | 7         | `7 == 7`? Yes         | ✅     |
| `1221` | 1221       | 1221      | `1221 == 1221`? Yes   | ✅     |

---

### Dry Run — Half-Reversal: `num = 1221` (Even-length Palindrome ✅)

> Pre-processing: `num = 1221`, `reversed_half = 0`
> Loop stops when `num ≤ reversed_half` (right half catches up to left half)

| Step | `num` Before | `digit` | `reversed_half` Before | `reversed_half` After | `num` After | `num > reversed_half`? | Explanation                        |
|------|--------------|---------|------------------------|-----------------------|-------------|------------------------|------------------------------------|
| 1    | 1221         | 1       | 0                      | 1                     | 122         | 122 > 1 → Yes          | Extract `1` from right             |
| 2    | 122          | 2       | 1                      | 12                    | 12          | 12 > 12 → No           | Extract `2`; halves are equal size |
| End  | —            | —       | —                      | 12                    | 12          | Loop exits             | Midpoint reached                   |
| ✅   | —            | —       | `12 == 12`?            | —                     | —           | **True → Palindrome**  | Even-length: left == right         |

**Final Result:** `True` ✅

---

### Dry Run — Half-Reversal: `num = 12321` (Odd-length Palindrome ✅)

> Pre-processing: `num = 12321`, `reversed_half = 0`

| Step | `num` Before | `digit` | `reversed_half` After | `num` After | `num > rev_half`? | Explanation                     |
|------|--------------|---------|-----------------------|-------------|-------------------|---------------------------------|
| 1    | 12321        | 1       | 1                     | 1232        | 1232 > 1 → Yes    | Extract rightmost `1`           |
| 2    | 1232         | 2       | 12                    | 123         | 123 > 12 → Yes    | Extract `2`                     |
| 3    | 123          | 3       | 123                   | 12          | 12 > 123 → No     | Extract middle digit `3`; stop  |
| End  | —            | —       | 123                   | 12          | Loop exits        | Midpoint passed                 |
| ✅   | —            | —       | `12 == 123 // 10`?    | —           | `12 == 12`? Yes   | Odd-length: discard middle `3`  |

**Final Result:** `True` ✅

---

## 7. Time & Space Complexity

### Approach 1 — Brute Force (Reverse & Compare)

| Metric | Complexity | Reason                                                                      |
|--------|------------|-----------------------------------------------------------------------------|
| Time   | **O(d)**   | Loop runs exactly `d` times — once per digit in `num`                       |
| Space  | **O(1)**   | Only `original`, `num`, `digit`, `reverse` — constant number of variables   |

---

### Approach 2 — Optimized (String Slicing)

| Metric | Complexity | Reason                                                                         |
|--------|------------|--------------------------------------------------------------------------------|
| Time   | **O(d)**   | `str()` conversion is O(d); `[::-1]` slicing is O(d); comparison is O(d)       |
| Space  | **O(d)**   | Two strings of length `d` exist in memory simultaneously during comparison     |

---

### Approach 3 — Efficient (Half-Reversal)

| Metric | Complexity | Reason                                                                          |
|--------|------------|---------------------------------------------------------------------------------|
| Time   | **O(d/2)** | The loop processes only half the digits before the condition `num > reversed_half` becomes False |
| Space  | **O(1)**   | Only two integer variables — `num` and `reversed_half`                          |

---

### Summary Table

| Approach              | Time    | Space  | Best For                                        |
|-----------------------|---------|--------|-------------------------------------------------|
| Brute Force (Reverse) | O(d)    | O(1)   | Learning; clear to read and understand          |
| String Slicing        | O(d)    | O(d)   | Quick solutions; most Pythonic                  |
| Half-Reversal         | O(d/2)  | O(1)   | Interviews; memory-safe; large integer problems |

> **Interview tip:** Interviewers often ask you to solve this **without converting to a string**. The half-reversal approach is the expected answer in that case.

---

## 8. Beginner Tips

### 🔑 Core Hacks & Rules of Thumb

1. **Palindrome = Reverse equals Original.**
   The entire problem reduces to this one comparison. Master the reversal pattern first (previous problem), and palindrome check is just one extra `==` at the end.

2. **Negative numbers are NEVER palindromes — handle them first.**
   The minus sign `−` has no mirror counterpart on the right side. Always add `if num < 0: return False` as your very first line.

3. **Trailing zeros (except `0` itself) are NEVER palindromes.**
   If a number ends in `0`, its reversed form has a leading zero, making it smaller than the original. So `num % 10 == 0 and num != 0` → always `False`. This is a built-in early-exit optimisation.

4. **Single-digit numbers are ALWAYS palindromes.**
   Any number from `0` to `9` reversed is itself. No special case needed — the logic handles it automatically.

5. **The half-reversal trick is the interview gold standard.**
   You only process `d/2` digits, and you never need the original saved separately — the shrinking `num` acts as the left half, and `reversed_half` acts as the right half. When `num ≤ reversed_half`, you've crossed the midpoint.

6. **Even vs Odd length palindromes have different midpoint checks.**
   - **Even** (`1221`): at the midpoint, `num == reversed_half`
   - **Odd** (`12321`): at the midpoint, `num == reversed_half // 10` (the middle digit is discarded)
   Both cases are handled cleanly with: `return num == reversed_half or num == reversed_half // 10`

---

### ⚠️ Edge Case Reminders

| Scenario                | Trap                                          | Safe Handling                             |
|-------------------------|-----------------------------------------------|-------------------------------------------|
| `num < 0`               | Loop won't catch it; wrong result             | `if num < 0: return False` at the top    |
| `num = 0`               | Loop skips; returns `0 == 0` → works fine     | Explicitly return `True` for clarity      |
| `num = 10, 100, 1000…`  | Reversed form drops leading zero → mismatch   | `if num % 10 == 0 and num != 0: return False` |
| Single digit `1–9`      | Loop runs once; reverse equals original → ✅  | No extra handling needed                  |
| Even-length palindrome  | Half-reversal midpoint: `num == reversed_half`| Covered by `or` condition                 |
| Odd-length palindrome   | Middle digit must be discarded                | Use `reversed_half // 10`                 |

---

### 📊 Approach Comparison at a Glance

| When to use...         | Reason                                                                |
|------------------------|-----------------------------------------------------------------------|
| **Brute Force**        | Great for learning; identical logic to reverse-a-number              |
| **String Slicing**     | One-liner for scripts; most readable for teammates                   |
| **Half-Reversal**      | Interview setting; when told "no string conversion allowed"           |

---

### 🧠 How This Problem Connects to Others

| Problem                      | Connection                                                         |
|------------------------------|--------------------------------------------------------------------|
| **Reverse a Number**         | Direct prerequisite — palindrome check IS reverse + compare        |
| **Count Digits**             | Used inside half-reversal to determine even/odd length             |
| **Palindrome String**        | Same concept applied to characters instead of digits               |
| **Palindrome Linked List**   | Same idea; uses two-pointer + reversal on a list structure         |
| **Largest Palindrome Product**| Builds on this check inside a search loop                         |
| **Valid Palindrome (LeetCode #125)** | String version with alphanumeric filtering                 |

> **The mental model to carry forward:** A palindrome problem always reduces to — *does the first half mirror the second half?* Whether it's a number, a string, an array, or a linked list, the solution strategy is always the same: meet in the middle and compare.

---

*End of Study Guide — Palindrome Number*
