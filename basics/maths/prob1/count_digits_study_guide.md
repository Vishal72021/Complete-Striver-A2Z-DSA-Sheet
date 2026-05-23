# Count Digits in a Number

---

## 1. Name of the Problem

**Count Digits in a Number**

A classic foundational problem in programming: given an integer `n`, determine how many digits it contains.

---

## 2. Problem Statement

### What is being solved?

Given an integer `n` (which may be positive, negative, or zero), count the total number of digits present in it.

> **Note:** The sign (`-`) of a negative number is **not** counted as a digit. Only the numeric characters (0–9) are counted. Zero (`0`) is treated as having exactly **1** digit.

---

### Example Input / Output

| Input (`n`) | Expected Output | Explanation                     |
|-------------|-----------------|----------------------------------|
| `12345`     | `5`             | Five digits: 1, 2, 3, 4, 5      |
| `0`         | `1`             | Zero has one digit: 0            |
| `-987`      | `3`             | Three digits: 9, 8, 7 (sign ignored) |
| `7`         | `1`             | Single digit: 7                  |
| `1000000`   | `7`             | Seven digits: 1, 0, 0, 0, 0, 0, 0 |

---

## 3. Logic Behind the Solution

### Part A — Intuition: How to Think About It

Imagine you are manually counting digits in `4523`:

- You look at `4` → count 1
- You look at `5` → count 2
- You look at `2` → count 3
- You look at `3` → count 4

You peel off one digit at a time from the right using **integer division by 10** (`n // 10`), and increment a counter each time.

This is exactly what the loop does — it strips the last digit away until nothing remains.

**Why divide by 10?**
- `4523 // 10` → `452` (removed the `3`)
- `452 // 10` → `45` (removed the `2`)
- `45 // 10` → `4`  (removed the `5`)
- `4 // 10` → `0`   (removed the `4`) → loop ends

Each division strips one digit, so the number of divisions equals the number of digits.

---

### Part B — Approaches

#### Approach 1: Brute Force (Loop-based Division)

- Strip one digit at a time using `n = n // 10`
- Increment a counter each iteration
- Stop when `n` becomes `0`
- **Edge case:** Handle `n = 0` separately (the loop never runs, but it has 1 digit)
- **Edge case:** Handle negative numbers by taking `abs(n)` before counting

#### Approach 2: Optimized (String Conversion / Math-based)

- **String method:** Convert to string, strip the `-` sign if any, and return `len(str(abs(n)))`
- **Math method (logarithm):** `floor(log10(n)) + 1` gives digit count directly for `n > 0`
  - `log10(4523)` ≈ `3.655` → `floor(3.655) + 1` = `4` ✓
- Both run in **O(1)** conceptual time for fixed-size integers, though the string approach has O(d) where d is digits

#### Edge Cases to Always Handle

| Edge Case         | Expected Behaviour                     |
|-------------------|----------------------------------------|
| `n = 0`           | Return `1` (zero is a 1-digit number)  |
| `n < 0`           | Take absolute value before counting    |
| Very large `n`    | Loop/string works; log10 risks float precision |

---

## 4. Pseudocode

### Brute Force (Loop Division)

```
FUNCTION count_digits_brute(n):
    IF n == 0:
        RETURN 1

    n ← absolute value of n
    count ← 0

    WHILE n > 0:
        count ← count + 1
        n ← n // 10        ← strip last digit

    RETURN count
```

### Optimized (String Conversion)

```
FUNCTION count_digits_optimized(n):
    RETURN length of string representation of absolute value of n
    
    i.e., RETURN len(str(abs(n)))
```

### Optimized (Logarithm — Math-based)

