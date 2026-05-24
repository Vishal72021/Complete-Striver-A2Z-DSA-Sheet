md# ✖️ Factorial of a Number

---

## 1. Name of the Problem

**Factorial of a Number**

> Also known as: *"n! (n Factorial)"* — a foundational concept in mathematics and
> computer science, appearing everywhere from combinatorics and probability to recursion
> theory, algorithm analysis, and compiler design.

---

## 2. Problem Statement

### What the Code Solves

Given a non-negative integer `n`, compute its **factorial**, written as `n!`.

The factorial of `n` is defined as the **product of all positive integers from 1 to n**:

```
n! = 1 × 2 × 3 × 4 × ... × n
```

With one special base case:

```
0! = 1          (by mathematical convention — the empty product)
```

---

### Formal Definition

```
Input  : A non-negative integer n
Output : The value of n! = 1 × 2 × 3 × ... × n
```

---

### Example 1

```
Input  : n = 5
Output : Factorial of the number is: 120
```

**Why?**
```
5! = 1 × 2 × 3 × 4 × 5
   = 2 × 3 × 4 × 5
   = 6 × 4 × 5
   = 24 × 5
   = 120  ✅
```

---

### Example 2

```
Input  : n = 0
Output : Factorial of the number is: 1
```

**Why?**
> `0!` = 1 by definition — the **empty product** convention.
> The loop `range(1, 1)` is empty; `factorial` stays at its initial value of 1.

---

### Example 3

```
Input  : n = 1
Output : Factorial of the number is: 1
```

**Why?**
```
1! = 1  (only one multiplication: 1 × 1 = 1)
```

---

### Example 4

```
Input  : n = 10
Output : Factorial of the number is: 3628800
```

```
10! = 1×2×3×4×5×6×7×8×9×10 = 3,628,800
```

---

### Growth of n! at a Glance

| n  | n!                    |
|----|-----------------------|
| 0  | 1                     |
| 1  | 1                     |
| 2  | 2                     |
| 3  | 6                     |
| 4  | 24                    |
| 5  | 120                   |
| 6  | 720                   |
| 7  | 5,040                 |
| 8  | 40,320                |
| 9  | 362,880               |
| 10 | 3,628,800             |
| 20 | 2,432,902,008,176,640,000 |

> Factorial grows **faster than exponential** — it is one of the fastest-growing
> functions in all of mathematics.

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Loop Way (Iterative Thinking)

The most direct interpretation: multiply every integer from 1 up to n into a running product.

```
n = 5

Start : factorial = 1
Step 1: factorial = 1 × 1 = 1
Step 2: factorial = 1 × 2 = 2
Step 3: factorial = 2 × 3 = 6
Step 4: factorial = 6 × 4 = 24
Step 5: factorial = 24 × 5 = 120
```

Think of it as a **rolling multiplication** — just as a running sum adds each new number,
a running product multiplies each new number into the accumulator.

---

#### The Recursive Way (Optimised Thinking)

Notice a natural self-similarity in the factorial definition:

```
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1 × 0!
0! = 1           ← base case; recursion stops here
```

Each factorial is just **n multiplied by the factorial of the previous number**.
This gives us the recurrence relation:

```
n! = n × (n-1)!     for n >= 1
0! = 1              base case
```

Recursion expresses this *exactly* as code mirrors math — but it uses the call stack,
which has a cost.

---

### Part B — Approaches

| Approach   | Strategy                                    | Time  | Space              |
|------------|---------------------------------------------|-------|--------------------|
| Iterative  | Loop from 1 to n, multiply into accumulator | O(n)  | O(1)               |
| Recursive  | Each call returns n × factorial(n-1)        | O(n)  | O(n) — call stack  |

**Edge Cases to Handle**

| Input    | Expected Result | Reason                                                    |
|----------|-----------------|-----------------------------------------------------------|
| `n = 0`  | 1               | Empty product convention; universally accepted in maths   |
| `n = 1`  | 1               | 1! = 1; loop runs once and multiplies by 1                |
| `n < 0`  | Invalid         | Factorial is undefined for negative integers              |
| Large `n`| Very large int  | Python handles arbitrary-precision integers natively      |

