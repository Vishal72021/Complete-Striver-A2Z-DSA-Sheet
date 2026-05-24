# 🔍 Checking Whether a Number is Prime

---

## 1. Name of the Problem

**Prime Number Check**

> Also known as: *"Primality Test"* — one of the most fundamental problems in number theory,
> appearing in competitive programming, cryptography, and interview questions at every level.

---

## 2. Problem Statement

### What the Code Solves

Given a positive integer `n`, determine whether it is a **prime number**.

A number is **prime** if:
- It is greater than 1, AND
- It has **no divisors** other than 1 and itself.

A number is **composite** (not prime) if any integer in the range `[2, n-1]` divides it evenly.

---

### Formal Definition

```
Input  : A positive integer n
Output : "Prime" if n has exactly 2 divisors (1 and n), else "Not Prime"
```

---

### Example 1

```
Input  : n = 7
Output : The number is a prime number.
```

**Why?**
- 7 ÷ 2 → remainder 1 ❌
- 7 ÷ 3 → remainder 1 ❌
- 7 ÷ 4 → remainder 3 ❌
- 7 ÷ 5 → remainder 2 ❌
- 7 ÷ 6 → remainder 1 ❌
- No divisor found → ✅ Prime

---

### Example 2

```
Input  : n = 12
Output : The number is not a prime number.
```

**Why?**
- 12 ÷ 2 = 6 → remainder 0 ✅ → Divisor found immediately → Not Prime

---

### Example 3

```
Input  : n = 2
Output : The number is a prime number.
```

> 2 is the **smallest and only even prime**. The loop `range(2, 2)` is empty → no divisor found.

---

### Example 4

```
Input  : n = 1
Output : The number is not a prime number.
```

> 1 is **neither prime nor composite** by mathematical convention.

---

## 3. Logic Behind the Solution

### Part A — Intuition

The simplest question to ask is: *"Does anything divide n other than 1 and n itself?"*

Start from 2 (the smallest possible divisor greater than 1) and try every integer up to `n-1`.
The moment you find one that divides `n` with no remainder, you can **stop immediately** — the
number is composite.

```
n = 13

Try: 2  → 13 % 2 = 1  ❌
Try: 3  → 13 % 3 = 1  ❌
Try: 4  → 13 % 4 = 1  ❌
...
Try: 12 → 13 % 12 = 1 ❌
→ No divisor found → PRIME ✅
```

**Key insight for the optimised approach**:
If `n` has a factor greater than `√n`, its *paired* factor must be smaller than `√n`.
So if no factor exists up to `√n`, none exists at all — you never need to search beyond `√n`.

```
n = 36,  √36 = 6

Pairs: (2, 18)  (3, 12)  (4, 9)  (6, 6)
         ↑               ↑
    smaller half    the √n boundary

→ Check only up to 6. If no factor found there, n is prime.
```

---

### Part B — Approaches

| Approach    | Strategy                                 | Time      | Space |
|-------------|------------------------------------------|-----------|-------|
| Brute Force | Loop from 2 to n-1, check each candidate | O(n)      | O(1)  |
| Optimised   | Loop from 2 to √n only                   | O(√n)     | O(1)  |

**Edge Cases to Handle**

| Input      | Expected Result | Reason                                      |
|------------|-----------------|---------------------------------------------|
| `n = 1`    | Not Prime       | 1 is neither prime nor composite            |
| `n = 2`    | Prime           | Smallest prime; loop is empty (range(2,2))  |
| `n = 3`    | Prime           | Only candidate is 2; 3 % 2 ≠ 0             |
| `n = 4`    | Not Prime       | 4 % 2 == 0                                 |
| `n ≤ 0`    | Invalid         | Primes are defined only for integers > 1   |
| Large `n`  | Varies          | Brute force is too slow; use O(√n)         |

---

## 4. Pseudocode

### Brute Force — O(n)

```
FUNCTION is_prime_brute(n):
    IF n <= 1:
        RETURN False                   # 0, 1, and negatives are not prime

    FOR i FROM 2 TO n-1 (inclusive):
        IF n MOD i == 0:
            RETURN False               # found a divisor → not prime

    RETURN True                        # no divisor found → prime
```

