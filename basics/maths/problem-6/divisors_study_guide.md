# 🔢 Finding All Divisors of a Number

---

## 1. Name of the Problem

**Finding All Divisors of a Number**

> Also known as: *"Print all factors of N"* — a classic number theory problem that appears frequently in beginner-to-intermediate competitive programming.

---

## 2. Problem Statement

### What the Code Solves

Given a positive integer `n`, find and print **all divisors** (also called factors) of that number.

A divisor of `n` is any integer `d` such that `n % d == 0` — meaning `d` divides `n` with no remainder.

---

### Formal Definition

```
Input  : A positive integer n
Output : All integers i in the range [1, n] such that n % i == 0
```

---

### Example 1

```
Input  : n = 12
Output : 1 2 3 4 6 12
```

**Why?**
- 12 ÷ 1  = 12  → remainder 0 ✅
- 12 ÷ 2  = 6   → remainder 0 ✅
- 12 ÷ 3  = 4   → remainder 0 ✅
- 12 ÷ 4  = 3   → remainder 0 ✅
- 12 ÷ 5  = 2.4 → remainder 2 ❌
- 12 ÷ 6  = 2   → remainder 0 ✅
- 12 ÷ 7…11     → remainders ≠ 0 ❌
- 12 ÷ 12 = 1   → remainder 0 ✅

---

### Example 2

```
Input  : n = 7
Output : 1 7
```

> 7 is a **prime number** — it has exactly 2 divisors: 1 and itself.

---

### Example 3

```
Input  : n = 1
Output : 1
```

> 1's only divisor is itself.

---

## 3. Logic Behind the Solution

### Part A — Intuition

The core idea is simple: **try every candidate** from 1 to n and check whether it divides n evenly.

Think of it like a sieve:

```
n = 12

Candidates:   1   2   3   4   5   6   7   8   9  10  11  12
Divides 12?   ✅  ✅  ✅  ✅  ❌  ✅  ❌  ❌  ❌  ❌  ❌  ✅
```

**Key insight for the optimised approach**: Divisors always come in *pairs*. If `d` divides `n`, then `n/d` also divides `n`. So you only need to search up to `√n` — every divisor ≤ √n has a partner divisor ≥ √n.

```
n = 36,  √36 = 6

Pair:  (1, 36)   (2, 18)   (3, 12)   (4, 9)   (6, 6←perfect square root)
       d  n/d     d  n/d    d  n/d    d  n/d    d = n/d → count once
```

---

### Part B — Approaches

| Approach    | Strategy                                    | Time       | Space  |
|-------------|---------------------------------------------|------------|--------|
| Brute Force | Loop from 1 to n, check every number        | O(n)       | O(1)   |
| Optimised   | Loop from 1 to √n, collect both pair values | O(√n)      | O(√n)  |

**Edge Cases to Handle**
- `n = 0` → mathematically undefined (every number divides 0); skip or reject.
- `n < 0` → negative numbers; you can either reject or work with absolute value.
- `n = 1` → only one divisor: `1`.
- Very large `n` → brute force becomes slow; optimised is essential.

---

## 4. Pseudocode

### Brute Force

```
FUNCTION brute_force_divisors(n):
    IF n <= 0:
        PRINT "Invalid input"
        RETURN

    divisors = []
    FOR i FROM 1 TO n (inclusive):
        IF n MOD i == 0:
            APPEND i TO divisors

    PRINT divisors
```

---

### Optimised (√n approach)

