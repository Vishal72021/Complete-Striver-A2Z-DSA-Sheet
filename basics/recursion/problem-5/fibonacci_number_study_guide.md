# 🌀 Nth Fibonacci Number

---

## 1. Name of the Problem

**Nth Fibonacci Number**

> Also known as: *"Fibonacci Sequence"* — one of the most studied sequences in all of
> mathematics, named after the Italian mathematician Leonardo of Pisa (Fibonacci, ~1202).
> It is the **canonical teaching example** for recursion, memoization, dynamic programming,
> and exponential time complexity. It appears in nature (flower petals, shell spirals,
> branching trees), financial modelling, algorithm design, and interview questions at
> every level from beginner to FAANG.

---

## 2. Problem Statement

### What the Code Solves

Given a non-negative integer `n`, find the **nth number** in the Fibonacci sequence.

The Fibonacci sequence is defined by:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)     for n >= 2
```

Each term is the **sum of the two terms immediately before it**.

---

### The Fibonacci Sequence

```
Index:  0   1   2   3   4   5   6   7   8   9   10   11   12
Value:  0   1   1   2   3   5   8   13  21  34  55   89   144
```

> Notice: each value = the sum of the previous two.
> 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8, 5+8=13, and so on.

---

### Formal Definition

```
Input  : A non-negative integer n
Output : The nth Fibonacci number F(n)
```

---

### Example 1

```
Input  : n = 6
Output : Fibonacci number is: 8
```

**Why?**
```
F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8
```

---

### Example 2

```
Input  : n = 10
Output : Fibonacci number is: 55
```

```
F(8)=21,  F(9)=34,  F(10) = 34 + 21 = 55
```

---

### Example 3 — Edge Cases

```
Input  : n = 0  →  Output : 0    (base case — defined as 0)
Input  : n = 1  →  Output : 1    (base case — defined as 1)
Input  : n = 2  →  Output : 1    (0 + 1 = 1; first computed term)
```

---

### Growth of F(n) at a Glance

| n  | F(n)                     | Approx.         |
|----|--------------------------|-----------------|
| 0  | 0                        | —               |
| 1  | 1                        | —               |
| 5  | 5                        | —               |
| 10 | 55                       | —               |
| 20 | 6,765                    | ~6.7K           |
| 30 | 832,040                  | ~832K           |
| 40 | 102,334,155              | ~102M           |
| 50 | 12,586,269,025           | ~12.6B          |
| 100| 354,224,848,179,261,915,075 | ~3.5 × 10²⁰  |

> Fibonacci numbers grow **exponentially** — approximately by the golden ratio
> φ ≈ 1.618 with each step. This is why the naive recursive approach becomes
> catastrophically slow for even moderate values of n.

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Direct Translation (Naive Recursive Thinking)

The problem definition *is* the algorithm — just translate the mathematical recurrence
directly into code:

```
F(n) = F(n-1) + F(n-2)
```

becomes:

```python
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Add the base cases (`n=0` returns 0, `n=1` returns 1) to stop the recursion, and you
have the given code. It is beautiful in its simplicity — but dangerously inefficient.

---

#### Why Naive Recursion is a Trap — The Repeated Work Problem

To compute `F(5)`, the recursion tree looks like this:

```
                    F(5)
                   /    \
               F(4)      F(3)
              /    \    /    \
           F(3)  F(2) F(2)  F(1)
           / \   / \   / \
        F(2) F(1) F(1) F(0) F(1) F(0)
        / \
     F(1) F(0)
```

**F(3) is computed TWICE. F(2) is computed THREE times. F(1) is computed FIVE times.**

For `F(50)`, the number of redundant calls reaches into the billions. This is the
definition of **overlapping subproblems** — the exact condition that makes a problem
a candidate for **dynamic programming**.

---

#### The Smarter Way — Memoization (Top-Down DP)

Store the result of each subproblem the *first* time it is computed. On every subsequent
call for the same `n`, return the cached result instantly instead of recomputing:

```
F(5) called:  compute and cache F(5) = F(4) + F(3)
F(4) called:  compute and cache F(4) = F(3) + F(2)
F(3) called:  compute and cache F(3) = F(2) + F(1)
F(2) called:  compute and cache F(2) = F(1) + F(0) = 1
F(1) called:  base case → 1
F(0) called:  base case → 0

Now F(3) is needed again?  →  Return cached value: 2   (zero recomputation)
Now F(2) is needed again?  →  Return cached value: 1   (zero recomputation)
```

