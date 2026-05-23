# Armstrong Number

---

## 1. Name of the Problem

**Armstrong Number (Narcissistic Number)**

Given an integer `n`, determine whether it is an **Armstrong number** — a number that equals the sum of its own digits each raised to the power of the number of digits it contains.

---

## 2. Problem Statement

### What is being solved?

A number with `d` digits is called an **Armstrong number** (also known as a **Narcissistic number** or **Pluperfect number**) if:

```
n = d₁ᵈ + d₂ᵈ + d₃ᵈ + ... + dₙᵈ
```

Where `d₁, d₂, ... dₙ` are its individual digits and `d` is the total count of digits.

> **In plain English:** Raise every digit to the power of *how many digits the number has*, then add them all up. If the sum equals the original number — it's an Armstrong number.

> **Notes:**
> - Every **single-digit number (0–9)** is an Armstrong number because `n¹ = n`.
> - The original code handles only **positive integers** — the refined version also handles zero and negatives.
> - Armstrong numbers are also called **narcissistic numbers** in most competitive programming resources.

---

### Example Input / Output

| Input (`num`) | Digits (`d`) | Calculation                           | Sum  | Armstrong? |
|---------------|--------------|---------------------------------------|------|------------|
| `153`         | 3            | 1³ + 5³ + 3³ = 1 + 125 + 27          | 153  | ✅ Yes      |
| `370`         | 3            | 3³ + 7³ + 0³ = 27 + 343 + 0          | 370  | ✅ Yes      |
| `371`         | 3            | 3³ + 7³ + 1³ = 27 + 343 + 1          | 371  | ✅ Yes      |
| `407`         | 3            | 4³ + 0³ + 7³ = 64 + 0 + 343          | 407  | ✅ Yes      |
| `1634`        | 4            | 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1+1296+81+256   | 1634 | ✅ Yes      |
| `123`         | 3            | 1³ + 2³ + 3³ = 1 + 8 + 27            | 36   | ❌ No       |
| `100`         | 3            | 1³ + 0³ + 0³ = 1 + 0 + 0             | 1    | ❌ No       |
| `5`           | 1            | 5¹                                    | 5    | ✅ Yes      |

---

## 3. Logic Behind the Solution

### Part A — Intuition: How to Think About It

Imagine the number `153`. It has **3 digits**. The question is:

> *"If I raise each digit to the power of 3 (the digit count) and add them all, do I get back 153?"*

```
1³ = 1
5³ = 125
3³ = 27
─────────
Sum = 153  ← equals original ✅ Armstrong!
```

Now try `123`:

```
1³ = 1
2³ = 8
3³ = 27
─────────
Sum = 36  ← does not equal 123 ❌ Not Armstrong
```

The number literally **reconstructs itself** from its own digits raised to the right power. That's why these are called **narcissistic** numbers — they are completely self-referential.

**The key steps in the algorithm:**
1. Count the digits (`d = len(str(num))`)
2. Extract each digit one by one (`digit = temp % 10`)
3. Raise each digit to the power `d` and accumulate (`sum += digit ** d`)
4. Compare the final sum to the original (`sum == num`)

---

### Part B — Approaches

#### Approach 1: Brute Force (String Conversion for Digit Count + Loop)

- Use `len(str(num))` to find the number of digits — simple and readable
- Extract digits one by one with `% 10` and `// 10`
- Accumulate `digit ** order`
- Compare sum to original

#### Approach 2: Optimized (Pure Math — No String Conversion)

- Use `math.log10(num) + 1` floored to compute digit count without strings
- Same loop logic for digit extraction
- Avoids string conversion entirely — purely numeric

#### Approach 3: Pythonic One-Liner (List Comprehension)

- Convert number to string, iterate over each character
- One-line sum using list comprehension
- Most compact form — good for quick checks

#### Edge Cases to Always Handle

| Edge Case          | Expected Behaviour                                                   |
|--------------------|----------------------------------------------------------------------|
| `num < 0`          | Negative numbers are never Armstrong numbers (sign not a digit)      |
| `num == 0`         | `0¹ = 0` → 0 IS an Armstrong number                                  |
| Single digit `1–9` | Always Armstrong: `n¹ = n`                                           |
| `num` with zeros   | `0^d = 0` — handled naturally in the loop                            |