```
FUNCTION optimised_divisors(n):
    IF n <= 0:
        PRINT "Invalid input"
        RETURN

    small = []   # divisors ≤ √n
    large = []   # their paired divisors > √n

    FOR i FROM 1 TO floor(√n) (inclusive):
        IF n MOD i == 0:
            APPEND i TO small
            IF i != n / i:            # avoid counting perfect-square root twice
                APPEND n / i TO large

    large = REVERSE(large)            # sort descending → ascending when combined
    PRINT small + large
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Finding All Divisors of a Number
  Approach : Brute Force  → O(n)
             Optimised    → O(√n)
  Author   : Study Notes
=============================================================
"""

import math


# ─────────────────────────────────────────────────────────────
# HELPER — Input validation
# ─────────────────────────────────────────────────────────────

def get_positive_integer(prompt: str) -> int:
    """
    Repeatedly prompt until the user enters a positive integer.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        int: A validated positive integer (>= 1).
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("  ⚠  Please enter a positive integer (>= 1).\n")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number.\n")


# ─────────────────────────────────────────────────────────────
# APPROACH 1 — Brute Force  O(n)
# ─────────────────────────────────────────────────────────────

def brute_force_divisors(n: int) -> list[int]:
    """
    Find all divisors of n by checking every integer from 1 to n.

    Strategy:
        For each candidate i in [1, n], if n % i == 0, i is a divisor.

    Args:
        n (int): The number whose divisors are required (n >= 1).

    Returns:
        list[int]: Sorted list of all divisors of n.

    Time  Complexity: O(n)   — we iterate through all n candidates.
    Space Complexity: O(d)   — where d is the number of divisors (output storage).
    """
    divisors = []

    for i in range(1, n + 1):          # check every candidate from 1 to n
        if n % i == 0:                 # remainder 0 → i divides n exactly
            divisors.append(i)

    return divisors


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Optimised  O(√n)
# ─────────────────────────────────────────────────────────────

def optimised_divisors(n: int) -> list[int]:
    """
    Find all divisors of n by exploiting the paired-divisor property.

    Key Insight:
        If i divides n, then (n // i) also divides n.
        Both form a pair (i, n//i).
        We only need to search i in [1, √n] and collect both values of each pair.
        Special case: when i == n // i (i.e., i = √n exactly), count only once.

    Args:
        n (int): The number whose divisors are required (n >= 1).

    Returns:
        list[int]: Sorted list of all divisors of n.

    Time  Complexity: O(√n)  — loop runs up to √n iterations.
    Space Complexity: O(d)   — where d is the number of divisors (output storage).
    """
    small = []   # divisors in [1, √n]
    large = []   # their paired counterparts in (√n, n]

    for i in range(1, int(math.isqrt(n)) + 1):   # iterate from 1 to √n (inclusive)
        if n % i == 0:                             # i is a divisor
            small.append(i)                        # always collect the smaller of the pair

            pair = n // i
            if pair != i:                          # avoid duplicating perfect-square root
                large.append(pair)                 # collect the larger paired divisor

    # large was collected in ascending order of i → descending order of n//i
    # reverse it so the final merged list stays sorted ascending
    large.reverse()

    return small + large


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(n: int, divisors: list[int], label: str) -> None:
    """
    Pretty-print the divisors result.

    Args:
        n        (int)       : The original number.
        divisors (list[int]) : The computed list of divisors.
        label    (str)       : Approach label for display.
    """
    print(f"\n  [{label}]")
    print(f"  Divisors of {n}: {divisors}")
    print(f"  Total divisors  : {len(divisors)}")

    # Extra info
    if len(divisors) == 2:
        print(f"  Note: {n} is a PRIME number (exactly 2 divisors).")
    elif len(divisors) == 1:
        print(f"  Note: {n} == 1, its only divisor is itself.")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to find divisors of a number.

    Options:
        1 → Brute Force  (O(n))
        2 → Optimised    (O(√n))
        3 → Both side by side
        4 → Exit
    """
    print("=" * 50)
    print("   DIVISORS OF A NUMBER — Study Program")
    print("=" * 50)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force  — O(n)")
        print("  [2] Optimised    — O(√n)")
        print("  [3] Both         — Compare side by side")
        print("  [4] Exit")
        print("-" * 50)

        choice = input("  Enter choice (1/2/3/4): ").strip()

        if choice == "4":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, or 4.\n")
            continue

        # ── Get input ─────────────────────────────────────
        n = get_positive_integer("\n  Enter a positive integer n: ")

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = brute_force_divisors(n)
            display_result(n, result, "Brute Force — O(n)")

        elif choice == "2":
            result = optimised_divisors(n)
            display_result(n, result, "Optimised — O(√n)")

        elif choice == "3":
            bf_result  = brute_force_divisors(n)
            opt_result = optimised_divisors(n)
            display_result(n, bf_result,  "Brute Force — O(n)")
            display_result(n, opt_result, "Optimised  — O(√n)")

            # Sanity check — both should produce identical output
            match = "✅ Match" if bf_result == opt_result else "❌ Mismatch!"
            print(f"\n  Consistency check : {match}")

        print()   # blank line before next menu


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

We use **n = 12** as the example for both approaches.

---

### Brute Force Dry Run — n = 12

| Step | i  | Operation   | n % i | Divisor Found? | Divisors List So Far   |
|------|----|-------------|-------|----------------|------------------------|
| 1    | 1  | 12 % 1 = 0  | 0     | ✅ Yes          | [1]                    |
| 2    | 2  | 12 % 2 = 0  | 0     | ✅ Yes          | [1, 2]                 |
| 3    | 3  | 12 % 3 = 0  | 0     | ✅ Yes          | [1, 2, 3]              |
| 4    | 4  | 12 % 4 = 0  | 0     | ✅ Yes          | [1, 2, 3, 4]           |
| 5    | 5  | 12 % 5 = 2  | 2     | ❌ No           | [1, 2, 3, 4]           |
| 6    | 6  | 12 % 6 = 0  | 0     | ✅ Yes          | [1, 2, 3, 4, 6]        |
| 7    | 7  | 12 % 7 = 5  | 5     | ❌ No           | [1, 2, 3, 4, 6]        |
| 8    | 8  | 12 % 8 = 4  | 4     | ❌ No           | [1, 2, 3, 4, 6]        |
| 9    | 9  | 12 % 9 = 3  | 3     | ❌ No           | [1, 2, 3, 4, 6]        |
| 10   | 10 | 12 % 10 = 2 | 2     | ❌ No           | [1, 2, 3, 4, 6]        |
| 11   | 11 | 12 % 11 = 1 | 1     | ❌ No           | [1, 2, 3, 4, 6]        |
| 12   | 12 | 12 % 12 = 0 | 0     | ✅ Yes          | [1, 2, 3, 4, 6, 12]    |

> **Loop ran 12 iterations.** Final answer: `[1, 2, 3, 4, 6, 12]`

---

### Optimised Dry Run — n = 12

**√12 ≈ 3.46 → loop runs i from 1 to 3**

#### Collection Phase

| Step | i | Operation    | n % i | i Divisor? | pair = n//i | pair == i? | small List   | large List   |
|------|----|-------------|-------|------------|-------------|------------|--------------|--------------|
| 1    | 1  | 12 % 1 = 0  | 0     | ✅ Yes      | 12          | No (12≠1)  | [1]          | [12]         |
| 2    | 2  | 12 % 2 = 0  | 0     | ✅ Yes      | 6           | No (6≠2)   | [1, 2]       | [12, 6]      |
| 3    | 3  | 12 % 3 = 0  | 0     | ✅ Yes      | 4           | No (4≠3)   | [1, 2, 3]    | [12, 6, 4]   |

#### Merge Phase

| Operation              | Result                     |
|------------------------|----------------------------|
| `large.reverse()`      | [4, 6, 12]                 |
| `small + large`        | [1, 2, 3, 4, 6, 12]        |

> **Loop ran only 3 iterations** (vs 12 for brute force). Final answer: `[1, 2, 3, 4, 6, 12]` ✅

---

### Perfect Square Edge Case — n = 36, √36 = 6

| Step | i | n % i | pair = n//i | pair == i? | Action                        |
|------|---|-------|-------------|------------|-------------------------------|
| 1    | 1 | 0     | 36          | No         | Add both: small=[1], large=[36]   |
| 2    | 2 | 0     | 18          | No         | Add both: small=[1,2], large=[36,18] |
| 3    | 3 | 0     | 12          | No         | Add both: small=[1,2,3], large=[36,18,12] |
| 4    | 4 | 0     | 9           | No         | Add both: small=[1,2,3,4], large=[36,18,12,9] |
| 5    | 5 | 36%5=1| —           | —          | Not a divisor, skip           |
| 6    | 6 | 0     | 6           | **Yes ✅**  | Add only to small (no duplicate): small=[1,2,3,4,6] |

> After `large.reverse()` → [9, 12, 18, 36]
> Final: [1, 2, 3, 4, 6] + [9, 12, 18, 36] = `[1, 2, 3, 4, 6, 9, 12, 18, 36]` ✅

---

## 7. Time & Space Complexity

### Brute Force

| Case         | Time Complexity | Explanation                                                                 |
|--------------|-----------------|-----------------------------------------------------------------------------|
| Best Case    | O(n)            | Even if n = 1 (only 1 iteration), the loop structure is still defined by n  |
| Worst Case   | O(n)            | We always iterate from 1 to n — all n candidates are checked               |
| Average Case | O(n)            | There's no early exit; every iteration runs regardless of divisor count     |

| Space Complexity | O(d) | We store d divisors in the output list. In the worst case (highly composite numbers), d can grow, but it's always much smaller than n. The loop itself uses O(1) extra space. |
|---|---|---|

---

### Optimised (√n approach)

| Case         | Time Complexity | Explanation                                                                              |
|--------------|-----------------|------------------------------------------------------------------------------------------|
| Best Case    | O(√n)           | Loop always runs from 1 to floor(√n); no early exit exists                              |
| Worst Case   | O(√n)           | Even for primes (fewest divisors), the full √n iterations still execute                 |
| Average Case | O(√n)           | Consistently √n iterations regardless of the divisor density of n                       |

| Space Complexity | O(d) | Two lists (`small` and `large`) together store all d divisors. The algorithm itself uses O(1) extra working space (just the loop variable i and pair). |
|---|---|---|

---

### Comparison at a Glance

| n           | Brute Force (n iters) | Optimised (√n iters) | Speed-up factor |
|-------------|----------------------|----------------------|-----------------|
| 100         | 100                  | 10                   | 10×             |
| 10,000      | 10,000               | 100                  | 100×            |
| 1,000,000   | 1,000,000            | 1,000                | 1,000×          |
| 1,000,000,000 | 1,000,000,000      | 31,623               | ~31,623×        |

> The optimised approach becomes **exponentially faster** as n grows.

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Divisors come in pairs**: If `d` divides `n`, so does `n/d`. Never scan past `√n`.
2. **Perfect squares**: When `i == n // i` (e.g., i=6, n=36), add `i` only once to avoid duplicating.
3. **The modulo operator `%` is your best friend**: `n % i == 0` is the only test you need to decide divisibility.
4. **1 and n are always divisors** of any positive integer n — you can hard-code them and search only [2, √n] for others if needed.