Every unique subproblem is solved exactly **once**. Total unique subproblems: n+1.
Time drops from O(2ⁿ) to O(n).

---

#### The Most Efficient Way — Iterative (Bottom-Up DP)

Start from the base cases and build upward, keeping only the last two values:

```
n = 6

Start:  prev2=F(0)=0,  prev1=F(1)=1

Step 1: curr = 0+1 = 1   → F(2)=1   | prev2=1, prev1=1
Step 2: curr = 1+1 = 2   → F(3)=2   | prev2=1, prev1=2
Step 3: curr = 1+2 = 3   → F(4)=3   | prev2=2, prev1=3
Step 4: curr = 2+3 = 5   → F(5)=5   | prev2=3, prev1=5
Step 5: curr = 3+5 = 8   → F(6)=8   | Answer: 8  ✅
```

No recursion. No call stack. Only two variables maintained at any time. O(1) space.

---

### Part B — Approaches

| Approach          | Strategy                                        | Time   | Space              |
|-------------------|-------------------------------------------------|--------|--------------------|
| Naive Recursive   | Direct recurrence; no caching                   | O(2ⁿ)  | O(n) — call stack  |
| Memoization       | Recursive + cache (top-down DP)                 | O(n)   | O(n) — cache + stack |
| Iterative         | Loop from bottom; only 2 variables (bottom-up)  | O(n)   | O(1)               |

**Edge Cases to Handle**

| Input    | Expected | Reason                                                |
|----------|----------|-------------------------------------------------------|
| `n = 0`  | 0        | First base case — defined by the sequence             |
| `n = 1`  | 1        | Second base case — defined by the sequence            |
| `n = 2`  | 1        | First computed term: F(0)+F(1) = 0+1 = 1             |
| `n < 0`  | Invalid  | Fibonacci undefined for negative integers             |
| Large n  | Very large int | Python handles arbitrary-precision integers; iterative is the only sane approach |

---

## 4. Pseudocode

### Naive Recursive — O(2ⁿ) Time, O(n) Space

```
FUNCTION fibonacci_naive(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    IF n == 0:
        RETURN 0                          # base case 1: F(0) = 0

    IF n == 1:
        RETURN 1                          # base case 2: F(1) = 1

    RETURN fibonacci_naive(n-1) + fibonacci_naive(n-2)   # recurrence
```

---

### Memoization — O(n) Time, O(n) Space

```
cache = {}                                # global dictionary to store computed values

FUNCTION fibonacci_memo(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    IF n == 0:  RETURN 0                  # base case 1
    IF n == 1:  RETURN 1                  # base case 2

    IF n IS IN cache:
        RETURN cache[n]                   # already computed → return instantly

    result      = fibonacci_memo(n-1) + fibonacci_memo(n-2)  # compute once
    cache[n]    = result                  # store for future calls

    RETURN result
```

---

### Iterative (Bottom-Up DP) — O(n) Time, O(1) Space

