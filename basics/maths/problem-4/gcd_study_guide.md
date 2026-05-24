# GCD of Two Numbers (Euclidean Algorithm)

---

## 1. Name of the Problem

**Greatest Common Divisor (GCD) — Euclidean Algorithm**

Given two integers `a` and `b`, find the largest positive integer that divides both of them without leaving a remainder.

---

## 2. Problem Statement

### What is being solved?

Given two non-negative integers `a` and `b`, compute their **Greatest Common Divisor (GCD)** — the largest number that evenly divides both `a` and `b`.

> **Key Definitions:**
> - **Divisor:** A number that divides another number with zero remainder.
> - **Common Divisor:** A number that divides *both* `a` and `b`.
> - **Greatest Common Divisor:** The *largest* such common divisor.
> - Also known as **HCF** (Highest Common Factor) in some curricula.

> **Notes:**
> - `GCD(a, 0) = a` — any number is a divisor of zero, so the GCD is `a` itself.
> - `GCD(0, 0)` is mathematically undefined; the refined code handles it explicitly.
> - Negative inputs: GCD is always a positive value; we use `abs()` before processing.

---

### Example Input / Output

| Input `a` | Input `b` | GCD | Explanation                                              |
|-----------|-----------|-----|----------------------------------------------------------|
| `12`      | `8`       | `4` | Divisors of 12: 1,2,3,4,6,12 — of 8: 1,2,4,8 → max = 4 |
| `48`      | `18`      | `6` | Divisors common to both: 1,2,3,6 → max = 6              |
| `100`     | `75`      | `25`| 25 divides both 100 and 75 exactly                       |
| `7`       | `5`       | `1` | 7 and 5 are coprime — only common divisor is 1           |
| `0`       | `5`       | `5` | GCD(0, 5) = 5 by definition                              |
| `9`       | `9`       | `9` | A number is always a divisor of itself                   |
| `-12`     | `8`       | `4` | Sign is ignored; GCD is always positive                  |

---

## 3. Logic Behind the Solution

### Part A — Intuition: How to Think About It

**Why does dividing work?**

The core insight of the Euclidean Algorithm is this beautiful mathematical truth:

> **GCD(a, b) = GCD(b, a % b)**

Why is this true? Because any number that divides both `a` and `b` also divides `a % b` (the remainder). And any number that divides both `b` and `a % b` also divides `a`. So the set of common divisors is *identical* on both sides — meaning the GCD is preserved across every step.

**Visualising with `a = 48`, `b = 18`:**

Think of it as repeatedly asking:
> *"What's left over after fitting `b` into `a` as many times as possible?"*

```
GCD(48, 18)
  → 48 = 2 × 18 + 12    remainder is 12 → GCD(18, 12)
  → 18 = 1 × 12 + 6     remainder is 6  → GCD(12, 6)
  → 12 = 2 × 6  + 0     remainder is 0  → GCD(6, 0) = 6
```

When the remainder hits **zero**, the current value of `b` IS the GCD.

**Why stop at zero?**
Zero has every positive integer as a divisor. So when `b = 0`, the GCD of `(a, 0)` is simply `a` — there's nothing left to reduce.

---

### Part B — Approaches

#### Approach 1: Brute Force (Check All Common Divisors)

- Iterate from `1` to `min(a, b)`
- Track the largest number that divides both `a` and `b`
- **Time complexity is high** — checks every candidate divisor

#### Approach 2: Euclidean Algorithm — Iterative (The code given)

- Repeatedly replace `(a, b)` with `(b, a % b)` until `b == 0`
- When `b == 0`, `a` holds the GCD
- Elegant, fast, and ancient — first described by Euclid (~300 BC)

#### Approach 3: Euclidean Algorithm — Recursive

- Same logic as Approach 2, expressed as a recursive function
- Base case: `gcd(a, 0) = a`
- Recursive case: `gcd(a, b) = gcd(b, a % b)`

#### Approach 4: Built-in (Python `math.gcd`)

- Python's standard library provides `math.gcd(a, b)` — internally optimised
- Useful to know for production code, but not acceptable in interviews