---

## 4. Pseudocode

### Iterative (as given in the original code) — O(n) Time, O(1) Space

```
FUNCTION factorial_iterative(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    factorial = 1                       # initialise accumulator (identity for multiplication)

    FOR i FROM 1 TO n (inclusive):
        factorial = factorial × i       # multiply current number into running product

    RETURN factorial
```

---

### Recursive — O(n) Time, O(n) Space

```
FUNCTION factorial_recursive(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    IF n == 0 OR n == 1:               # base cases: 0! = 1 and 1! = 1
        RETURN 1

    RETURN n × factorial_recursive(n - 1)   # recurrence relation: n! = n × (n-1)!
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Factorial of a Number
  Approach : Iterative  → O(n) time, O(1) space
             Recursive  → O(n) time, O(n) space (call stack)
  Author   : Study Notes
=============================================================
"""

import sys


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
# APPROACH 1 — Iterative  O(n) time, O(1) space
# ─────────────────────────────────────────────────────────────

def factorial_iterative(n: int) -> int:
    """
    Compute n! by multiplying each integer from 1 to n into an accumulator.

    Strategy:
        Initialise product at 1 (the multiplicative identity — multiplying
        by 1 changes nothing, just like starting a sum at 0).
        Multiply each integer i in [1, n] into the running product.

    Args:
        n (int): The number whose factorial is required (n >= 0).

    Returns:
        int: The value of n!

    Time  Complexity: O(n) — exactly n multiplications.
    Space Complexity: O(1) — only one extra variable (factorial).
    """
    factorial = 1                       # multiplicative identity: 1 × anything = anything

    for i in range(1, n + 1):          # i goes from 1 to n inclusive
        factorial *= i                  # multiply current integer into running product

    return factorial                    # 0! → loop never runs → returns 1 correctly


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Recursive  O(n) time, O(n) space
# ─────────────────────────────────────────────────────────────

def factorial_recursive(n: int) -> int:
    """
    Compute n! using the natural recursive definition of factorial.

    Recurrence Relation:
        0! = 1                          ← base case (stops recursion)
        1! = 1                          ← base case (stops recursion)
        n! = n × (n-1)!                 ← recursive case

    Args:
        n (int): The number whose factorial is required (n >= 0).

    Returns:
        int: The value of n!

    Time  Complexity: O(n) — n recursive calls, each doing O(1) work.
    Space Complexity: O(n) — n stack frames held in memory simultaneously
                             until the base case is reached and unwinding begins.
    """
    # Base cases: factorial of 0 or 1 is 1 (stops the recursion)
    if n == 0 or n == 1:
        return 1

    # Recursive case: n! = n × (n-1)!
    return n * factorial_recursive(n - 1)


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(n: int, result: int, label: str) -> None:
    """
    Pretty-print the factorial result with context.

    Args:
        n      (int): The value of n entered by the user.
        result (int): The computed factorial.
        label  (str): Approach label for display.
    """
    print(f"\n  [{label}]")

    # Show the full expanded expression for small n
    if n == 0:
        print(f"  0! = 1  (empty product — by mathematical convention)")
    elif n <= 7:
        expression = " × ".join(str(i) for i in range(1, n + 1))
        print(f"  {n}! = {expression}")
    else:
        print(f"  {n}! = 1 × 2 × 3 × ... × {n-1} × {n}")

    print(f"  Factorial of {n} is: {result:,}")

    # Extra contextual note about result size
    digit_count = len(str(result))
    if n >= 10:
        print(f"  ({digit_count} digits long)")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to compute the factorial of a number.

    Options:
        1 → Iterative  (O(n) time, O(1) space)
        2 → Recursive  (O(n) time, O(n) space)
        3 → Both side by side (with consistency check)
        4 → Exit
    """
    # Increase recursion limit for large inputs; Python default is 1000
    sys.setrecursionlimit(10_000)

    print("=" * 54)
    print("   FACTORIAL OF A NUMBER — Study Program")
    print("=" * 54)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Iterative  — O(n) time, O(1) space")
        print("  [2] Recursive  — O(n) time, O(n) space")
        print("  [3] Both       — Compare side by side")
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

        # Warn before running recursion on very large n
        if choice in ("2", "3") and n > 5000:
            print(f"  ⚠  n = {n} is large. Recursion may hit stack limits.\n"
                  f"     Tip: use the Iterative approach for large n.\n")

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = factorial_iterative(n)
            display_result(n, result, "Iterative — O(n) time, O(1) space")

        elif choice == "2":
            try:
                result = factorial_recursive(n)
                display_result(n, result, "Recursive — O(n) time, O(n) space")
            except RecursionError:
                print(f"  ❌ RecursionError: n={n} exceeds Python's stack limit.")
                print(f"     Use the Iterative approach for large n.")

        elif choice == "3":
            iter_result = factorial_iterative(n)
            display_result(n, iter_result, "Iterative — O(n) time, O(1) space")
            try:
                rec_result = factorial_recursive(n)
                display_result(n, rec_result, "Recursive — O(n) time, O(n) space")
                match = "✅ Match" if iter_result == rec_result else "❌ Mismatch!"
                print(f"\n  Consistency check : {match}")
            except RecursionError:
                print(f"\n  ❌ Recursive approach hit stack limit for n={n}.")
                print(f"     Iterative result is still valid: {iter_result:,}")

        print()   # blank line before next menu


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

We use **n = 5** for the iterative approach and trace the full **recursive call stack** for **n = 4**.

---

### Iterative Dry Run — n = 5

| Step | i | factorial Before | Operation         | factorial After | Explanation                       |
|------|---|------------------|-------------------|-----------------|-----------------------------------|
| Init | — | 1                | factorial = 1     | 1               | Start at multiplicative identity  |
| 1    | 1 | 1                | 1 × 1  = 1        | 1               | Multiply by 1 (no change)         |
| 2    | 2 | 1                | 1 × 2  = 2        | 2               | Multiply by 2                     |
| 3    | 3 | 2                | 2 × 3  = 6        | 6               | Multiply by 3                     |
| 4    | 4 | 6                | 6 × 4  = 24       | 24              | Multiply by 4                     |
| 5    | 5 | 24               | 24 × 5 = 120      | 120             | Multiply by 5; loop ends          |
| End  | — | —                | return 120        | —               | **Final Answer: 120 ✅**          |

> Loop ran **5 iterations** — exactly n multiplications.

---

### Iterative Dry Run — n = 0 (Edge Case)

| Step | i | factorial Before | Operation              | factorial After | Explanation                         |
|------|---|------------------|------------------------|-----------------|-------------------------------------|
| Init | — | 1                | factorial = 1          | 1               | Start at multiplicative identity     |
| —    | — | 1                | range(1, 1) → empty    | 1               | Loop body never executes for n = 0  |
| End  | — | —                | return 1               | —               | **Final Answer: 1 ✅ (0! = 1)**      |

---

### Recursive Dry Run — n = 4

#### Winding Phase (calls being made, stack building up)

| Call Depth | Function Call            | Reaches Base Case? | Returns Immediately? | Waiting For         |
|------------|--------------------------|--------------------|----------------------|---------------------|
| 1          | factorial_recursive(4)   | No                 | No                   | factorial_recursive(3) |
| 2          | factorial_recursive(3)   | No                 | No                   | factorial_recursive(2) |
| 3          | factorial_recursive(2)   | No                 | No                   | factorial_recursive(1) |
| 4          | factorial_recursive(1)   | **Yes** (n == 1)   | **Yes → returns 1**  | Nothing             |

> Stack at deepest point holds **4 frames** simultaneously in memory.

---

#### Unwinding Phase (results bubbling back up)

| Call Depth | Function Call          | Receives From Deeper Call | Computes          | Returns to Caller |
|------------|------------------------|---------------------------|-------------------|-------------------|
| 4          | factorial_recursive(1) | — (base case)             | return 1          | Depth 3           |
| 3          | factorial_recursive(2) | received 1                | 2 × 1 = **2**     | Depth 2           |
| 2          | factorial_recursive(3) | received 2                | 3 × 2 = **6**     | Depth 1           |
| 1          | factorial_recursive(4) | received 6                | 4 × 6 = **24**    | Caller (main)     |

> **Final Answer: 24 ✅** &nbsp;|&nbsp; 4! = 4 × 3 × 2 × 1 = 24

---

#### Full Recursive Call Chain Visualised

```
factorial_recursive(4)
└── 4 × factorial_recursive(3)
         └── 3 × factorial_recursive(2)
                  └── 2 × factorial_recursive(1)
                               └── returns 1         ← base case hit

         Unwind:
                  2 × 1  = 2   ↑
         3 × 2  = 6            ↑