```
FUNCTION count_digits_log(n):
    IF n == 0:
        RETURN 1

    n ← absolute value of n
    RETURN floor(log10(n)) + 1
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Count Digits in a Number
  Approach : Brute Force (Loop) | Optimized (String / Log)
  Author   : Study Guide Generator
=============================================================
"""

import math


# ─────────────────────────────────────────────
#  APPROACH 1 — Brute Force (Loop-based)
# ─────────────────────────────────────────────

def count_digits_brute(n: int) -> int:
    """
    Count digits using repeated integer division by 10.

    Args:
        n (int): Any integer (positive, negative, or zero).

    Returns:
        int: Number of digits in n.

    Time  : O(d) where d = number of digits
    Space : O(1)
    """
    # Edge case: 0 has exactly one digit
    if n == 0:
        return 1

    # Negative numbers: ignore the minus sign
    n = abs(n)

    count = 0
    while n > 0:
        count += 1       # count this digit
        n = n // 10      # strip the last digit

    return count


# ─────────────────────────────────────────────
#  APPROACH 2a — Optimized (String Conversion)
# ─────────────────────────────────────────────

def count_digits_string(n: int) -> int:
    """
    Count digits by converting the number to its string form.

    Args:
        n (int): Any integer (positive, negative, or zero).

    Returns:
        int: Number of digits in n.

    Time  : O(d) for string conversion, where d = digit count
    Space : O(d) for the string object
    """
    # abs() removes the '-' sign for negatives; str() converts to string
    return len(str(abs(n)))


# ─────────────────────────────────────────────
#  APPROACH 2b — Optimized (Logarithm)
# ─────────────────────────────────────────────

def count_digits_log(n: int) -> int:
    """
    Count digits using the mathematical property:
        digit_count = floor(log10(n)) + 1  for n > 0

    Args:
        n (int): Any integer (positive, negative, or zero).

    Returns:
        int: Number of digits in n.

    Time  : O(1) — single math operation
    Space : O(1)

    Warning:
        Floating-point precision can cause off-by-one errors for
        very large integers (e.g., powers of 10). Use with caution.
    """
    # Edge case: log10(0) is undefined; 0 has 1 digit
    if n == 0:
        return 1

    n = abs(n)  # handle negatives

    return math.floor(math.log10(n)) + 1


# ─────────────────────────────────────────────
#  HELPER — Display result neatly
# ─────────────────────────────────────────────

def display_result(n: int, result: int, approach: str) -> None:
    """Print the result in a formatted way."""
    print(f"\n  Number   : {n}")
    print(f"  Approach : {approach}")
    print(f"  Digits   : {result}")
    print("  " + "─" * 30)


# ─────────────────────────────────────────────
#  MAIN — Menu-Driven Program
# ─────────────────────────────────────────────

def main():
    """
    Menu-driven program to count digits using three approaches.
    Lets the user choose their preferred method interactively.
    """
    print("=" * 45)
    print("       COUNT DIGITS IN A NUMBER")
    print("=" * 45)

    # ── Get input ──────────────────────────────
    while True:
        try:
            n = int(input("\nEnter an integer: "))
            break
        except ValueError:
            print("  [Error] Please enter a valid integer.")

    # ── Menu ───────────────────────────────────
    print("\nChoose an approach:")
    print("  1. Brute Force   — Loop + Integer Division")
    print("  2. Optimized     — String Conversion")
    print("  3. Optimized     — Logarithm (Math)")
    print("  4. All Three     — Compare All Approaches")

    while True:
        choice = input("\nYour choice (1–4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            break
        print("  [Error] Enter a number between 1 and 4.")

    # ── Execute chosen approach ─────────────────
    print()
    if choice == "1":
        result = count_digits_brute(n)
        display_result(n, result, "Brute Force (Loop Division)")

    elif choice == "2":
        result = count_digits_string(n)
        display_result(n, result, "Optimized (String Conversion)")

    elif choice == "3":
        result = count_digits_log(n)
        display_result(n, result, "Optimized (Logarithm)")

    elif choice == "4":
        r1 = count_digits_brute(n)
        r2 = count_digits_string(n)
        r3 = count_digits_log(n)
        display_result(n, r1, "Brute Force (Loop Division)")
        display_result(n, r2, "Optimized (String Conversion)")
        display_result(n, r3, "Optimized (Logarithm)")


if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

Using **`n = 4523`** as the example throughout.

---

### Dry Run — Brute Force (Loop Division)

> Pre-processing: `n = abs(4523) = 4523`, `count = 0`

| Step | `n` Before | Operation      | `n` After | `count` | Explanation                              |
|------|------------|----------------|-----------|---------|------------------------------------------|
| 1    | 4523       | `count += 1`   | —         | 1       | Counted the digit `3`                    |
|      | 4523       | `n = n // 10`  | 452       | 1       | Stripped last digit (`3`), left with 452 |
| 2    | 452        | `count += 1`   | —         | 2       | Counted the digit `2`                    |
|      | 452        | `n = n // 10`  | 45        | 2       | Stripped last digit (`2`), left with 45  |
| 3    | 45         | `count += 1`   | —         | 3       | Counted the digit `5`                    |
|      | 45         | `n = n // 10`  | 4         | 3       | Stripped last digit (`5`), left with 4   |
| 4    | 4          | `count += 1`   | —         | 4       | Counted the digit `4`                    |
|      | 4          | `n = n // 10`  | 0         | 4       | Stripped last digit (`4`), left with 0   |
| End  | 0          | `while 0 > 0`? | —         | 4       | Condition is False → loop exits          |