#### Edge Cases to Always Handle

| Edge Case        | Expected Behaviour                          |
|------------------|---------------------------------------------|
| `a = 0, b = 0`   | Undefined — return `0` or raise an error    |
| `a = 0` or `b = 0` | `GCD(0, x) = x`                          |
| Either input negative | Take `abs()` — GCD is always positive  |
| `a == b`         | `GCD(a, a) = a`                             |
| Coprime inputs   | GCD = `1` (e.g., 7 and 5)                   |

---

## 4. Pseudocode

### Brute Force (Check All Divisors)

```
FUNCTION gcd_brute(a, b):
    a ← absolute value of a
    b ← absolute value of b

    IF a == 0 AND b == 0:
        RETURN 0   ← undefined case

    gcd ← 1
    FOR i FROM 1 TO min(a, b) INCLUSIVE:
        IF a MOD i == 0 AND b MOD i == 0:
            gcd ← i    ← update whenever a larger common divisor found

    RETURN gcd
```

### Euclidean Algorithm — Iterative

```
FUNCTION gcd_euclidean_iterative(a, b):
    a ← absolute value of a
    b ← absolute value of b

    WHILE b != 0:
        temp ← b
        b    ← a MOD b    ← remainder becomes new b
        a    ← temp       ← old b becomes new a

    RETURN a   ← when b == 0, a holds the GCD
```

### Euclidean Algorithm — Recursive