```
FUNCTION fibonacci_iterative(n):
    IF n < 0:
        PRINT "Invalid input"
        RETURN

    IF n == 0:  RETURN 0                  # handle base case before loop
    IF n == 1:  RETURN 1                  # handle base case before loop

    prev2 = 0                             # F(0) — two steps behind current
    prev1 = 1                             # F(1) — one step behind current

    FOR i FROM 2 TO n (inclusive):
        curr  = prev2 + prev1             # F(i) = F(i-2) + F(i-1)
        prev2 = prev1                     # slide the window forward
        prev1 = curr                      # new "one step behind" is curr

    RETURN prev1                          # prev1 now holds F(n)
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Nth Fibonacci Number
  Approach : Naive Recursive  → O(2ⁿ) time, O(n)  space
             Memoization      → O(n)   time, O(n)  space
             Iterative        → O(n)   time, O(1)  space
  Author   : Study Notes
=============================================================
"""

import sys
import time


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
# APPROACH 1 — Naive Recursive  O(2ⁿ) time, O(n) space
# ─────────────────────────────────────────────────────────────

def fibonacci_naive(n: int) -> int:
    """
    Compute F(n) using direct recursion with no caching whatsoever.

    Strategy:
        Directly translate the mathematical recurrence into code.
        F(n) = F(n-1) + F(n-2), with base cases F(0)=0 and F(1)=1.

    WARNING:
        This approach recomputes the same subproblems exponentially
        many times. For n > 35, runtime becomes noticeably slow.
        For n > 45, it may take minutes. Never use in production.

    Args:
        n (int): The index in the Fibonacci sequence (n >= 0).

    Returns:
        int: The nth Fibonacci number F(n).

    Time  Complexity: O(2ⁿ) — each call spawns two more; tree has ~2ⁿ nodes.
    Space Complexity: O(n)  — maximum call stack depth is n (the longest
                              path from root to leaf in the recursion tree).
    """
    # Base cases — stop the recursion
    if n == 0:
        return 0          # F(0) = 0 by definition
    if n == 1:
        return 1          # F(1) = 1 by definition

    # Recursive case — two calls, each reducing n by 1 or 2
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Memoization (Top-Down DP)  O(n) time, O(n) space
# ─────────────────────────────────────────────────────────────

def fibonacci_memo(n: int, cache: dict | None = None) -> int:
    """
    Compute F(n) using recursion enhanced with a memoization cache.

    Strategy:
        Before computing F(n), check whether the result is already in
        the cache dictionary. If yes, return it immediately (O(1)).
        If no, compute it, store it in the cache, then return it.
        This ensures each unique subproblem is solved exactly once.

    Args:
        n     (int)        : The index in the Fibonacci sequence (n >= 0).
        cache (dict | None): Dictionary mapping n → F(n). Created on first
                             call; passed down through all recursive calls.

    Returns:
        int: The nth Fibonacci number F(n).

    Time  Complexity: O(n)  — each of the n+1 unique subproblems computed once.
    Space Complexity: O(n)  — cache holds up to n+1 entries; call stack up to
                              depth n on the first traversal.
    """
    # Initialise cache on the very first call (default mutable arg pattern avoided)
    if cache is None:
        cache = {}

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Cache hit — return precomputed result immediately
    if n in cache:
        return cache[n]

    # Cache miss — compute, store, and return
    result   = (fibonacci_memo(n - 1, cache)     # left branch
              + fibonacci_memo(n - 2, cache))    # right branch (mostly cache hits)
    cache[n] = result                            # store for any future call with same n

    return result


# ─────────────────────────────────────────────────────────────
# APPROACH 3 — Iterative (Bottom-Up DP)  O(n) time, O(1) space
# ─────────────────────────────────────────────────────────────

def fibonacci_iterative(n: int) -> int:
    """
    Compute F(n) iteratively by building the sequence from the ground up.

    Strategy:
        Start with the two known base values F(0)=0 and F(1)=1.
        Slide a two-variable window forward, computing the next Fibonacci
        number at each step and discarding the oldest value — only the
        most recent two values are ever needed at any point.

    Args:
        n (int): The index in the Fibonacci sequence (n >= 0).

    Returns:
        int: The nth Fibonacci number F(n).

    Time  Complexity: O(n)  — exactly n-1 iterations of the loop.
    Space Complexity: O(1)  — only three variables used regardless of n:
                              prev2, prev1, curr.
    """
    # Base cases handled before the loop
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0    # represents F(i-2); starts as F(0)
    prev1 = 1    # represents F(i-1); starts as F(1)

    # Build forward from F(2) up to F(n)
    for _ in range(2, n + 1):          # loop runs from i=2 to i=n inclusive
        curr  = prev2 + prev1          # F(i) = F(i-2) + F(i-1)
        prev2 = prev1                  # slide: old F(i-1) becomes new F(i-2)
        prev1 = curr                   # slide: new F(i)   becomes new F(i-1)

    return prev1                       # after the loop, prev1 holds F(n)


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(n: int, result: int, label: str,
                   elapsed_ms: float | None = None) -> None:
    """
    Pretty-print the Fibonacci result with context.

    Args:
        n          (int)        : The index n entered by the user.
        result     (int)        : The computed Fibonacci number F(n).
        label      (str)        : Approach label for display.
        elapsed_ms (float|None) : Optional elapsed time in milliseconds.
    """
    print(f"\n  [{label}]")
    print(f"  F({n}) = {result:,}")

    if elapsed_ms is not None:
        print(f"  Time taken : {elapsed_ms:.4f} ms")

    # Contextual notes
    if n == 0:
        print("  Note: F(0) = 0 — first base case by definition.")
    elif n == 1:
        print("  Note: F(1) = 1 — second base case by definition.")
    elif n <= 12:
        # Print the sequence up to F(n) for smaller values
        seq = [0, 1]
        for i in range(2, n + 1):
            seq.append(seq[-1] + seq[-2])
        sequence_str = ", ".join(str(x) for x in seq)
        print(f"  Sequence   : {sequence_str}")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to compute the nth Fibonacci number.

    Options:
        1 → Naive Recursive  (O(2ⁿ) time — for small n only)
        2 → Memoization      (O(n)  time, O(n) space)
        3 → Iterative        (O(n)  time, O(1) space — recommended)
        4 → All Three        — compare results and timing side by side
        5 → Exit
    """
    sys.setrecursionlimit(10_000)   # increase limit for memo approach on large n

    print("=" * 58)
    print("   NTH FIBONACCI NUMBER — Study Program")
    print("=" * 58)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Naive Recursive  — O(2ⁿ) time  ⚠ slow for n > 35")
        print("  [2] Memoization      — O(n)  time, O(n) space")
        print("  [3] Iterative        — O(n)  time, O(1) space ✅ recommended")
        print("  [4] All Three        — Compare results and timing")
        print("  [5] Exit")
        print("-" * 58)

        choice = input("  Enter choice (1/2/3/4/5): ").strip()

        if choice == "5":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, 4, or 5.\n")
            continue

        # ── Get input ─────────────────────────────────────
        n = get_non_negative_integer("\n  Enter a non-negative integer n: ")

        # Safety guard for naive recursion on large n
        if choice in ("1", "4") and n > 40:
            print(f"\n  ⚠  n = {n} will be extremely slow for the Naive Recursive")
            print(f"     approach (O(2ⁿ) ≈ {2**n:,} operations).")
            confirm = input("     Proceed anyway? (y/n): ").strip().lower()
            if confirm != "y":
                print("     Skipping Naive Recursive. Choose option 2 or 3 instead.")
                if choice == "1":
                    print()
                    continue
                choice = "23_only"   # run only memo and iterative in option 4

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            t0     = time.perf_counter()
            result = fibonacci_naive(n)
            elapsed = (time.perf_counter() - t0) * 1000
            display_result(n, result,
                           "Naive Recursive — O(2ⁿ)", elapsed)

        elif choice == "2":
            t0     = time.perf_counter()
            result = fibonacci_memo(n)
            elapsed = (time.perf_counter() - t0) * 1000
            display_result(n, result,
                           "Memoization — O(n) time, O(n) space", elapsed)

        elif choice == "3":
            t0     = time.perf_counter()
            result = fibonacci_iterative(n)
            elapsed = (time.perf_counter() - t0) * 1000
            display_result(n, result,
                           "Iterative — O(n) time, O(1) space", elapsed)

        elif choice in ("4", "23_only"):
            results = {}

            if choice == "4":
                t0 = time.perf_counter()
                results["naive"] = fibonacci_naive(n)
                naive_ms = (time.perf_counter() - t0) * 1000
                display_result(n, results["naive"],
                               "Naive Recursive  — O(2ⁿ)", naive_ms)

            t0 = time.perf_counter()
            results["memo"] = fibonacci_memo(n)
            memo_ms = (time.perf_counter() - t0) * 1000
            display_result(n, results["memo"],
                           "Memoization      — O(n) time, O(n) space", memo_ms)

            t0 = time.perf_counter()
            results["iter"] = fibonacci_iterative(n)
            iter_ms = (time.perf_counter() - t0) * 1000
            display_result(n, results["iter"],
                           "Iterative        — O(n) time, O(1) space", iter_ms)

            # Consistency check
            vals   = list(results.values())
            match  = all(v == vals[0] for v in vals)
            verdict = "✅ All Match" if match else "❌ Mismatch!"
            print(f"\n  Consistency check : {verdict}")

        print()   # blank line before next menu


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

We use **n = 5** across all three approaches, showing every step.

---

### Naive Recursive Dry Run — n = 5

#### Full Recursion Tree

```
                           F(5)
                         /      \
                      F(4)       F(3)─────────────┐
                    /      \         \             |
                 F(3)       F(2)    F(2)          F(1)=1
               /      \    /   \   /   \
            F(2)     F(1) F(1) F(0) F(1) F(0)
           /    \      =1   =1   =0   =1   =0
        F(1)   F(0)
         =1     =0