---

### ⚠️ Edge Case Reminders

| Edge Case      | Brute Force Behaviour       | Optimised Behaviour         | What To Do                          |
|----------------|-----------------------------|-----------------------------|-------------------------------------|
| `n = 1`        | Outputs [1]; loop runs once | √1 = 1; i=1 → pair=1==i → outputs [1] | Both handle correctly ✅           |
| `n = prime`    | Outputs [1, n]; runs n times| Outputs [1, n]; runs √n times | Works correctly in both ✅         |
| `n = 0`        | `range(1, 1)` is empty → no output | `range(1, 1)` → no output | Validate input; 0 has no proper divisors |
| `n < 0`        | Loop doesn't run (range issue) | Same | Always validate: reject or use `abs(n)` |
| Large n (10⁹)  | Extremely slow (~10⁹ iters)  | Fast (~31,623 iters)        | Always use optimised for large n     |

---

### ⚖️ When To Use Which Approach

| Situation                               | Recommended Approach     |
|-----------------------------------------|--------------------------|
| Learning / understanding the concept    | Brute Force first        |
| n is small (n < 10,000)                 | Either works             |
| n is large (n > 10,000)                 | Always use Optimised     |
| Competitive programming / interviews    | Always use Optimised     |
| Need sorted output immediately          | Brute Force (naturally sorted); Optimised needs the merge step |