4 × 6  = 24                    ↑  ← final answer returned
```

---

### Side-by-Side Comparison — n = 5

| Property              | Iterative                     | Recursive                              |
|-----------------------|-------------------------------|----------------------------------------|
| Steps                 | 5 multiplications             | 5 calls + 5 returns = 10 operations    |
| Stack frames used     | 1 (constant)                  | 5 (one per call level)                 |
| Memory pattern        | Single variable updated       | Call stack grows then shrinks          |
| Final answer          | 120 ✅                        | 120 ✅                                 |
| Preferred for large n | ✅ Yes                        | ❌ Risk of stack overflow               |

---

## 7. Time & Space Complexity

### Iterative Approach

| Case         | Time Complexity | Explanation                                                              |
|--------------|-----------------|--------------------------------------------------------------------------|
| Best Case    | O(n)            | Even n=1 runs the loop once; no early exit exists                        |
| Worst Case   | O(n)            | Loop always runs exactly n iterations with no variability                |
| Average Case | O(n)            | Exactly n multiplications every time — completely deterministic          |

| Space Complexity | O(1) | Only one extra variable (`factorial`) used throughout. Loop variable `i` is also O(1). No recursion, no stack growth. |
|---|---|---|

---

### Recursive Approach

| Case         | Time Complexity | Explanation                                                              |
|--------------|-----------------|--------------------------------------------------------------------------|
| Best Case    | O(1)            | n = 0 or n = 1 hits the base case immediately with zero recursive calls |
| Worst Case   | O(n)            | n recursive calls made, each performing one O(1) multiplication          |
| Average Case | O(n)            | Always exactly n stack frames for any general n                          |

| Space Complexity | O(n) | Each recursive call adds one frame to the call stack. At peak depth (when base case is reached), n frames are alive in memory simultaneously. Stack unwinds only after the base case returns. |
|---|---|---|

---

### Why Recursive Space is O(n) — Visualised

```
Call stack at maximum depth for n = 5:

┌──────────────────────────────┐  ← Top of stack (most recent call)
│  factorial_recursive(1) → 1  │  Frame 5
├──────────────────────────────┤
│  factorial_recursive(2)      │  Frame 4
├──────────────────────────────┤
│  factorial_recursive(3)      │  Frame 3
├──────────────────────────────┤
│  factorial_recursive(4)      │  Frame 2
├──────────────────────────────┤
│  factorial_recursive(5)      │  Frame 1
└──────────────────────────────┘  ← Bottom (original call from main)

n frames deep = O(n) space
```

For n = 10,000: Python would need 10,000 stack frames — this is why `RecursionError`
occurs for large n without adjusting `sys.setrecursionlimit`.

---

### Head-to-Head Summary

| Property         | Iterative | Recursive            |
|------------------|-----------|----------------------|
| Time Complexity  | O(n)      | O(n)                 |
| Space Complexity | **O(1)**  | O(n) — stack frames  |
| Large n safety   | ✅ Safe   | ❌ Stack overflow risk|
| Code clarity     | Moderate  | Mirrors maths exactly|
| Best used when   | Always    | Teaching recursion   |

> Both approaches are O(n) in time — the iterative approach wins decisively on **space**.

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Multiplicative identity = 1**: Always initialise your accumulator at `1` for products,
   just as you initialise at `0` for sums. Starting at `0` would wipe out everything
   (anything × 0 = 0 forever).

2. **Factorial grows insanely fast**: 20! already exceeds 2 × 10¹⁸. Most languages overflow
   at this point — Python does not because it uses arbitrary-precision integers. This is a
   genuine Python superpower for mathematical problems.

3. **Recursion = maths notation in code**: The recursive definition `n! = n × (n-1)!` maps
   directly to the recursive function — one line of code per line of maths. This is the
   canonical example taught when introducing recursion.

4. **Every recursive solution has an iterative twin**: Any recursive factorial can be
   rewritten as a loop. The iterative version is almost always preferred in production
   code due to its O(1) space footprint.

---

### ⚠️ Edge Case Reminders

| Input    | Correct Answer | Common Mistake                                             |
|----------|----------------|------------------------------------------------------------|
| `n = 0`  | 1              | Returning 0 — forgetting the empty product convention      |
| `n = 1`  | 1              | Off-by-one: `range(1, 2)` runs once → multiplies by 1 ✅  |
| `n = 2`  | 2              | Formula: 1 × 2 = 2 ✅                                     |
| `n < 0`  | Invalid        | Factorial is undefined for negatives — always validate     |
| Large n  | Huge integer   | Python handles it; other languages (C, Java) overflow      |

---

### 🔬 The Initialisation Trap

```python
# ❌ Wrong — starting at 0 destroys everything
factorial = 0
for i in range(1, n + 1):
    factorial *= i          # 0 × anything = 0 forever → always returns 0