```

#### Call and Return Table

| Call # | Function Call | Returns | Reason                               |
|--------|---------------|---------|--------------------------------------|
| 1      | F(5)          | —       | Calls F(4) + F(3); waiting           |
| 2      | F(4)          | —       | Calls F(3) + F(2); waiting           |
| 3      | F(3)          | —       | Calls F(2) + F(1); waiting           |
| 4      | F(2)          | —       | Calls F(1) + F(0); waiting           |
| 5      | F(1)          | **1**   | Base case ✅                          |
| 6      | F(0)          | **0**   | Base case ✅                          |
| 7      | F(2)          | **1**   | 1 + 0 = 1                           |
| 8      | F(1)          | **1**   | Base case ✅                          |
| 9      | F(3)          | **2**   | 1 + 1 = 2                           |
| 10     | F(3)          | —       | Calls F(2) + F(1) **AGAIN** ♻️ Redundant! |
| 11     | F(2)          | —       | Calls F(1) + F(0) **AGAIN** ♻️ Redundant! |
| 12     | F(1)          | **1**   | Base case ✅ (computed 3rd time)     |
| 13     | F(0)          | **0**   | Base case ✅ (computed 2nd time)     |
| 14     | F(2)          | **1**   | 1 + 0 = 1  ♻️ Redundant!             |
| 15     | F(1)          | **1**   | Base case ✅ (computed 4th time)     |
| 16     | F(3)          | **2**   | 1 + 1 = 2  ♻️ Redundant!             |
| 17     | F(4)          | **3**   | 2 + 1 = 3                           |
| 18     | F(2)          | —       | Calls F(1) + F(0) **AGAIN** ♻️ Redundant! |
| 19     | F(1)          | **1**   | Base case ✅ (computed 5th time)     |
| 20     | F(0)          | **0**   | Base case ✅ (computed 2nd time)     |
| 21     | F(2)          | **1**   | 1 + 0 = 1  ♻️ Redundant!             |
| 22     | F(3)          | **2**   | 1 + 1 = 2  ♻️ Redundant! computed 3rd time |
| 23     | F(5)          | **5**   | 3 + 2 = 5  ✅ Final Answer           |

> **15 unique-looking calls** to compute F(5) — but only 6 unique subproblems exist:
> F(0), F(1), F(2), F(3), F(4), F(5). Everything else is pure wasted work.

#### Redundancy Summary for n = 5

| Subproblem | Times Computed | Should Be |
|------------|----------------|-----------|
| F(0)       | 3              | 1         |
| F(1)       | 5              | 1         |
| F(2)       | 3              | 1         |
| F(3)       | 2              | 1         |
| F(4)       | 1              | 1         |
| F(5)       | 1              | 1         |
| **Total**  | **15**         | **6**     |

---

### Memoization Dry Run — n = 5

**cache = {}** initially empty.

| Call # | Call        | Cache Before          | Action                            | Returns | Cache After                           |
|--------|-------------|-----------------------|-----------------------------------|---------|---------------------------------------|
| 1      | F(5)        | {}                    | Not in cache → recurse            | —       | —                                     |
| 2      | F(4)        | {}                    | Not in cache → recurse            | —       | —                                     |
| 3      | F(3)        | {}                    | Not in cache → recurse            | —       | —                                     |
| 4      | F(2)        | {}                    | Not in cache → recurse            | —       | —                                     |
| 5      | F(1)        | {}                    | Base case                         | **1**   | {}                                    |
| 6      | F(0)        | {}                    | Base case                         | **0**   | {}                                    |
| 7      | F(2)        | {}                    | 1+0=1; store in cache             | **1**   | {2: 1}                                |
| 8      | F(1)        | {2:1}                 | Base case                         | **1**   | {2: 1}                                |
| 9      | F(3)        | {2:1}                 | 1+1=2; store in cache             | **2**   | {2:1, 3:2}                            |
| 10     | F(2)        | {2:1, 3:2}            | **Cache hit ✅** → return 1       | **1**   | {2:1, 3:2}                            |
| 11     | F(4)        | {2:1, 3:2}            | 2+1=3; store in cache             | **3**   | {2:1, 3:2, 4:3}                       |
| 12     | F(3)        | {2:1, 3:2, 4:3}       | **Cache hit ✅** → return 2       | **2**   | {2:1, 3:2, 4:3}                       |
| 13     | F(5)        | {2:1, 3:2, 4:3}       | 3+2=5; store in cache             | **5**   | {2:1, 3:2, 4:3, 5:5}                 |

> Only **9 calls** vs **23** in naive recursion for the same n=5.
> Every subproblem computed exactly **once**. Cache hits at steps 10 and 12 avoid
> entire subtrees of recomputation.

---

### Iterative Dry Run — n = 5

| Iteration | i | prev2 (F(i-2)) | prev1 (F(i-1)) | curr = prev2 + prev1 | prev2 After | prev1 After | Explanation         |
|-----------|---|----------------|----------------|----------------------|-------------|-------------|---------------------|
| Init      | — | 0              | 1              | —                    | 0           | 1           | F(0)=0, F(1)=1      |
| 1         | 2 | 0              | 1              | 0 + 1 = **1**        | 1           | 1           | F(2) = 1            |
| 2         | 3 | 1              | 1              | 1 + 1 = **2**        | 1           | 2           | F(3) = 2            |
| 3         | 4 | 1              | 2              | 1 + 2 = **3**        | 2           | 3           | F(4) = 3            |
| 4         | 5 | 2              | 3              | 2 + 3 = **5**        | 3           | 5           | F(5) = 5 → done ✅  |
| End       | — | —              | —              | return prev1         | —           | **5**       | **Final Answer ✅** |

> Only **4 iterations** (n-1 = 4) for n=5. Zero recursion. Two variables throughout.

---

### Side-by-Side Comparison — n = 5

| Property               | Naive Recursive | Memoization       | Iterative             |
|------------------------|-----------------|-------------------|-----------------------|
| Total calls/steps      | 23 calls        | 9 calls           | 4 iterations          |
| Unique subproblems     | 6               | 6                 | 4 (no subproblems)    |
| Redundant computations | 15 ♻️           | 0 ✅              | 0 ✅                  |
| Max stack depth        | 5 frames        | 5 frames          | 1 frame (no recursion)|
| Extra memory used      | O(5) stack      | O(5) cache+stack  | O(1) — 3 variables    |
| Final answer           | 5 ✅            | 5 ✅              | 5 ✅                  |

---

## 7. Time & Space Complexity

### Naive Recursive — Direct Recurrence

| Case         | Time Complexity | Explanation                                                                           |
|--------------|-----------------|---------------------------------------------------------------------------------------|
| Best Case    | O(1)            | n = 0 or n = 1 → hits base case immediately; no recursive calls made                 |
| Worst Case   | O(2ⁿ)           | Each call fans into 2 calls; full binary tree of depth n → ~2ⁿ nodes total           |
| Average Case | O(2ⁿ)           | For any general n, the tree is unavoidable — exponential every time                  |

| Space Complexity | O(n) | The call stack reaches maximum depth n (the longest path root→leaf is always n steps deep: F(n)→F(n-1)→F(n-2)→...→F(0)). Width of the tree is exponential but stack only holds one path at a time. |
|---|---|---|

**Exact call count formula:**

```
T(n) = T(n-1) + T(n-2) + 1
     ≈ φⁿ   where φ ≈ 1.618 (golden ratio)