---

### Optimised — O(√n)

```
FUNCTION is_prime_optimised(n):
    IF n <= 1:
        RETURN False                   # handle edge cases first
    IF n <= 3:
        RETURN True                    # 2 and 3 are prime by definition
    IF n MOD 2 == 0 OR n MOD 3 == 0:
        RETURN False                   # quickly eliminate even numbers and multiples of 3

    i = 5
    WHILE i * i <= n:                  # only check up to √n
        IF n MOD i == 0:
            RETURN False               # divisible by i → not prime
        IF n MOD (i + 2) == 0:
            RETURN False               # divisible by i+2 → not prime
        i = i + 6                      # all primes > 3 are of the form 6k ± 1

    RETURN True
```

> **Why `6k ± 1`?**
> Every integer can be expressed as one of: 6k, 6k+1, 6k+2, 6k+3, 6k+4, 6k+5.
> - 6k, 6k+2, 6k+4 → divisible by 2 → not prime
> - 6k+3 → divisible by 3 → not prime
> - Only 6k+1 and 6k+5 (= 6k-1) can be prime → check only those.

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Prime Number Check (Primality Test)
  Approach : Brute Force  → O(n)
             Optimised    → O(√n)  using 6k ± 1 rule
  Author   : Study Notes
=============================================================
"""

import math


# ─────────────────────────────────────────────────────────────
# HELPER — Validated input
# ─────────────────────────────────────────────────────────────

def get_integer(prompt: str) -> int:
    """
    Repeatedly prompt until the user enters a valid integer.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        int: Any integer entered by the user (validation of range
             is handled inside each approach function).
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number.\n")


# ─────────────────────────────────────────────────────────────
# APPROACH 1 — Brute Force  O(n)
# ─────────────────────────────────────────────────────────────

def is_prime_brute(n: int) -> bool:
    """
    Check primality by testing every integer from 2 to n-1.

    Strategy:
        For each candidate i in [2, n-1], if n % i == 0, n is composite.
        If no such i is found, n is prime.

    Args:
        n (int): The number to test.

    Returns:
        bool: True if n is prime, False otherwise.

    Time  Complexity: O(n)  — up to n-2 iterations in the worst case.
    Space Complexity: O(1)  — only a loop variable; no extra storage.
    """
    # Edge case: primes are defined only for integers greater than 1
    if n <= 1:
        return False

    # Try every potential divisor from 2 up to n-1
    for i in range(2, n):               # range(2, n) → [2, 3, ..., n-1]
        if n % i == 0:                  # remainder 0 → i divides n → composite
            return False                # early exit; no need to continue

    return True                         # survived all checks → prime


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Optimised  O(√n)  using 6k ± 1 rule
# ─────────────────────────────────────────────────────────────