**Final Result:** `count = 4` ✓

---

### Dry Run — Edge Case: `n = 0`

| Step | Check          | Result | Explanation                          |
|------|----------------|--------|--------------------------------------|
| 1    | `n == 0`?      | True   | Special case detected                |
| 2    | `return 1`     | 1      | Zero is a single-digit number: `"0"` |

**Final Result:** `1` ✓

---

### Dry Run — Edge Case: `n = -987`

| Step | `n` Before | Operation        | `n` After | `count` | Explanation                       |
|------|------------|------------------|-----------|---------|-----------------------------------|
| Pre  | -987       | `n = abs(-987)`  | 987       | 0       | Strip the negative sign           |
| 1    | 987        | `count += 1`     | —         | 1       | Counted digit `7`                 |
|      | 987        | `n = n // 10`    | 98        | 1       | Stripped `7`                      |
| 2    | 98         | `count += 1`     | —         | 2       | Counted digit `8`                 |
|      | 98         | `n = n // 10`    | 9         | 2       | Stripped `8`                      |
| 3    | 9          | `count += 1`     | —         | 3       | Counted digit `9`                 |
|      | 9          | `n = n // 10`    | 0         | 3       | Stripped `9`                      |
| End  | 0          | `while 0 > 0`?   | —         | 3       | Loop exits                        |

**Final Result:** `3` ✓

---

### Dry Run — Optimized (String Conversion) for `n = 4523`

| Step | Operation              | Result     | Explanation                                  |
|------|------------------------|------------|----------------------------------------------|
| 1    | `abs(4523)`            | `4523`     | No change needed (positive number)           |
| 2    | `str(4523)`            | `"4523"`   | Convert integer to string                    |
| 3    | `len("4523")`          | `4`        | Count characters in the string               |
| End  | `return 4`             | `4`        | Each character is one digit ✓                |

**Final Result:** `4` ✓

---

### Dry Run — Optimized (Logarithm) for `n = 4523`

| Step | Operation                    | Value       | Explanation                                      |
|------|------------------------------|-------------|--------------------------------------------------|
| 1    | `abs(4523)`                  | `4523`      | Positive, no change                              |
| 2    | `math.log10(4523)`           | `3.6552...` | log₁₀(4523) ≈ 3.655                              |
| 3    | `math.floor(3.6552)`         | `3`         | Floor rounds down to the power of 10             |
| 4    | `3 + 1`                      | `4`         | Adding 1 converts the exponent to a digit count  |
| End  | `return 4`                   | `4`         | ✓                                                |

**Why does this work?**
> Any d-digit number n satisfies: `10^(d-1) ≤ n < 10^d`
> Taking log₁₀: `d-1 ≤ log₁₀(n) < d`
> So `floor(log₁₀(n)) = d - 1`, and `floor(log₁₀(n)) + 1 = d`

**Final Result:** `4` ✓

---

## 7. Time & Space Complexity

### Brute Force — Loop Division

| Metric       | Complexity | Reason                                                                                     |
|--------------|------------|--------------------------------------------------------------------------------------------|
| Time         | **O(d)**   | The loop runs exactly `d` times, once per digit. `d = floor(log₁₀(n)) + 1` ≈ `log₁₀(n)` |
| Space        | **O(1)**   | Only two variables used (`n` and `count`), regardless of input size                        |

- **Best case:** O(1) — single digit input, loop runs once
- **Worst case:** O(d) — large number with many digits

---

### Optimized — String Conversion