For n=40: ~2.2 billion calls.
For n=50: ~2.25 trillion calls.
```

---

### Memoization — Top-Down DP

| Case         | Time Complexity | Explanation                                                                          |
|--------------|-----------------|--------------------------------------------------------------------------------------|
| Best Case    | O(1)            | n = 0 or n = 1 → base case; or all results already cached from a prior call         |
| Worst Case   | O(n)            | First call: n+1 unique subproblems computed, each exactly once, each O(1) work      |
| Average Case | O(n)            | Always n+1 unique subproblems; cache eliminates all redundancy                      |

| Space Complexity | O(n) | Cache dictionary holds up to n+1 entries (F(0) through F(n)). Call stack reaches depth n on the first traversal before any cache hits occur. Both components are O(n). |
|---|---|---|

---

### Iterative — Bottom-Up DP

| Case         | Time Complexity | Explanation                                                                      |
|--------------|-----------------|----------------------------------------------------------------------------------|
| Best Case    | O(1)            | n = 0 or n = 1 → handled before the loop; zero iterations                       |
| Worst Case   | O(n)            | Loop runs exactly n-1 iterations for any n ≥ 2                                  |
| Average Case | O(n)            | Always exactly n-1 iterations — perfectly deterministic, zero variability        |

| Space Complexity | O(1) | Only three variables: `prev2`, `prev1`, `curr`. No cache, no call stack, no recursion. Entirely constant space regardless of n. |
|---|---|---|

---

### The Exponential Explosion Visualised

```
n  | Naive calls (approx) | Memo calls | Iterative steps
---|----------------------|------------|----------------
5  |          15          |     9      |       4
10 |         177          |    19      |       9
20 |       21,891         |    39      |      19
30 |    2,692,537         |    59      |      29
40 |  331,160,281         |    79      |      39
50 | 40,730,022,147       |    99      |      49
n  |        O(2ⁿ)         |   O(n)     |      O(n)
```

> The naive recursive approach for n=50 makes over **40 trillion calls**.
> The iterative approach makes **49 steps**. This is the starkest possible
> demonstration of why algorithm choice matters.

---

### Head-to-Head Summary

| Property              | Naive Recursive      | Memoization             | Iterative                |
|-----------------------|----------------------|-------------------------|--------------------------|
| Time Complexity       | **O(2ⁿ)** ❌         | O(n) ✅                 | O(n) ✅                  |
| Space Complexity      | O(n) stack           | O(n) cache + stack      | **O(1)** ✅ winner       |
| Redundant work?       | Massive ❌           | None ✅                 | None ✅                  |
| Recursion?            | Yes (deep)           | Yes (depth n)           | No ✅                    |
| Stack overflow risk?  | Yes (large n) ⚠️     | Yes (large n) ⚠️        | Never ✅                 |
| Easiest to read?      | ✅ Mirrors maths     | Moderate                | Moderate                 |
| Best used when        | Teaching recursion only | Learning DP / memoization | Always in practice   |

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Spot overlapping subproblems**: When you see a recursive function that calls
   itself with *different-but-overlapping* arguments (F(n-1) and F(n-2) both eventually
   need F(n-3), F(n-4)...), that's the signal for dynamic programming. Memoization
   is almost always the first fix.

2. **Bottom-up = think in the direction of data flow**: Instead of asking
   *"How do I get F(n) from smaller pieces?"* (top-down), ask
   *"How do I build up from F(0) to F(n)?"* (bottom-up). The loop naturally
   follows the dependency chain in the correct order.

3. **Two variables are enough**: You never need the entire sequence stored.
   F(n) only depends on F(n-1) and F(n-2) — a sliding window of size 2.
   This collapses O(n) space (a full array) to O(1).

4. **Exponential vs linear is not a minor difference**: For n=50, naive recursion
   makes 40 trillion calls. Iterative makes 49 steps. This is not a performance
   tweak — it is the difference between an algorithm that finishes in microseconds
   and one that would run longer than the age of the universe.

5. **The golden ratio connection**: F(n) ≈ φⁿ / √5, where φ = (1+√5)/2 ≈ 1.618.
   This is why the naive recursion tree has ~φⁿ nodes, and why Fibonacci numbers
   grow so rapidly. This also yields an O(1) formula — but with floating-point
   precision issues for large n.

---

### ⚠️ Edge Case Reminders

| Input    | Expected | Common Mistake                                                        |
|----------|----------|-----------------------------------------------------------------------|
| `n = 0`  | 0        | Returning 1 — confusing F(0)=0 with F(1)=1                          |
| `n = 1`  | 1        | Off-by-one in the base cases ✅ — both must be explicitly handled     |
| `n = 2`  | 1        | F(2) = F(1)+F(0) = 1+0 = 1, not 2                                   |
| `n < 0`  | Invalid  | Fibonacci undefined for negatives — always validate input             |
| `n = 35+`| Valid    | Naive recursion becomes visibly slow — warn the user                  |
| `n = 1000+`| Valid  | Use iterative only; both recursive approaches hit Python's stack limit|

---

### 🔬 The Mutable Default Argument Trap

```python
# ❌ DANGEROUS — cache persists across ALL calls forever (Python default arg trap)
def fibonacci_memo(n, cache={}):
    ...