def is_prime_optimised(n: int) -> bool:
    """
    Check primality using the paired-divisor insight and 6k±1 rule.

    Key Insights:
        1. If n has a factor > √n, its paired factor is < √n.
           So searching only up to √n is sufficient.
        2. All primes greater than 3 are of the form 6k ± 1.
           We can eliminate all multiples of 2 and 3 upfront, then
           step through candidates in increments of 6.

    Args:
        n (int): The number to test.

    Returns:
        bool: True if n is prime, False otherwise.

    Time  Complexity: O(√n)  — loop runs at most √n / 3 iterations.
    Space Complexity: O(1)   — constant extra space.
    """
    # Handle small and trivial cases
    if n <= 1:
        return False          # 0, 1, and negatives → not prime
    if n <= 3:
        return True           # 2 and 3 are prime
    if n % 2 == 0:
        return False          # eliminate all even numbers > 2
    if n % 3 == 0:
        return False          # eliminate all multiples of 3 > 3

    # All remaining primes are of the form 6k ± 1
    # Start at i = 5 (= 6×1 - 1) and check i and i+2 (= 6k+1)
    i = 5
    while i * i <= n:         # only go up to √n
        if n % i == 0:        # check 6k - 1
            return False
        if n % (i + 2) == 0:  # check 6k + 1
            return False
        i += 6                # advance to next 6k block

    return True               # no divisor found → prime


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(n: int, result: bool, label: str) -> None:
    """
    Pretty-print the primality result.

    Args:
        n      (int)  : The number tested.
        result (bool) : True if prime, False otherwise.
        label  (str)  : Approach label for display.
    """
    verdict = "PRIME ✅" if result else "NOT PRIME ❌"
    print(f"\n  [{label}]")
    print(f"  {n} is → {verdict}")

    # Extra contextual notes
    if n <= 1:
        print("  Note: Numbers ≤ 1 are neither prime nor composite.")
    elif n == 2:
        print("  Note: 2 is the smallest and only even prime.")
    elif result and n % 2 == 0:
        pass   # unreachable (no even number > 2 is prime)
    elif not result:
        # Find and show the smallest divisor for educational value
        for d in range(2, int(math.isqrt(n)) + 1):
            if n % d == 0:
                print(f"  Smallest divisor of {n} (other than 1): {d}  "
                      f"[since {d} × {n // d} = {n}]")
                break


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to check whether a number is prime.

    Options:
        1 → Brute Force  (O(n))
        2 → Optimised    (O(√n) with 6k±1 rule)
        3 → Both side by side (with consistency check)
        4 → Exit
    """
    print("=" * 52)
    print("   PRIME NUMBER CHECK — Study Program")
    print("=" * 52)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force  — O(n)")
        print("  [2] Optimised    — O(√n)  with 6k±1 rule")
        print("  [3] Both         — Compare side by side")
        print("  [4] Exit")
        print("-" * 52)

        choice = input("  Enter choice (1/2/3/4): ").strip()

        if choice == "4":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, or 4.\n")
            continue

        # ── Get input ─────────────────────────────────────
        n = get_integer("\n  Enter an integer n: ")

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = is_prime_brute(n)
            display_result(n, result, "Brute Force — O(n)")

        elif choice == "2":
            result = is_prime_optimised(n)
            display_result(n, result, "Optimised — O(√n)")

        elif choice == "3":
            bf_result  = is_prime_brute(n)
            opt_result = is_prime_optimised(n)
            display_result(n, bf_result,  "Brute Force — O(n)")
            display_result(n, opt_result, "Optimised  — O(√n)")

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

We use two examples: **n = 7** (prime) and **n = 12** (not prime).

---

### Brute Force Dry Run — n = 7 (Prime)

| Step | i | Operation  | n % i | Divisor Found? | is_prime Flag | Explanation                          |
|------|---|------------|-------|----------------|---------------|--------------------------------------|
| Init | — | n = 7      | —     | —              | True          | Start with assumption: prime         |
| 1    | 2 | 7 % 2 = 1  | 1     | ❌ No           | True          | 1 ≠ 0; not a divisor; continue       |
| 2    | 3 | 7 % 3 = 1  | 1     | ❌ No           | True          | Not a divisor; continue              |
| 3    | 4 | 7 % 4 = 3  | 3     | ❌ No           | True          | Not a divisor; continue              |
| 4    | 5 | 7 % 5 = 2  | 2     | ❌ No           | True          | Not a divisor; continue              |
| 5    | 6 | 7 % 6 = 1  | 1     | ❌ No           | True          | Not a divisor; loop ends (range(2,7))|
| End  | — | Return True | —    | —              | **True**      | No divisor found → **PRIME ✅**      |

> Loop ran **5 iterations** (i = 2 through 6).

---

### Brute Force Dry Run — n = 12 (Not Prime)

| Step | i | Operation   | n % i | Divisor Found? | is_prime Flag | Explanation                     |
|------|---|-------------|-------|----------------|---------------|---------------------------------|
| Init | — | n = 12      | —     | —              | True          | Start with assumption: prime    |
| 1    | 2 | 12 % 2 = 0  | 0     | ✅ Yes          | **False**     | Divisor found → break immediately |
| End  | — | Return False | —    | —              | **False**     | Early exit → **NOT PRIME ❌**   |

> Loop ran **1 iteration** only — early exit via `break`.

---

### Optimised Dry Run — n = 7 (Prime)

**Pre-checks before the while loop:**

| Step | Check              | Result | Action         |
|------|--------------------|--------|----------------|
| 1    | 7 ≤ 1?             | No     | Continue       |
| 2    | 7 ≤ 3?             | No     | Continue       |
| 3    | 7 % 2 == 0?        | No (1) | Continue       |
| 4    | 7 % 3 == 0?        | No (1) | Continue       |
| 5    | Enter while loop   | i = 5  | 5 × 5 = 25 > 7 → loop never executes |

**While loop:** Condition `5 * 5 = 25 ≤ 7` is **False** → loop body skipped entirely.

| Result | Explanation                   |
|--------|-------------------------------|
| True   | No divisor found → **PRIME ✅** |

> Completed in **O(1)** effective steps for n = 7 — no loop iterations needed.

---

### Optimised Dry Run — n = 49 (Not Prime, = 7 × 7)

**Pre-checks:**

| Step | Check         | Result | Action   |
|------|---------------|--------|----------|
| 1    | 49 ≤ 1?       | No     | Continue |
| 2    | 49 ≤ 3?       | No     | Continue |
| 3    | 49 % 2 == 0?  | No (1) | Continue |
| 4    | 49 % 3 == 0?  | No (1) | Continue |

**While loop** (`i` starts at 5, condition: `i * i ≤ 49`):

| Step | i | i*i | i*i ≤ 49? | 49 % i | 49 % (i+2) | Action                         |
|------|---|-----|-----------|--------|------------|--------------------------------|
| 1    | 5 | 25  | ✅ Yes     | 4      | 49%7 = **0** | Divisor found (i+2 = 7) → Return False |

> 49 is **NOT PRIME ❌** (49 = 7 × 7). Found in **1 loop iteration**.

---

### Optimised Dry Run — n = 97 (Prime)

**√97 ≈ 9.8 → loop runs while `i*i ≤ 97`**

| Step | i  | i*i | i*i ≤ 97? | 97 % i | 97 % (i+2) | Action        |
|------|----|-----|-----------|--------|------------|---------------|
| 1    | 5  | 25  | ✅         | 2      | 97%7=6     | No divisor    |
| 2    | 11 | 121 | ❌         | —      | —          | Loop exits    |

> **Only 1 loop iteration** needed for n = 97.
> Result: **PRIME ✅** — far faster than brute force's 95 iterations.

---

## 7. Time & Space Complexity

### Brute Force

| Case         | Time Complexity | Explanation                                                                     |
|--------------|-----------------|---------------------------------------------------------------------------------|
| Best Case    | O(1)            | n is even (n % 2 == 0 at i=2) → exits immediately on the very first check     |
| Worst Case   | O(n)            | n is prime → loop runs from i=2 all the way to i=n-1 without finding a divisor |
| Average Case | O(n)            | For random n, expected iterations are proportional to n                         |

| Space Complexity | O(1) | Only one loop variable `i` used. No arrays, no recursion stack. |
|---|---|---|

---

### Optimised (√n + 6k±1)

| Case         | Time Complexity | Explanation                                                                         |
|--------------|-----------------|-------------------------------------------------------------------------------------|
| Best Case    | O(1)            | n ≤ 3, or n is even / divisible by 3 → caught by pre-checks before the loop        |
| Worst Case   | O(√n)           | n is prime → loop runs from i=5 all the way to i=√n finding no divisor             |
| Average Case | O(√n)           | On average, a factor is found well before √n, but upper bound remains O(√n)        |

| Space Complexity | O(1) | Only one loop variable `i` and constant checks. No extra storage whatsoever. |
|---|---|---|

---

### Comparison at a Glance

| n           | Brute Force (max iters) | Optimised (max iters) | Speed-up      |
|-------------|-------------------------|-----------------------|---------------|
| 100         | 98                      | 5                     | ~20×          |
| 10,007      | 10,005                  | 33                    | ~303×         |
| 1,000,003   | 1,000,001               | 333                   | ~3,000×       |
| 1,000,000,007 | ~10⁹                  | ~10,541               | ~94,868×      |

> The gap widens **dramatically** as n grows — the optimised approach is the only viable
> choice for numbers in the millions and beyond.

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **The √n shortcut**: If n has no factor from 2 to √n, it has no factor at all.
   This is the single most important insight in primality testing.

2. **Even numbers are instantly out**: After checking divisibility by 2, you can skip all
   even candidates. The 6k±1 approach takes this idea even further.

3. **`break` is your performance ally**: The moment you find one divisor, the number is
   composite — stop. Don't waste iterations checking the rest.

4. **`is_prime = True` as a flag**: The original code sets a boolean flag and updates it.
   Returning early (`return False`) is cleaner and faster — avoid the flag pattern in
   real code.

---

### ⚠️ Edge Case Reminders

| Input      | Correct Answer  | Common Mistake                                      |
|------------|-----------------|-----------------------------------------------------|
| `n = 1`    | NOT Prime       | Forgetting that 1 is **not** prime (has only 1 divisor, not 2) |
| `n = 2`    | Prime           | `range(2, 2)` is empty → code correctly returns True without checking |
| `n = 4`    | NOT Prime       | Don't test only odd numbers without first eliminating 4 |
| `n = 0`    | NOT Prime       | 0 has infinitely many divisors — not prime          |
| `n < 0`    | NOT Prime       | Negative numbers are not prime by definition         |
| `n = 9`    | NOT Prime       | 9 = 3×3; easy to miss — always check up to **and including** √n |

---

### 🔬 The `math.isqrt` vs `int(n**0.5)` Trap

```python
# ❌ Risky — floating-point errors can cause off-by-one for perfect squares
int(49 ** 0.5)     # sometimes gives 6 instead of 7 for large perfect squares

# ✅ Always correct — integer square root, no floating-point issues
math.isqrt(49)     # always gives 7
```

> **Rule of thumb**: Use `math.isqrt(n)` any time you need integer square roots in Python.

---

### ⚖️ When To Use Which Approach

| Situation                                    | Recommended Approach          |
|----------------------------------------------|-------------------------------|
| Learning / first exposure to primality        | Brute Force (clearest logic)  |
| n is small (n < 1,000)                        | Either works fine             |
| n is large (n > 10,000)                       | Always use Optimised          |
| Competitive programming / interviews          | Optimised (6k±1)              |
| Checking primality for millions of numbers    | Sieve of Eratosthenes         |
| Cryptographic-grade primality (very large n)  | Miller-Rabin probabilistic test|

---

### 📏 Rules of Thumb

- **O(√n) is the pattern**: Anytime a problem involves factors, divisibility, or primality
  → think `√n` as your loop boundary.
- **Eliminate 2 and 3 first**: These two pre-checks alone cut your search space to ≈1/3
  before the main loop even starts.
- **Prime ≠ Odd**: 2 is prime and even. Never assume "prime implies odd."
- **1 is NOT prime**: This trips up beginners constantly. Memorise it as a rule.
- **The 6k±1 pattern**: All primes > 3 are of the form `6k-1` or `6k+1`
  (e.g., 5, 7, 11, 13, 17, 19, 23, 29…). Use this to step in jumps of 6.

---

### 🔗 Related Problems to Practice Next

| Problem                            | Key Concept Shared                           |
|------------------------------------|----------------------------------------------|
| Print all primes up to N           | Sieve of Eratosthenes (O(n log log n))       |
| Find all prime factors of N        | Factorisation loop up to √n                  |
| Count prime numbers in a range     | Sieve / segmented sieve                      |
| Goldbach's Conjecture verification | Primality check for every even number        |
| Find divisors of N                 | Same √n loop; collect both i and n//i        |
| Largest prime factor               | Divide out factors iteratively up to √n      |

---

*End of Study Notes — Prime Number Check*