```
FUNCTION gcd_euclidean_recursive(a, b):
    IF b == 0:
        RETURN a                           ← base case

    RETURN gcd_euclidean_recursive(b, a MOD b)   ← recursive case
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : GCD of Two Numbers
  Approach : Brute Force (All Divisors)
             Euclidean Algorithm — Iterative
             Euclidean Algorithm — Recursive
             Built-in (math.gcd)
  Author   : Study Guide Generator
=============================================================
"""

import math


# ─────────────────────────────────────────────
#  APPROACH 1 — Brute Force (Check All Divisors)
# ─────────────────────────────────────────────

def gcd_brute(a: int, b: int) -> int:
    """
    Find GCD by checking every integer from 1 to min(a, b).

    Algorithm:
        Iterate through all candidates and track the largest
        number that divides both a and b without a remainder.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: GCD of a and b.

    Time  : O(min(a, b)) — scans every candidate divisor
    Space : O(1)
    """
    a, b = abs(a), abs(b)

    # Edge case: GCD(0, 0) is undefined
    if a == 0 and b == 0:
        print("  [Warning] GCD(0, 0) is undefined. Returning 0.")
        return 0

    # GCD(0, x) = x
    if a == 0:
        return b
    if b == 0:
        return a

    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:  # i divides both a and b
            gcd = i                     # update to the larger common divisor

    return gcd


# ─────────────────────────────────────────────
#  APPROACH 2 — Euclidean Algorithm (Iterative)
# ─────────────────────────────────────────────

def gcd_iterative(a: int, b: int) -> int:
    """
    Find GCD using the iterative Euclidean Algorithm.

    Core principle:
        GCD(a, b) == GCD(b, a % b)
        When b reaches 0, a holds the GCD.

    Algorithm:
        Repeatedly replace (a, b) with (b, a % b)
        until b becomes 0.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: GCD of a and b.

    Time  : O(log(min(a, b))) — number of steps bounded by Fibonacci sequence
    Space : O(1)
    """
    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("  [Warning] GCD(0, 0) is undefined. Returning 0.")
        return 0

    while b != 0:
        temp = b        # save b before overwriting
        b    = a % b    # remainder: next value of b
        a    = temp     # old b becomes new a

    return a            # when b == 0, a is the GCD


# ─────────────────────────────────────────────
#  APPROACH 3 — Euclidean Algorithm (Recursive)
# ─────────────────────────────────────────────

def gcd_recursive(a: int, b: int) -> int:
    """
    Find GCD using the recursive Euclidean Algorithm.

    Base case    : GCD(a, 0) = a
    Recursive case: GCD(a, b) = GCD(b, a % b)

    Args:
        a (int): First integer (non-negative for recursion; handled at call site).
        b (int): Second integer (non-negative).

    Returns:
        int: GCD of a and b.

    Time  : O(log(min(a, b)))
    Space : O(log(min(a, b))) — recursive call stack depth
    """
    if b == 0:
        return a                          # base case: GCD found
    return gcd_recursive(b, a % b)       # recursive case


def gcd_recursive_safe(a: int, b: int) -> int:
    """Wrapper that handles negatives and the (0,0) edge case."""
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        print("  [Warning] GCD(0, 0) is undefined. Returning 0.")
        return 0
    return gcd_recursive(a, b)


# ─────────────────────────────────────────────
#  APPROACH 4 — Built-in (math.gcd)
# ─────────────────────────────────────────────

def gcd_builtin(a: int, b: int) -> int:
    """
    Find GCD using Python's built-in math.gcd().

    Notes:
        - math.gcd() always returns a non-negative integer.
        - In Python 3.9+, math.gcd() accepts more than two arguments.
        - Not acceptable in interviews, but useful in production code.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: GCD of a and b.

    Time  : O(log(min(a, b))) internally
    Space : O(1)
    """
    return math.gcd(abs(a), abs(b))


# ─────────────────────────────────────────────
#  HELPER — Display result neatly
# ─────────────────────────────────────────────

def display_result(a: int, b: int, result: int, approach: str) -> None:
    """Print the GCD result in a formatted way."""
    print(f"\n  Input    : a = {a},  b = {b}")
    print(f"  Approach : {approach}")
    print(f"  GCD      : {result}")
    print("  " + "─" * 40)


# ─────────────────────────────────────────────
#  MAIN — Menu-Driven Program
# ─────────────────────────────────────────────

def main():
    """
    Menu-driven program to compute GCD using four approaches.
    Validates input and lets the user pick their preferred method.
    """
    print("=" * 50)
    print("       GCD OF TWO NUMBERS")
    print("=" * 50)

    # ── Get input ──────────────────────────────
    while True:
        try:
            a = int(input("\nEnter first integer  (a): "))
            b = int(input("Enter second integer (b): "))
            break
        except ValueError:
            print("  [Error] Please enter valid integers.")

    # ── Menu ───────────────────────────────────
    print("\nChoose an approach:")
    print("  1. Brute Force  — Check All Divisors         O(min(a,b))")
    print("  2. Euclidean    — Iterative                  O(log min(a,b))")
    print("  3. Euclidean    — Recursive                  O(log min(a,b))")
    print("  4. Built-in     — math.gcd()                 O(log min(a,b))")
    print("  5. All          — Run All Four & Compare")

    while True:
        choice = input("\nYour choice (1–5): ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            break
        print("  [Error] Enter a number between 1 and 5.")

    # ── Execute ────────────────────────────────
    print()
    if choice == "1":
        result = gcd_brute(a, b)
        display_result(a, b, result, "Brute Force (All Divisors)")

    elif choice == "2":
        result = gcd_iterative(a, b)
        display_result(a, b, result, "Euclidean — Iterative")

    elif choice == "3":
        result = gcd_recursive_safe(a, b)
        display_result(a, b, result, "Euclidean — Recursive")

    elif choice == "4":
        result = gcd_builtin(a, b)
        display_result(a, b, result, "Built-in (math.gcd)")

    elif choice == "5":
        r1 = gcd_brute(a, b)
        r2 = gcd_iterative(a, b)
        r3 = gcd_recursive_safe(a, b)
        r4 = gcd_builtin(a, b)
        display_result(a, b, r1, "Brute Force (All Divisors)")
        display_result(a, b, r2, "Euclidean — Iterative")
        display_result(a, b, r3, "Euclidean — Recursive")
        display_result(a, b, r4, "Built-in (math.gcd)")


if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

---

### Dry Run — Brute Force: `a = 12`, `b = 8`

> Iterate `i` from `1` to `min(12, 8) = 8`, track every `i` that divides both.

| Step | `i` | `12 % i == 0`? | `8 % i == 0`? | Both? | `gcd` Updated To | Explanation                     |
|------|-----|----------------|---------------|-------|------------------|---------------------------------|
| 1    | 1   | ✅ (12%1=0)    | ✅ (8%1=0)    | ✅    | 1                | 1 divides everything            |
| 2    | 2   | ✅ (12%2=0)    | ✅ (8%2=0)    | ✅    | 2                | 2 is a larger common divisor   |
| 3    | 3   | ✅ (12%3=0)    | ❌ (8%3=2)    | ❌    | 2                | 3 does not divide 8             |
| 4    | 4   | ✅ (12%4=0)    | ✅ (8%4=0)    | ✅    | 4                | 4 is the new largest so far     |
| 5    | 5   | ❌ (12%5=2)    | ❌ (8%5=3)    | ❌    | 4                | 5 divides neither               |
| 6    | 6   | ✅ (12%6=0)    | ❌ (8%6=2)    | ❌    | 4                | 6 divides 12 but not 8          |
| 7    | 7   | ❌ (12%7=5)    | ❌ (8%7=1)    | ❌    | 4                | 7 divides neither               |
| 8    | 8   | ❌ (12%8=4)    | ✅ (8%8=0)    | ❌    | 4                | 8 divides 8 but not 12          |
| End  | —   | —              | —             | —     | **4**            | Loop done; largest common = `4` |

**Final Result:** `GCD = 4` ✅

---

### Dry Run — Euclidean Iterative: `a = 48`, `b = 18`

> Loop runs while `b != 0`. Each iteration: `temp = b`, `b = a % b`, `a = temp`.

| Step | `a` Before | `b` Before | `temp` | `b = a % b`      | `a = temp` | `b != 0`? | Explanation                        |
|------|------------|------------|--------|------------------|------------|-----------|------------------------------------|
| 1    | 48         | 18         | 18     | 48 % 18 = **12** | 18         | ✅ 12≠0   | 48 ÷ 18 = 2 rem 12; reduce         |
| 2    | 18         | 12         | 12     | 18 % 12 = **6**  | 12         | ✅ 6≠0    | 18 ÷ 12 = 1 rem 6; reduce          |
| 3    | 12         | 6          | 6      | 12 % 6  = **0**  | 6          | ❌ 0=0    | 12 ÷ 6 = 2 rem 0; b becomes 0      |
| End  | **6**      | 0          | —      | —                | —          | Loop exits| `b == 0` → GCD is `a = 6`          |

**Final Result:** `GCD = 6` ✅

---

### Dry Run — Euclidean Iterative: `a = 100`, `b = 75`

| Step | `a` Before | `b` Before | `b = a % b`        | `a` After | Explanation              |
|------|------------|------------|--------------------|-----------|--------------------------|
| 1    | 100        | 75         | 100 % 75 = **25**  | 75        | 100 ÷ 75 = 1 rem 25      |
| 2    | 75         | 25         | 75 % 25  = **0**   | 25        | 75 ÷ 25 = 3 rem 0        |
| End  | **25**     | 0          | —                  | —         | `b == 0` → GCD = `25`    |

**Final Result:** `GCD = 25` ✅

---

### Dry Run — Euclidean Recursive: `a = 48`, `b = 18`

> Each row is one recursive call. Base case: `b == 0`.

| Call Depth | `a` | `b` | `b == 0`? | Returns                      | Explanation                   |
|------------|-----|-----|-----------|------------------------------|-------------------------------|
| 1          | 48  | 18  | ❌        | `gcd(18, 48 % 18)` = `gcd(18, 12)` | Recurse deeper           |
| 2          | 18  | 12  | ❌        | `gcd(12, 18 % 12)` = `gcd(12, 6)`  | Recurse deeper           |
| 3          | 12  | 6   | ❌        | `gcd(6, 12 % 6)`  = `gcd(6, 0)`    | Recurse deeper           |
| 4          | 6   | 0   | ✅        | `return 6`                          | **Base case hit — GCD = 6** |
| ← unwind   | —   | —   | —         | `6` bubbles back up all calls       | All calls return `6`     |

**Final Result:** `GCD = 6` ✅

---

### Dry Run — Edge Cases Summary

| Input `a` | Input `b` | What Happens                            | Result |
|-----------|-----------|-----------------------------------------|--------|
| `0`       | `5`       | Loop: `b=0%5=0` immediately; `a=5`      | `5`    |
| `5`       | `0`       | `b=0` → loop skips entirely; `a=5`      | `5`    |
| `7`       | `5`       | `7%5=2` → `5%2=1` → `2%1=0` → GCD = 1  | `1`    |
| `9`       | `9`       | `9%9=0` → single step → GCD = 9         | `9`    |
| `-12`     | `8`       | `abs()` → same as `gcd(12, 8)` = 4      | `4`    |

---

## 7. Time & Space Complexity

### Approach 1 — Brute Force (All Divisors)

| Metric | Complexity        | Reason                                                                               |
|--------|-------------------|--------------------------------------------------------------------------------------|
| Time   | **O(min(a, b))**  | Loop runs from `1` to `min(a, b)`, checking every integer as a potential divisor     |
| Space  | **O(1)**          | Only the `gcd` variable is maintained — no extra data structures                     |

- For large inputs (e.g., `a = 10^9`), this is extremely slow — up to a billion iterations.

---

### Approach 2 — Euclidean Iterative

| Metric | Complexity              | Reason                                                                                                        |
|--------|-------------------------|---------------------------------------------------------------------------------------------------------------|
| Time   | **O(log min(a, b))**    | Each step reduces the problem size by at least half (proven via the Fibonacci worst case). Steps ≈ `log_φ(min(a,b))` where φ ≈ 1.618 |
| Space  | **O(1)**                | Only three variables: `a`, `b`, `temp` — no recursion stack                                                   |

- **Worst case inputs:** Consecutive Fibonacci numbers (e.g., `a=89, b=55`) — they produce the most steps, but still only O(log n) steps total.

---

### Approach 3 — Euclidean Recursive

| Metric | Complexity              | Reason                                                                              |
|--------|-------------------------|-------------------------------------------------------------------------------------|
| Time   | **O(log min(a, b))**    | Same number of reduction steps as iterative — logic is identical                    |
| Space  | **O(log min(a, b))**    | Each recursive call adds a frame to the call stack; depth equals number of steps    |

- Same time as iterative, but uses **more memory** due to the call stack.
- For very large inputs Python's default recursion limit (`sys.setrecursionlimit`) may need increasing.

---

### Approach 4 — Built-in `math.gcd`

| Metric | Complexity              | Reason                                                                  |
|--------|-------------------------|-------------------------------------------------------------------------|
| Time   | **O(log min(a, b))**    | Implemented in C under the hood using the same Euclidean principle      |
| Space  | **O(1)**                | Single function call, no Python-level stack overhead                    |

---

### Summary Table

| Approach              | Time               | Space                  | Best For                                        |
|-----------------------|--------------------|------------------------|-------------------------------------------------|
| Brute Force           | O(min(a, b))       | O(1)                   | Learning what GCD means; tiny inputs only       |
| Euclidean Iterative   | O(log min(a, b))   | O(1)                   | Interviews; best balance of speed and memory    |
| Euclidean Recursive   | O(log min(a, b))   | O(log min(a, b))       | Elegant code; functional programming style      |
| Built-in math.gcd     | O(log min(a, b))   | O(1)                   | Production code; fastest in practice            |

> **The jump from O(min(a,b)) → O(log min(a,b)) is enormous.**
> For `a = 10^9`, brute force needs ~1 billion steps.
> Euclidean needs only ~60 steps. This is why the algorithm is over 2,300 years old and still used today.

---

## 8. Beginner Tips

### 🔑 Core Hacks & Rules of Thumb

1. **The swap pattern is the heart of the algorithm.**
   ```
   temp = b
   b = a % b
   a = temp
   ```
   This three-line pattern is what you must memorise cold. In Python you can also write it as a one-liner swap: `a, b = b, a % b` — this is idiomatic and eliminates the need for `temp` entirely.

2. **GCD(a, 0) = a — know this by heart.**
   When `b` becomes `0`, the GCD is whatever `a` currently holds. The loop condition `while b != 0` stops exactly at this moment. This is both the base case (recursive) and the termination condition (iterative).

3. **Order of arguments does NOT matter.**
   `GCD(48, 18) == GCD(18, 48)`. If `a < b`, the first iteration simply swaps them:
   `a=18, b=48 → temp=48, b=18%48=18, a=48` → effectively `GCD(48, 18)` from step 2 onward.

4. **For LCM, use GCD.**
   The relationship `LCM(a, b) = (a * b) // GCD(a, b)` means once you can compute GCD, you get LCM for free. These two always appear together.

