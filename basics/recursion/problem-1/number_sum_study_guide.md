# ➕ Sum of the First N Natural Numbers

---

## 1. Name of the Problem

**Sum of the First N Natural Numbers**

> Also known as: *"Gauss Summation"* or *"Arithmetic Series Sum"* — one of the oldest and
> most elegant results in mathematics, famously discovered by Carl Friedrich Gauss as a
> child by pairing numbers at opposite ends of a sequence.

---

## 2. Problem Statement

### What the Code Solves

Given a positive integer `n`, compute the **sum of all natural numbers from 1 to n**.

```
1 + 2 + 3 + 4 + ... + n = ?
```

The code skips the loop entirely and uses the **closed-form formula**:

```
Sum = n × (n + 1) / 2
```

---

### Formal Definition

```
Input  : A positive integer n
Output : The value of  1 + 2 + 3 + ... + n
```

---

### Example 1

```
Input  : n = 5
Output : Sum of the first 5 natural numbers is: 15
```

**Why?**
```
1 + 2 + 3 + 4 + 5 = 15
Formula: 5 × (5 + 1) / 2 = 5 × 6 / 2 = 30 / 2 = 15  ✅
```

---

### Example 2

```
Input  : n = 10
Output : Sum of the first 10 natural numbers is: 55
```

**Why?**
```
1 + 2 + 3 + ... + 10 = 55
Formula: 10 × (10 + 1) / 2 = 10 × 11 / 2 = 110 / 2 = 55  ✅
```

---

### Example 3

```
Input  : n = 1
Output : Sum of the first 1 natural numbers is: 1
```

> The sum of a single natural number is itself.
> Formula: 1 × (1 + 1) / 2 = 1 × 2 / 2 = 1  ✅

---

### Example 4

```
Input  : n = 100
Output : Sum of the first 100 natural numbers is: 5050
```

> This is Gauss's legendary classroom answer — computed mentally by pairing
> (1 + 100), (2 + 99), (3 + 98) … → 50 pairs × 101 = 5050.

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Loop Way (Brute Force Thinking)

The most natural approach is to simply add each number one by one:

```
n = 5

Step 1: total = 0
Step 2: total = 0 + 1 = 1
Step 3: total = 1 + 2 = 3
Step 4: total = 3 + 3 = 6
Step 5: total = 6 + 4 = 10
Step 6: total = 10 + 5 = 15
```

This works, but takes n steps.

---

#### The Gauss Way (Formula / Optimised Thinking)

Write the sum forwards and backwards simultaneously:

```
S  =   1  +   2  +   3  + ... + (n-1) +  n
S  =   n  + (n-1)+ (n-2) + ... +   2  +  1
─────────────────────────────────────────────
2S = (n+1)+ (n+1)+ (n+1) + ... + (n+1)+(n+1)
   =  n × (n + 1)

∴  S = n × (n + 1) / 2
```

Every pair sums to `(n + 1)`, and there are exactly `n` such pairs.
This reduces an n-step problem to a **single arithmetic expression** — O(1) time.

---

### Part B — Approaches

| Approach    | Strategy                               | Time  | Space |
|-------------|----------------------------------------|-------|-------|
| Brute Force | Loop from 1 to n, accumulate total     | O(n)  | O(1)  |
| Optimised   | Apply the formula n × (n + 1) // 2     | O(1)  | O(1)  |

**Edge Cases to Handle**

| Input    | Expected Result | Reason                                           |
|----------|-----------------|--------------------------------------------------|
| `n = 0`  | 0               | Sum of zero numbers is 0 (empty sum)             |
| `n = 1`  | 1               | Only one natural number; sum equals itself       |
| `n < 0`  | Invalid         | Natural numbers are positive; reject negatives   |
| Large `n`| Very large int  | Python handles big integers natively; no overflow|

---

## 4. Pseudocode

### Brute Force — O(n)

```
FUNCTION sum_brute_force(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    total = 0
    FOR i FROM 1 TO n (inclusive):
        total = total + i       # accumulate each natural number

    RETURN total
```

---

### Optimised — O(1) using Gauss Formula

```
FUNCTION sum_formula(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    RETURN n × (n + 1) // 2    # integer division avoids floating-point
```

> **Why `//` instead of `/`?**
> One of `n` or `(n+1)` is always even (consecutive integers), so their product
> is always divisible by 2. Using `//` (integer division) keeps the result
> as a clean integer with no floating-point representation issues.

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Sum of the First N Natural Numbers
  Approach : Brute Force  → O(n)   loop accumulation
             Optimised    → O(1)   Gauss formula
  Author   : Study Notes