# ✅ SAFE — None sentinel; fresh cache created on each top-level call
def fibonacci_memo(n, cache=None):
    if cache is None:
        cache = {}
    ...
```

> Python evaluates default arguments **once at function definition time**, not
> on each call. Using `cache={}` as a default means the same dictionary object
> is reused across all calls — which is actually useful for persistent caching
> but confusing and error-prone. Using `None` as sentinel is the clean pattern.

---

### 🔬 Python's Built-in and Library Options

```python
from functools import lru_cache

# Option 1: lru_cache decorator — memoization in one line
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Option 2: math.comb-based (Binet's formula — O(1) but float precision issues)
import math
def fib_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(phi**n / math.sqrt(5))   # unreliable for large n

# Option 3: matrix exponentiation — O(log n) time (advanced)
```

> Know these exist, but always understand the manual implementations first.
> `@lru_cache` is the production Python answer; iterative is the interview answer.

---

### ⚖️ When To Use Which Approach

| Situation                                        | Recommended Approach                              |
|--------------------------------------------------|---------------------------------------------------|
| First learning recursion                         | Naive recursive (pure, clear, educational)        |
| Learning dynamic programming / memoization       | Memoization (classic DP introduction)             |
| Any real or production use case                  | Iterative (O(n) time, O(1) space, no stack risk)  |
| n is very small (n ≤ 15)                         | Any approach — all finish instantly               |
| n is moderate (15 < n ≤ 35)                      | Naive is slow; prefer memo or iterative           |
| n is large (n > 35)                              | Iterative only — naive is unusable                |
| n is very large (n > 10,000)                     | Iterative; recursive approaches hit stack limits  |
| Need O(log n) time (very large n, many queries)  | Matrix exponentiation                             |

---

### 📏 Rules of Thumb

- **See exponential recursion? Think DP**: The Fibonacci recursion is the archetypal
  case of *overlapping subproblems* + *optimal substructure* — the two conditions
  that define dynamic programming candidates. Memorise this pattern.

- **Top-down DP (memoization) = recursion + cache**: Add a dictionary, check before
  computing, store after computing. This template applies to dozens of DP problems.

- **Bottom-up DP (iterative) = fill a table in order**: Figure out which subproblems
  need to be solved before the current one, fill them first. For Fibonacci, the
  "table" collapses to just two variables.

- **n // 2 for palindromes, n-1 for Fibonacci**: The iterative loop always runs
  exactly `n-1` times (from i=2 to i=n) — never n, never n+1.

- **Recursion depth limit**: Python's default is 1000. Naive recursion for n=1001
  crashes. Memoization for n=1001 also crashes (depth 1001). Only the iterative
  approach is safe for arbitrarily large n in Python.

---

### 🔗 Related Problems to Practice Next

| Problem                                   | Key Concept Shared                                    |
|-------------------------------------------|-------------------------------------------------------|
| Climbing Stairs (LeetCode 70)             | Identical recurrence: f(n) = f(n-1) + f(n-2)        |
| Min Cost Climbing Stairs (LC 746)         | Fibonacci-style DP with costs                         |
| House Robber (LC 198)                     | Linear DP; two-variable sliding window                |
| Tribonacci Number (LC 1137)               | Extends Fibonacci: f(n) = f(n-1)+f(n-2)+f(n-3)      |
| Longest Common Subsequence                | 2D DP; overlapping subproblems in 2 dimensions        |
| Coin Change (LC 322)                      | DP with overlapping subproblems; bottom-up table      |
| Decode Ways (LC 91)                       | Fibonacci-like recurrence on string indices           |
| Matrix Chain Multiplication               | Classic DP; understanding recursive decomposition     |

---

*End of Study Notes — Nth Fibonacci Number*