---

## 4. Pseudocode

### Brute Force (String Digit Count + Loop)

```
FUNCTION is_armstrong_brute(num):
    IF num < 0:
        RETURN False             ← negatives are never Armstrong

    order ← number of digits in num   ← len(str(num))
    temp  ← num
    total ← 0

    WHILE temp > 0:
        digit ← temp MOD 10          ← extract last digit
        total ← total + digit^order  ← raise to power of digit count
        temp  ← temp // 10           ← strip last digit

    RETURN (total == num)
```

### Optimized (Pure Math — No String Conversion)

```
FUNCTION is_armstrong_math(num):
    IF num < 0:
        RETURN False

    IF num == 0:
        RETURN True              ← 0^1 = 0

    order ← floor(log10(num)) + 1   ← digit count via logarithm
    temp  ← num
    total ← 0

    WHILE temp > 0:
        digit ← temp MOD 10
        total ← total + digit^order
        temp  ← temp // 10

    RETURN (total == num)
```

### Pythonic One-Liner

```
FUNCTION is_armstrong_pythonic(num):
    IF num < 0:
        RETURN False

    s     ← string of num
    order ← length of s

    RETURN num == sum of (int(ch)^order for each character ch in s)
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Armstrong Number (Narcissistic Number)
  Approach : Brute Force   (String digit count + Loop)
             Optimized     (Pure Math — log10 digit count)
             Pythonic      (List Comprehension one-liner)
  Author   : Study Guide Generator
=============================================================
"""

import math


# ─────────────────────────────────────────────
#  APPROACH 1 — Brute Force (String Count + Loop)
# ─────────────────────────────────────────────

def is_armstrong_brute(num: int) -> bool:
    """
    Check if a number is an Armstrong number using a digit-extraction loop.

    Algorithm:
        1. Count digits using len(str(num)).
        2. Extract each digit with % 10 and accumulate digit^order.
        3. Compare accumulated sum to the original number.

    Args:
        num (int): Any integer.

    Returns:
        bool: True if num is an Armstrong number, False otherwise.

    Time  : O(d) — d = number of digits; loop runs d times
    Space : O(d) — str(num) creates a string of length d
    """
    # Negative numbers are never Armstrong numbers
    if num < 0:
        return False

    # Special case: 0 is an Armstrong number (0^1 = 0)
    if num == 0:
        return True

    order = len(str(num))   # count digits via string conversion
    temp  = num             # working copy; don't mutate original
    total = 0

    while temp > 0:
        digit  = temp % 10          # extract the last digit
        total += digit ** order     # raise to power of digit count
        temp  //= 10                # strip the last digit

    return total == num             # True if sum reconstructs original


# ─────────────────────────────────────────────
#  APPROACH 2 — Optimized (Pure Math, No Strings)
# ─────────────────────────────────────────────

def is_armstrong_math(num: int) -> bool:
    """
    Check if a number is an Armstrong number using log10 for digit count.

    Algorithm:
        1. Use floor(log10(num)) + 1 to count digits without strings.
        2. Same digit-extraction loop as brute force.

    Args:
        num (int): Any integer.

    Returns:
        bool: True if num is an Armstrong number, False otherwise.

    Time  : O(d) — same loop; log10 call is O(1)
    Space : O(1) — no string objects created

    Warning:
        log10 can have floating-point precision issues near powers of 10.
        For competitive use, prefer the brute force string method.
    """
    if num < 0:
        return False

    # log10(0) is undefined; 0 is an Armstrong number by definition
    if num == 0:
        return True

    order = math.floor(math.log10(num)) + 1   # digit count via math
    temp  = num
    total = 0

    while temp > 0:
        digit  = temp % 10
        total += digit ** order
        temp  //= 10

    return total == num


# ─────────────────────────────────────────────
#  APPROACH 3 — Pythonic (List Comprehension)
# ─────────────────────────────────────────────

def is_armstrong_pythonic(num: int) -> bool:
    """
    Check if a number is an Armstrong number using a one-liner comprehension.

    Algorithm:
        Convert num to string, iterate over each character digit,
        raise each to the power of the total digit count, and sum.

    Args:
        num (int): Any integer.

    Returns:
        bool: True if num is an Armstrong number, False otherwise.

    Time  : O(d) — comprehension iterates over all d digit characters
    Space : O(d) — string of length d + list of d values in comprehension
    """
    if num < 0:
        return False

    s     = str(num)
    order = len(s)

    # int(ch) converts each character back to its digit value
    return num == sum(int(ch) ** order for ch in s)


# ─────────────────────────────────────────────
#  BONUS — Find All Armstrong Numbers in a Range
# ─────────────────────────────────────────────

def find_all_armstrongs(start: int, end: int) -> list:
    """
    Return a list of all Armstrong numbers in the range [start, end].

    Args:
        start (int): Range start (inclusive).
        end   (int): Range end   (inclusive).

    Returns:
        list: All Armstrong numbers in the given range.
    """
    return [n for n in range(max(0, start), end + 1)
            if is_armstrong_brute(n)]


# ─────────────────────────────────────────────
#  HELPER — Display result neatly
# ─────────────────────────────────────────────

def display_result(num: int, result: bool, approach: str) -> None:
    """Print the Armstrong check result in a formatted way."""
    verdict = "✅ ARMSTRONG NUMBER" if result else "❌ NOT an Armstrong Number"
    print(f"\n  Number   : {num}")
    print(f"  Approach : {approach}")
    print(f"  Result   : {verdict}")
    print("  " + "─" * 42)


# ─────────────────────────────────────────────
#  MAIN — Menu-Driven Program
# ─────────────────────────────────────────────

def main():
    """
    Menu-driven program to check Armstrong numbers using three approaches,
    with a bonus option to list all Armstrong numbers in a range.
    """
    print("=" * 52)
    print("           ARMSTRONG NUMBER CHECK")
    print("=" * 52)

    # ── Menu ───────────────────────────────────
    print("\nWhat would you like to do?")
    print("  1. Check a single number")
    print("  2. Find all Armstrong numbers in a range")

    while True:
        mode = input("\nYour choice (1–2): ").strip()
        if mode in {"1", "2"}:
            break
        print("  [Error] Enter 1 or 2.")

    # ── Mode 1: Check Single Number ────────────
    if mode == "1":

        while True:
            try:
                num = int(input("\nEnter an integer: "))
                break
            except ValueError:
                print("  [Error] Please enter a valid integer.")

        print("\nChoose an approach:")
        print("  1. Brute Force  — String Digit Count + Loop")
        print("  2. Optimized    — Pure Math (log10 digit count)")
        print("  3. Pythonic     — List Comprehension One-liner")
        print("  4. All          — Run All Three & Compare")

        while True:
            choice = input("\nYour choice (1–4): ").strip()
            if choice in {"1", "2", "3", "4"}:
                break
            print("  [Error] Enter a number between 1 and 4.")

        print()
        if choice == "1":
            result = is_armstrong_brute(num)
            display_result(num, result, "Brute Force (String Count + Loop)")

        elif choice == "2":
            result = is_armstrong_math(num)
            display_result(num, result, "Optimized (Pure Math)")

        elif choice == "3":
            result = is_armstrong_pythonic(num)
            display_result(num, result, "Pythonic (List Comprehension)")

        elif choice == "4":
            r1 = is_armstrong_brute(num)
            r2 = is_armstrong_math(num)
            r3 = is_armstrong_pythonic(num)
            display_result(num, r1, "Brute Force (String Count + Loop)")
            display_result(num, r2, "Optimized (Pure Math)")
            display_result(num, r3, "Pythonic (List Comprehension)")

    # ── Mode 2: Find All in Range ──────────────
    elif mode == "2":

        while True:
            try:
                start = int(input("\nEnter range start: "))
                end   = int(input("Enter range end  : "))
                if start > end:
                    print("  [Error] Start must be ≤ end.")
                    continue
                break
            except ValueError:
                print("  [Error] Please enter valid integers.")

        armstrongs = find_all_armstrongs(start, end)
        print(f"\n  Armstrong numbers between {start} and {end}:")
        if armstrongs:
            print(f"  {armstrongs}")
        else:
            print("  None found in this range.")
        print("  " + "─" * 42)


if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

---

### Dry Run — Brute Force: `num = 153` (Armstrong ✅)

> Pre-processing: `order = len("153") = 3`, `temp = 153`, `total = 0`

| Step | `temp` Before | `digit = temp % 10` | `digit ** order`  | `total` Before | `total` After | `temp` After | Explanation              |
|------|---------------|---------------------|-------------------|----------------|---------------|--------------|--------------------------|
| 1    | 153           | 3                   | 3³ = **27**       | 0              | 27            | 15           | Extracted digit `3`      |
| 2    | 15            | 5                   | 5³ = **125**      | 27             | 152           | 1            | Extracted digit `5`      |
| 3    | 1             | 1                   | 1³ = **1**        | 152            | 153           | 0            | Extracted digit `1`      |
| End  | 0             | —                   | —                 | —              | 153           | —            | Loop exits (`0 > 0` false)|
| ✅   | —             | —                   | —                 | —              | —             | —            | `153 == 153` → **Armstrong** |

**Final Result:** `True` ✅

---

### Dry Run — Brute Force: `num = 370` (Armstrong ✅)

> Pre-processing: `order = len("370") = 3`, `temp = 370`, `total = 0`

| Step | `temp` Before | `digit` | `digit³`       | `total` After | `temp` After | Explanation         |
|------|---------------|---------|----------------|---------------|--------------|---------------------|
| 1    | 370           | 0       | 0³ = **0**     | 0             | 37           | Digit `0` → adds 0  |
| 2    | 37            | 7       | 7³ = **343**   | 343           | 3            | Digit `7`           |
| 3    | 3             | 3       | 3³ = **27**    | 370           | 0            | Digit `3`           |
| End  | 0             | —       | —              | 370           | —            | Loop exits          |
| ✅   | —             | —       | —              | —             | —            | `370 == 370` → **Armstrong** |

**Final Result:** `True` ✅

---

### Dry Run — Brute Force: `num = 123` (Not Armstrong ❌)

> Pre-processing: `order = len("123") = 3`, `temp = 123`, `total = 0`

| Step | `temp` Before | `digit` | `digit³`      | `total` After | `temp` After | Explanation         |
|------|---------------|---------|---------------|---------------|--------------|---------------------|
| 1    | 123           | 3       | 3³ = **27**   | 27            | 12           | Digit `3`           |
| 2    | 12            | 2       | 2³ = **8**    | 35            | 1            | Digit `2`           |
| 3    | 1             | 1       | 1³ = **1**    | 36            | 0            | Digit `1`           |
| End  | 0             | —       | —             | 36            | —            | Loop exits          |
| ❌   | —             | —       | —             | —             | —            | `36 ≠ 123` → **Not Armstrong** |

**Final Result:** `False` ❌

---

### Dry Run — Brute Force: `num = 1634` (4-digit Armstrong ✅)

> Pre-processing: `order = len("1634") = 4`, `temp = 1634`, `total = 0`

| Step | `temp` Before | `digit` | `digit⁴`           | `total` After | `temp` After | Explanation    |
|------|---------------|---------|--------------------|---------------|--------------|----------------|
| 1    | 1634          | 4       | 4⁴ = **256**       | 256           | 163          | Digit `4`      |
| 2    | 163           | 3       | 3⁴ = **81**        | 337           | 16           | Digit `3`      |
| 3    | 16            | 6       | 6⁴ = **1296**      | 1633          | 1            | Digit `6`      |
| 4    | 1             | 1       | 1⁴ = **1**         | 1634          | 0            | Digit `1`      |
| End  | 0             | —       | —                  | 1634          | —            | Loop exits     |
| ✅   | —             | —       | —                  | —             | —            | `1634 == 1634` → **Armstrong** |

**Final Result:** `True` ✅

---

### Dry Run — Pythonic One-liner: `num = 153`

| Step | Operation                            | Value              | Explanation                             |
|------|--------------------------------------|--------------------|-----------------------------------------|
| 1    | `s = str(153)`                       | `"153"`            | Convert number to string                |
| 2    | `order = len("153")`                 | `3`                | Count characters = digit count          |
| 3    | `int('1') ** 3`                      | `1`                | First character raised to power 3       |
| 4    | `int('5') ** 3`                      | `125`              | Second character raised to power 3      |
| 5    | `int('3') ** 3`                      | `27`               | Third character raised to power 3       |
| 6    | `sum([1, 125, 27])`                  | `153`              | Add all powered digits                  |
| 7    | `153 == 153`                         | `True`             | Sum equals original → Armstrong ✅      |

**Final Result:** `True` ✅

---

### Dry Run — Edge Cases Summary

| Input  | `order` | Calculation           | `total` | `total == num`? | Result |
|--------|---------|----------------------|---------|-----------------|--------|
| `0`    | —       | Early return `True`  | —       | —               | ✅     |
| `5`    | 1       | 5¹ = 5               | 5       | 5 == 5 ✅       | ✅     |
| `-153` | —       | Early return `False` | —       | —               | ❌     |
| `100`  | 3       | 1³+0³+0³ = 1         | 1       | 1 ≠ 100 ❌      | ❌     |
| `407`  | 3       | 4³+0³+7³ = 64+0+343  | 407     | 407 == 407 ✅   | ✅     |

---

## 7. Time & Space Complexity

### Approach 1 — Brute Force (String Count + Loop)

| Metric | Complexity | Reason                                                                           |
|--------|------------|----------------------------------------------------------------------------------|
| Time   | **O(d)**   | `len(str(num))` is O(d); the while loop runs exactly `d` times — once per digit  |
| Space  | **O(d)**   | `str(num)` allocates a string of length `d` in memory                            |

---

### Approach 2 — Optimized (Pure Math)

| Metric | Complexity | Reason                                                                            |
|--------|------------|-----------------------------------------------------------------------------------|
| Time   | **O(d)**   | `math.log10` + `math.floor` are O(1); the loop still runs `d` times              |
| Space  | **O(1)**   | No string created — only scalar variables (`order`, `temp`, `total`, `digit`)     |

- The loop dominates both approaches equally — the only real difference is memory: O(d) vs O(1)

---

### Approach 3 — Pythonic (List Comprehension)

| Metric | Complexity | Reason                                                                              |
|--------|------------|-------------------------------------------------------------------------------------|
| Time   | **O(d)**   | The generator expression iterates over all `d` characters of the string             |
| Space  | **O(d)**   | The string `s` of length `d` is created; generator is lazy so no intermediate list  |

---

### Summary Table

| Approach              | Time  | Space  | Best For                                           |
|-----------------------|-------|--------|----------------------------------------------------|
| Brute Force (Loop)    | O(d)  | O(d)   | Learning the algorithm; most readable              |
| Optimized (Math)      | O(d)  | O(1)   | Memory-sensitive contexts; no strings allowed      |
| Pythonic (Comprehension)| O(d)| O(d)   | Concise code; Python-specific solutions            |

> **All three approaches are O(d) in time** — the digit-extraction loop is the bottleneck in every case, and there is no way to avoid visiting each digit at least once. The differences only show up in **space**.

> **Note on `d`:** For a number `n`, `d = floor(log₁₀(n)) + 1 ≈ log₁₀(n)`. So O(d) = O(log n) in terms of the input value `n`. Armstrong checking is extremely fast even for very large numbers.

---

## 8. Beginner Tips

### 🔑 Core Hacks & Rules of Thumb

1. **`order = len(str(num))` is the cleanest way to count digits.**
   Always compute the digit count *once* before the loop and store it — don't recompute it inside the loop. The power never changes; only the digit changes each iteration.

2. **Never use `sum` as a variable name in Python.**
   The original code uses `sum` as a variable — this shadows Python's built-in `sum()` function and can cause subtle bugs if you try to use it later in the same program. Always use `total`, `digit_sum`, or `armstrong_sum` instead.

3. **Every single-digit number (0–9) is trivially an Armstrong number.**
   `n¹ = n` for any single-digit `n`. This is a useful quick sanity check for your function — if it returns `False` for any digit 0–9, something is broken.

4. **The four 3-digit Armstrong numbers are worth memorising.**
   `153`, `370`, `371`, `407` — these are the canonical test cases used in almost every textbook, interview, and competitive programming problem involving Armstrong numbers. Know them by heart.

5. **`digit ** order` is the expensive operation — be aware of it.**
   For large numbers with many digits, exponentiation (`**`) is more costly than addition or modulo. In Python it is handled gracefully, but in lower-level languages this matters. For `d`-digit numbers, each `digit^d` grows fast: `9^10 = 3,486,784,401`.

6. **Pythonic comprehension is compact but harder to debug.**
   `num == sum(int(ch) ** order for ch in str(num))` is elegant, but if something goes wrong, you can't step through it easily. In an exam or interview, write the explicit loop — it shows your understanding better.

7. **Shadow variable trick: use `temp`, never mutate `num`.**
   The loop strips digits from `temp`, not from `num`. This preserves `num` for the final comparison `total == num`. If you accidentally write `while num > 0` and strip digits from `num`, you'll be comparing `total` to `0` at the end — always wrong.

---

### ⚠️ Edge Case Reminders

| Scenario              | Trap                                               | Safe Handling                               |
|-----------------------|----------------------------------------------------|---------------------------------------------|
| `num < 0`             | `len(str(-153)) = 4` (includes the `-` sign)       | Return `False` immediately for negatives    |
| `num == 0`            | `log10(0)` is undefined; loop skips → `total=0`   | Return `True` early (0¹ = 0)                |
| Single digits `1–9`   | Work fine — loop runs once, `digit^1 = digit`      | No special handling needed                  |
| Digit is `0`          | `0^d = 0` for any `d > 0` — contributes 0         | Handled naturally in the loop               |
| Using `sum` as name   | Shadows Python's built-in `sum()` function         | Rename to `total` or `digit_sum`            |
| Not saving `num` copy | Loop destroys `num`; final comparison uses 0       | Always use `temp = num` before the loop     |

---

### 📊 Known Armstrong Numbers for Quick Testing

| Digits | Armstrong Numbers                                     |
|--------|-------------------------------------------------------|
| 1      | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9                        |
| 2      | None — no 2-digit Armstrong numbers exist             |
| 3      | **153, 370, 371, 407**                                |
| 4      | **1634, 8208, 9474**                                  |
| 5      | **54748, 92727, 93084**                               |
| 6      | **548834**                                            |
| 7      | **1741725, 4210818, 9800817, 9926315**                |

> **Why are there no 2-digit Armstrong numbers?**
> For a 2-digit number `n = 10a + b`, we need `a² + b² = 10a + b`.
> Checking all pairs (10–99) — none satisfy this. The gap between linear growth and quadratic growth makes it impossible.

---

### 🧠 How This Problem Connects to Others

| Problem / Concept            | Connection                                                                       |
|------------------------------|----------------------------------------------------------------------------------|
| **Count Digits**             | Direct prerequisite — `order = len(str(num))` is the digit count problem         |
| **Sum of Digits**            | Same loop structure — accumulate `digit` instead of `digit^order`                |
| **Reverse a Number**         | Same `% 10` + `// 10` skeleton — change what you do with the extracted digit     |
| **Perfect Number**           | Similar self-referential check — does sum of *divisors* equal the number?        |
| **Happy Number**             | Repeatedly sum squared digits — shares the "sum of powered digits" core idea     |
| **Power Function**           | `digit ** order` — understanding `**` and how to implement it manually           |
| **Find All in Range**        | Armstrong check inside a loop — the bonus function in the refined code above     |

> **The universal digit-loop skeleton — now with powers:**
>
> ```
> temp = num
> while temp > 0:
>     digit = temp % 10
>     # ← THIS LINE defines the problem:
>     #   count digits    → count += 1
>     #   sum of digits   → total += digit
>     #   reverse number  → reverse = reverse*10 + digit
>     #   Armstrong check → total += digit ** order
>     temp //= 10
> ```
>
> Every digit-manipulation problem uses this same skeleton. **Only the operation inside changes.**

---

*End of Study Guide — Armstrong Number*