=============================================================
"""


# ─────────────────────────────────────────────────────────────
# HELPER — Validated input
# ─────────────────────────────────────────────────────────────

def get_non_negative_integer(prompt: str) -> int:
    """
    Repeatedly prompt until the user enters a non-negative integer.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        int: A validated non-negative integer (>= 0).
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("  ⚠  Please enter a non-negative integer (>= 0).\n")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number.\n")


# ─────────────────────────────────────────────────────────────
# APPROACH 1 — Brute Force  O(n)
# ─────────────────────────────────────────────────────────────

def sum_brute_force(n: int) -> int:
    """
    Compute the sum 1 + 2 + 3 + ... + n using a simple loop.

    Strategy:
        Initialise a running total at 0.
        Add each integer from 1 to n one at a time.

    Args:
        n (int): Upper bound of the summation (n >= 0).

    Returns:
        int: Sum of the first n natural numbers.

    Time  Complexity: O(n) — exactly n iterations of the loop.
    Space Complexity: O(1) — only one extra variable (total).
    """
    total = 0                          # running accumulator

    for i in range(1, n + 1):         # i goes from 1 to n inclusive
        total += i                     # add current number to running sum

    return total


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Optimised  O(1) — Gauss Formula
# ─────────────────────────────────────────────────────────────