# ✅ Correct — start at the multiplicative identity
factorial = 1
for i in range(1, n + 1):
    factorial *= i          # builds the product correctly
```

> **Rule**: For running products, always start at `1`. For running sums, always start at `0`.
> These are the *identity elements* for multiplication and addition respectively.

---

### 🔬 Python's Built-in Option

```python
import math

# Python's standard library computes factorial in one call
result = math.factorial(n)    # optimised C implementation — fast and safe
```

> `math.factorial` raises `ValueError` for negative inputs automatically.
> Knowing it exists is useful — but always understand the manual implementation first.

---

### ⚖️ When To Use Which Approach

| Situation                                  | Recommended Approach                      |
|--------------------------------------------|-------------------------------------------|
| Learning factorial / first exposure        | Iterative (most transparent logic)        |
| Learning recursion as a concept            | Recursive (mirrors mathematical definition)|
| Any production or interview code           | Iterative (O(1) space, no stack risk)     |
| n is very large (n > 5,000)               | Iterative only (recursion hits stack limit)|
| Need factorial in real Python code         | `math.factorial(n)` — fastest option      |
| Competitive programming                    | `math.factorial(n)` or iterative          |

---

### 📏 Rules of Thumb

- **Factorial = combinatorics**: `n!` counts the number of ways to arrange n distinct
  items. It appears everywhere: permutations (`n!`), combinations (`n! / (k!(n-k)!)`),
  probability, and Taylor series (`eˣ = Σ xⁿ/n!`).

- **Recursion depth limit**: Python's default recursion limit is 1000. For factorial,
  this means `n > 998` will cause `RecursionError` unless you call
  `sys.setrecursionlimit()`. The iterative approach has no such restriction.

- **`*=` is shorthand**: `factorial *= i` is identical to `factorial = factorial * i`.
  The compound assignment operator (`*=`) is cleaner and preferred.

- **Spot the pattern**: Any loop of the form `for i in range(1, n+1): product *= i`
  is computing `n!`. Recognise it instantly.

- **Tail recursion note**: Python does **not** optimise tail recursion (unlike Haskell
  or Scala). Even a tail-recursive factorial in Python still uses O(n) stack space —
  another reason to prefer the iterative version.

---

### 🔗 Related Problems to Practice Next

| Problem                               | Key Concept Shared                                  |
|---------------------------------------|-----------------------------------------------------|
| Number of permutations (nPr)          | Uses `n! / (n-r)!`                                 |
| Number of combinations (nCr)          | Uses `n! / (k! × (n-k)!)`                         |
| Trailing zeroes in n!                 | Count factors of 5 in n! using `n//5 + n//25 + …` |
| Fibonacci number (recursive)          | Introduces multi-branch recursion                   |
| Tower of Hanoi                        | Classic recursion with exponential complexity       |
| Power of a number (xⁿ)               | Iterative and recursive multiplication              |
| Sum of digits of n! (large numbers)   | Arbitrary-precision integer handling                |

---

*End of Study Notes — Factorial of a Number*