5. **Fibonacci numbers are the worst case for Euclidean GCD.**
   Consecutive Fibonacci pairs (e.g., `55, 34` or `89, 55`) require the maximum number of steps for their size. This is how mathematicians proved the O(log n) bound — it's the hardest possible input pattern.

6. **Python one-liner swap eliminates the `temp` variable.**
   ```python
   # Instead of:
   temp = b; b = a % b; a = temp
   # Write:
   a, b = b, a % b
   ```
   Python evaluates the right-hand side fully before assigning — so `a % b` uses the *old* `b`, not the new one. This is safe and clean.

---

### ⚠️ Edge Case Reminders

| Scenario          | Trap                                              | Safe Handling                              |
|-------------------|---------------------------------------------------|--------------------------------------------|
| `a=0, b=0`        | Undefined — loop returns `0`, which can mislead   | Explicitly check and warn or raise error   |
| `a=0` or `b=0`    | Loop skips or exits immediately; correct result   | Verify: `GCD(0, x) = x`                   |
| Negative inputs   | `%` in Python returns non-negative, but `a` stays negative | Always `abs()` both inputs first  |
| `a == b`          | First remainder is `0`; single iteration          | Works automatically                        |
| Coprime pair      | GCD = 1; algorithm terminates at `b=1 → b=0`      | No special handling needed                 |
| Very large inputs | Brute force will time out; use Euclidean only      | Always prefer Euclidean for large n        |