def sum_formula(n: int) -> int:
    """
    Compute the sum 1 + 2 + 3 + ... + n using the Gauss closed-form formula.

    Formula Derivation:
        Write the series forwards and backwards; every pair sums to (n+1).
        There are n such pairs, giving total = n * (n+1) / 2.

    Args:
        n (int): Upper bound of the summation (n >= 0).

    Returns:
        int: Sum of the first n natural numbers.

    Time  Complexity: O(1) — single arithmetic expression; no loops.
    Space Complexity: O(1) — no extra storage whatsoever.
    """
    # n*(n+1) always has one even factor (consecutive integers),
    # so // 2 always yields a perfect integer — no rounding needed.
    return n * (n + 1) // 2


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(n: int, result: int, label: str) -> None:
    """
    Pretty-print the summation result with context.

    Args:
        n      (int): The value of n entered by the user.
        result (int): The computed sum.
        label  (str): Approach label for display.
    """
    print(f"\n  [{label}]")
    if n == 0:
        print(f"  Sum of the first 0 natural numbers is: 0  (empty sum)")
    elif n <= 5:
        # Show the full expanded series for small n (educational)
        series = " + ".join(str(i) for i in range(1, n + 1))
        print(f"  {series} = {result}")
    else:
        # Show a condensed representation for larger n
        print(f"  1 + 2 + 3 + ... + {n} = {result}")

    print(f"  Sum of the first {n} natural numbers is: {result}")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to compute the sum of first n natural numbers.

    Options:
        1 → Brute Force  (O(n) loop)
        2 → Optimised    (O(1) Gauss formula)
        3 → Both side by side (with consistency check)
        4 → Exit
    """
    print("=" * 54)
    print("   SUM OF FIRST N NATURAL NUMBERS — Study Program")
    print("=" * 54)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force  — O(n)  loop")
        print("  [2] Optimised    — O(1)  Gauss formula")
        print("  [3] Both         — Compare side by side")
        print("  [4] Exit")
        print("-" * 54)

        choice = input("  Enter choice (1/2/3/4): ").strip()

        if choice == "4":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, or 4.\n")
            continue

        # ── Get input ─────────────────────────────────────
        n = get_non_negative_integer("\n  Enter a non-negative integer n: ")

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = sum_brute_force(n)
            display_result(n, result, "Brute Force — O(n)")

        elif choice == "2":
            result = sum_formula(n)
            display_result(n, result, "Optimised — O(1) Gauss Formula")

        elif choice == "3":
            bf_result  = sum_brute_force(n)
            opt_result = sum_formula(n)
            display_result(n, bf_result,  "Brute Force — O(n)")
            display_result(n, opt_result, "Optimised  — O(1) Gauss Formula")

            # Sanity check — both must always agree
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

We use **n = 5** for the brute force and **n = 10** for the formula, showing full step-by-step execution.

---

### Brute Force Dry Run — n = 5

| Step | i | total Before | Operation    | total After | Explanation                     |
|------|---|--------------|--------------|-------------|---------------------------------|
| Init | — | 0            | total = 0    | 0           | Accumulator starts at zero      |
| 1    | 1 | 0            | 0 + 1 = 1    | 1           | Add 1 to running total          |
| 2    | 2 | 1            | 1 + 2 = 3    | 3           | Add 2 to running total          |
| 3    | 3 | 3            | 3 + 3 = 6    | 6           | Add 3 to running total          |
| 4    | 4 | 6            | 6 + 4 = 10   | 10          | Add 4 to running total          |
| 5    | 5 | 10           | 10 + 5 = 15  | 15          | Add 5; loop ends (range(1, 6))  |
| End  | — | —            | return 15    | —           | **Final Answer: 15 ✅**         |

> Loop ran **5 iterations** — one per natural number.

---

### Brute Force Dry Run — n = 0 (Edge Case)

| Step | i | total Before | Operation          | total After | Explanation                       |
|------|---|--------------|--------------------|-------------|-----------------------------------|
| Init | — | 0            | total = 0          | 0           | Accumulator initialised           |
| —    | — | 0            | range(1, 1) → empty| 0           | Loop body never executes          |
| End  | — | —            | return 0           | —           | **Final Answer: 0 ✅ (empty sum)**|

---

### Optimised (Formula) Dry Run — n = 10

| Step | Operation               | Intermediate Value | Explanation                                   |
|------|-------------------------|--------------------|-----------------------------------------------|
| 1    | n + 1                   | 10 + 1 = 11        | Compute the second factor                     |
| 2    | n × (n + 1)             | 10 × 11 = 110      | Multiply n by (n+1)                           |
| 3    | n × (n + 1) // 2        | 110 // 2 = 55      | Integer-divide by 2; exact since 110 is even  |
| End  | return 55               | **55**             | **Final Answer: 55 ✅**                       |

> Entire computation: **3 arithmetic operations**, regardless of how large n is.

---

### Optimised (Formula) Dry Run — n = 100 (Gauss's Classic)

| Step | Operation               | Intermediate Value | Explanation                        |
|------|-------------------------|--------------------|------------------------------------|
| 1    | n + 1                   | 100 + 1 = 101      | Second factor                      |
| 2    | n × (n + 1)             | 100 × 101 = 10,100 | Product                            |
| 3    | n × (n + 1) // 2        | 10,100 // 2 = 5050 | Exact halving (10,100 is even)     |
| End  | return 5050             | **5050**           | **Gauss's legendary answer ✅**    |

> What would take 100 loop iterations in brute force is done in **3 steps** here.

---

### Side-by-Side Step Count Comparison

| n         | Brute Force Steps | Formula Steps | Ratio         |
|-----------|-------------------|---------------|---------------|
| 5         | 5                 | 3             | ~2×           |
| 100       | 100               | 3             | ~33×          |
| 10,000    | 10,000            | 3             | ~3,333×       |
| 1,000,000 | 1,000,000         | 3             | ~333,333×     |
| n         | n                 | 3             | n/3 → **∞**  |

> The formula **always** takes exactly 3 operations — multiply, add, divide — forever.

---

## 7. Time & Space Complexity

### Brute Force — Loop Accumulation

| Case         | Time Complexity | Explanation                                                          |
|--------------|-----------------|----------------------------------------------------------------------|
| Best Case    | O(n)            | Even for n=1, the loop structure is defined by n; always runs fully  |
| Worst Case   | O(n)            | No early exit exists; all n iterations always execute                |
| Average Case | O(n)            | Exactly n additions every single time — no variability               |

| Space Complexity | O(1) | Only one extra variable (`total`) is used. The loop variable `i` is also O(1). No arrays, no recursion. |
|---|---|---|

---

### Optimised — Gauss Formula

| Case         | Time Complexity | Explanation                                                              |
|--------------|-----------------|--------------------------------------------------------------------------|
| Best Case    | O(1)            | Single formula evaluation; completely independent of n                   |
| Worst Case   | O(1)            | Same single formula; n=10⁹ takes identical time to n=1                  |
| Average Case | O(1)            | Always exactly 3 arithmetic operations: multiply, add, integer divide    |

| Space Complexity | O(1) | No variables other than the return value expression itself. Zero extra storage. |
|---|---|---|

---

### Why Is the Formula Truly O(1)?

In the brute force, work grows *with* n — double n, double the steps.
In the formula, work is **fixed** — three arithmetic operations happen no matter what.
This is the definition of constant time: **input size has zero effect on runtime**.

```
Brute force: T(n) = n          → linear growth
Formula:     T(n) = 3          → flat line; constant forever
```

Python's arbitrary-precision integers mean multiplication of very large numbers
technically takes slightly more than O(1) at the hardware level for astronomically
large n — but for all practical purposes the formula is treated as O(1).

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Pair from both ends**: Gauss's trick — pair the first and last (1+n),
   second and second-to-last (2+(n-1)), and so on. Every pair equals (n+1),
   and there are n/2 such pairs → sum = n(n+1)/2.

2. **Visualise as a triangle**: Imagine stacking rows of dots:
```
   Row 1: ●
   Row 2: ● ●
   Row 3: ● ● ●
   Row 4: ● ● ● ●
   Row 5: ● ● ● ● ●
```
   This forms half a rectangle of size n × (n+1). Half of that = n(n+1)/2.

3. **`//` not `/`**: Always use integer division (`//`) for this formula.
   One of n or (n+1) is always even (consecutive integers), so the result
   is always a whole number — `//` makes this explicit and avoids float output.

4. **Recognise the pattern in interviews**: Whenever you see a loop that adds
   consecutive integers, immediately replace it with the formula.
   This signals mathematical maturity to interviewers.

---

### ⚠️ Edge Case Reminders

| Input     | Correct Answer | Common Mistake                                          |
|-----------|----------------|---------------------------------------------------------|
| `n = 0`   | 0              | Forgetting the empty sum convention; should return 0    |
| `n = 1`   | 1              | Formula: 1×2//2 = 1 ✅; simple but worth verifying     |
| `n < 0`   | Invalid        | Natural numbers start at 1; reject negative input       |
| `n = 2`   | 3              | 1+2=3; Formula: 2×3//2=3 ✅                            |
| Large `n` | Very large int | Python handles big ints natively — no overflow risk     |

---

### 🔬 The `//` vs `/` Distinction

```python
n = 5

# ❌ Using regular division — produces a float
result = n * (n + 1) / 2       # → 15.0  (float, not ideal)

# ✅ Using integer division — clean integer output
result = n * (n + 1) // 2      # → 15   (int, always correct)
```

> Since one of `n` or `n+1` is always even, the product `n*(n+1)` is always
> divisible by 2 — `//` is perfectly safe here and gives the cleanest result.

---

### ⚖️ When To Use Which Approach

| Situation                                         | Recommended Approach           |
|---------------------------------------------------|--------------------------------|
| Learning / first time seeing summation            | Brute Force (builds intuition) |
| Any real code or interview setting                | Formula — always O(1)          |
| Competitive programming                           | Formula — saves critical time  |
| n is small (n < 1,000)                            | Either works, formula is cleaner|
| n is very large (n > 10⁶)                         | Formula only; loop is too slow |
| Weighted or non-consecutive sums                  | Loop or arithmetic series formula|

---

### 📏 Rules of Thumb

- **Any arithmetic series** `a, a+d, a+2d, ..., l` has sum = `(count × (first + last)) / 2`.
  The natural numbers are just the special case where `a=1`, `d=1`, `l=n`.

- **Spot the O(n) loop pattern**: If you see `for i in range(1, n+1): total += i`,
  that's always replaceable with `n*(n+1)//2`. This is a classic code review signal.

- **Sum of even numbers up to n**: `n//2 × (n//2 + 1)`
- **Sum of odd numbers up to n**: `ceil(n/2)²`
- **Sum of squares 1²+2²+...+n²**: `n(n+1)(2n+1) / 6`
- **Sum of cubes 1³+2³+...+n³**: `[n(n+1)/2]²`  ← notice it squares the natural sum!

---

### 🔗 Related Problems to Practice Next

| Problem                                | Key Concept Shared                          |
|----------------------------------------|---------------------------------------------|
| Sum of even numbers from 1 to n        | Arithmetic series with step 2               |
| Sum of odd numbers from 1 to n         | Arithmetic series; pairing trick            |
| Sum of squares (1²+2²+...+n²)          | Closed-form formula: n(n+1)(2n+1)/6        |
| Sum of cubes (1³+2³+...+n³)            | Closed-form formula: [n(n+1)/2]²           |
| Find n given the sum S                 | Reverse the formula: solve n²+n-2S=0       |
| Prefix sum array                       | Build on the same accumulation idea         |
| Subarray sum problems                  | Prefix sums make O(n²) → O(n)              |

---

*End of Study Notes — Sum of the First N Natural Numbers*