---

### 📏 Rules of Thumb

- **Always validate input** before running any loop — prevents silent bugs.
- **`math.isqrt(n)`** is safer than `int(n**0.5)` for integer square roots — floating-point errors in `**0.5` can cause off-by-one mistakes for perfect squares.
  ```python
  # ❌ Risky for large perfect squares
  int(36**0.5)   # → 5 sometimes due to floating point
  
  # ✅ Always correct
  math.isqrt(36) # → 6 guaranteed
  ```
- **O(√n) is a red flag to recognise**: Whenever a problem involves factors, primes, or divisibility — think `√n` immediately.
- **The number of divisors** of n is denoted `d(n)` or `τ(n)` (tau function). For most numbers it's tiny (O(n^ε) for any ε > 0) — but knowing this helps set expectations.

---

### 🔗 Related Problems to Practice Next

| Problem                            | Key Concept                         |
|------------------------------------|-------------------------------------|
| Check if a number is prime         | Uses the same √n loop               |
| Find the sum of divisors           | Accumulate `i + n//i` inside the loop |
| Count divisors of numbers 1 to N   | Sieve of Eratosthenes               |
| Largest prime factor               | Divide out factors iteratively      |
| GCD / LCM                          | Built on divisibility               |
| Aggressive Cows (Binary Search)    | Binary search on answer             |

---

*End of Study Notes — Divisors of a Number*