---

### 📊 Approach Comparison at a Glance

| When to use...           | Reason                                                                    |
|--------------------------|---------------------------------------------------------------------------|
| **Brute Force**          | Only for tiny inputs or to verify the Euclidean result during learning    |
| **Euclidean Iterative**  | Default choice — interviews, competitive programming, any real use case   |
| **Euclidean Recursive**  | When clean, readable code matters more than call-stack overhead           |
| **math.gcd**             | Production Python code — fastest, battle-tested, handles edge cases       |

---

### 🧠 How This Problem Connects to Others

| Problem / Concept              | Connection                                                                   |
|--------------------------------|------------------------------------------------------------------------------|
| **LCM of Two Numbers**         | `LCM(a,b) = (a * b) // GCD(a,b)` — direct formula using GCD                 |
| **Simplify a Fraction**        | Divide numerator & denominator by their GCD to reduce to lowest terms        |
| **Check if Two Numbers are Coprime** | They are coprime if and only if `GCD(a, b) == 1`                      |
| **GCD of an Array**            | `GCD(a, b, c) = GCD(GCD(a, b), c)` — apply pairwise across the list         |
| **Modular Arithmetic**         | Euclidean algorithm is the basis of modular inverse (used in cryptography)   |
| **RSA Encryption**             | Key generation uses extended Euclidean algorithm — a direct extension        |
| **Bezout's Identity**          | Extended Euclidean gives `x, y` such that `ax + by = GCD(a,b)`              |

> **The mental model to carry forward:**
> GCD is about *remainder reduction* — you keep asking "what's left over?" until nothing is left.
> The Euclidean algorithm is not just a coding trick; it is the foundation of number theory, cryptography, and modular arithmetic. Every time you see `%` (modulo) in a math-heavy problem, think: *can the Euclidean idea help here?*

---

*End of Study Guide — GCD of Two Numbers (Euclidean Algorithm)*