| Metric       | Complexity | Reason                                                                                   |
|--------------|------------|------------------------------------------------------------------------------------------|
| Time         | **O(d)**   | `str()` must produce a character for each digit → O(d). `len()` is O(1) on Python strings |
| Space        | **O(d)**   | A string of length `d` is allocated in memory to hold the digit characters               |

- Practically fast in Python because string operations are implemented in C under the hood
- The extra **O(d) space** is the trade-off vs. the loop approach

---

### Optimized — Logarithm

| Metric       | Complexity | Reason                                                                                     |
|--------------|------------|--------------------------------------------------------------------------------------------|
| Time         | **O(1)**   | `log10()` and `floor()` are single mathematical operations, independent of digit count    |
| Space        | **O(1)**   | No extra data structures — only a couple of numeric variables                              |

- **Theoretical winner** on complexity
- **Practical caveat:** Python's `math.log10()` uses floating-point arithmetic. For very large numbers (e.g., `10**15 + 1`), floating-point rounding errors can give an off-by-one result
- **Safe rule:** Use `len(str(abs(n)))` for correctness; use `log10` only when n is guaranteed to not be a power of 10 or a boundary case

---

### Summary Table

| Approach            | Time    | Space   | Pros                          | Cons                              |
|---------------------|---------|---------|-------------------------------|-----------------------------------|
| Brute Force (Loop)  | O(d)    | O(1)    | Simple, no libraries needed   | Slower for large d                |
| String Conversion   | O(d)    | O(d)    | Clean, Pythonic, always correct | Slight memory overhead           |
| Logarithm           | O(1)    | O(1)    | Fastest theoretically          | Float precision risk near powers of 10 |

---

## 8. Beginner Tips

### 🔑 Core Hacks & Rules of Thumb

1. **The `// 10` trick is your best friend.**
   Integer division by 10 strips the *rightmost* digit. Division by 100 strips two digits. This is a pattern that appears in many digit-manipulation problems (reverse a number, sum of digits, check palindrome, etc.).

2. **Always handle `n = 0` first.**
   The loop `while n > 0` never executes when `n = 0`, so you'd return `0` — which is wrong. Zero has **one** digit. Always add `if n == 0: return 1` at the top.

3. **Always handle negatives with `abs()`.**
   The minus sign is not a digit. Wrap `n` in `abs()` before any digit-counting logic.

4. **`len(str(abs(n)))` is the Pythonic one-liner.**
   For competitive programming or quick solutions, this single expression handles all cases including zero and negatives. Know it by heart.

5. **Logarithm = Math elegance, but with a trap.**
   `math.floor(math.log10(n)) + 1` works perfectly for most inputs, but can break silently for powers of 10 due to floating-point errors (e.g., `log10(1000)` might return `2.9999...` instead of `3.0`). Use `int(math.log10(n)) + 1` with awareness, or stick to the string method for safety.

---

### ⚠️ Edge Case Reminders

| Scenario             | What Goes Wrong Without a Fix              | Fix                              |
|----------------------|--------------------------------------------|----------------------------------|
| `n = 0`              | Loop skips entirely → returns `0` (wrong)  | `if n == 0: return 1`            |
| `n < 0`              | Division behaves oddly with sign           | `n = abs(n)` before the loop     |
| Very large integers  | `log10` may have float precision errors    | Use `len(str(abs(n)))` instead   |
| Single digit `n`     | Works fine — loop runs once                | No special handling needed       |

---

### 📊 Approach Comparison at a Glance

| When to use...              | Reason                                                          |
|-----------------------------|------------------------------------------------------------------|
| **Loop (Division)**         | When learning fundamentals; no imports needed; builds intuition  |
| **String Conversion**       | When you need quick, correct, readable production code           |
| **Logarithm**               | In math-heavy contexts or when you need O(1) and control inputs  |

---

### 🧠 Patterns This Problem Teaches

This problem is a gateway to many others. Once you understand stripping digits with `// 10`, you can solve:

- **Sum of Digits:** accumulate `n % 10` each iteration instead of a count
- **Reverse a Number:** build a new number from `n % 10` each iteration
- **Palindrome Check:** compare original vs reversed digits
- **Armstrong Number:** check if sum of (each digit)^d == original number
- **Digital Root:** repeatedly sum digits until a single digit remains

> **The loop pattern is always the same — what changes is what you *do* with each digit.**

---

*End of Study Guide — Count Digits in a Number*
