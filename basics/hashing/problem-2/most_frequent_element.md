# 🏆 Highest Occurring Element in an Array

---

## 1. Name of the Problem

**Highest Occurring Element in an Array**

> Also known as: *"Most Frequent Element"*, *"Mode of an Array"*, or *"Majority
> Element (generalised)"* — a foundational problem that combines the **hash map
> frequency counting pattern** with a **running maximum tracker**. It is a direct
> extension of the frequency count problem and serves as the entry point to harder
> problems like *Top K Frequent Elements*, *Majority Element (Boyer-Moore Vote)*,
> *Find All Duplicates*, and *Word Frequency Analysis*.

---

## 2. Problem Statement

### What the Code Solves

Given an array of `n` integers, find the **element that appears the most number of
times**. If multiple elements share the highest frequency, return the one encountered
**first** (i.e., whose count reached the maximum earliest during a left-to-right scan).

The code does this in a **single pass**: it builds a frequency map and simultaneously
tracks the current maximum — no second pass needed.

---

### Formal Definition

```
Input  : n integers forming array arr
Output : The element e in arr such that count(e) >= count(x)
         for every other element x in arr.
         On a tie: the element whose count reached the maximum first (leftmost winner).
```

---

### Example 1

```
Input  : n = 7,  arr = [1, 2, 2, 3, 3, 3, 4]
Output : The highest occurring element is: 3
```

**Why?**
```
Frequency: {1: 1,  2: 2,  3: 3,  4: 1}
Maximum frequency: 3  →  element: 3  ✅
```

---

### Example 2

```
Input  : n = 6,  arr = [4, 4, 4, 2, 2, 2]
Output : The highest occurring element is: 4
```

**Why?**
```
Frequency: {4: 3, 2: 3}
Both 4 and 2 appear 3 times — TIE.
4 reached count=3 first (at index 2) → winner is 4.
```

---

### Example 3

```
Input  : n = 5,  arr = [7, 7, 7, 7, 7]
Output : The highest occurring element is: 7
```

> All elements are the same — trivially the only candidate.

---

### Example 4 — Edge Cases

```
Input  : n = 1,  arr = [42]
Output : The highest occurring element is: 42

Input  : n = 3,  arr = [1, 2, 3]
Output : The highest occurring element is: 1
```

> All distinct elements each appear once — the first element wins the tie
> (it reaches count=1 first).

---

### What Happens Internally — Step by Step

For `arr = [3, 1, 3, 2, 1, 3]`:

```
After each element:

Process 3 → hash_map={3:1}  max_count=1  winner=3
Process 1 → hash_map={3:1, 1:1}  max_count=1  winner=3  (tie; 3 stays — '>' not '>=')
Process 3 → hash_map={3:2, 1:1}  max_count=2  winner=3
Process 2 → hash_map={3:2, 1:1, 2:1}  max_count=2  winner=3
Process 1 → hash_map={3:2, 1:2}  max_count=2  winner=3  (tie; 3 stays)
Process 3 → hash_map={3:3, 1:2, 2:1}  max_count=3  winner=3

Final answer: 3  ✅
```

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Two-Pass Way (Brute Force Thinking)

The most straightforward approach is to:
1. Build the full frequency map first (one complete pass).
2. Scan the frequency map to find the key with the highest value (second pass).

```
Pass 1 — Count:  {3: 3, 1: 2, 2: 1}
Pass 2 — Find max:  max({3:3, 1:2, 2:1}, key=lambda x: x[1])  →  element 3
```

This is clear, clean, and completely correct — but requires two passes.

---

#### The One-Pass Way (Optimised Thinking — as given in the code)

The key observation is: **you don't need to wait until counting is done to track
the maximum**. After every single update to the hash map, ask:

> *"Is the count I just updated now the new maximum?"*

If yes — update `max_count` and record the current element as the new winner.
This fuses both passes into a single traversal:

```
arr = [1, 2, 2, 3, 3, 3]

Visit 1 → count[1]=1 → 1 > 0 ✅ → max=1, winner=1
Visit 2 → count[2]=1 → 1 > 1 ❌ → max=1, winner=1
Visit 2 → count[2]=2 → 2 > 1 ✅ → max=2, winner=2
Visit 3 → count[3]=1 → 1 > 2 ❌ → max=2, winner=2
Visit 3 → count[3]=2 → 2 > 2 ❌ → max=2, winner=2
Visit 3 → count[3]=3 → 3 > 2 ✅ → max=3, winner=3

Final: element=3, count=3  ✅
```

Think of it as a **live leaderboard**: as you scan left to right, you update the
scoreboard and immediately promote a new champion the moment anyone overtakes the
current record.

---

#### Why `>` and Not `>=` for Tie Breaking

The condition `hash_map[element] > max_count` uses **strict greater than**:

```
arr = [4, 4, 2, 2, 2]

Visit 4 → count[4]=1 → 1 > 0 ✅ → winner=4
Visit 4 → count[4]=2 → 2 > 1 ✅ → winner=4
Visit 2 → count[2]=1 → 1 > 2 ❌ → winner=4 (unchanged)
Visit 2 → count[2]=2 → 2 > 2 ❌ → winner=4 (TIE: 4 stays)
Visit 2 → count[2]=3 → 3 > 2 ✅ → winner=2

Final: element=2, count=3  ✅
```

Using `>` means the winner only changes when strictly **beaten** — ties preserve
the current champion. Using `>=` would instead give the **last** element to reach
the maximum count, not the first.

---

### Part B — Approaches

| Approach            | Strategy                                          | Time      | Space  |
|---------------------|---------------------------------------------------|-----------|--------|
| Brute Force         | Nested loop: count each element by rescanning     | O(n²)     | O(u)   |
| Two-Pass Hash Map   | Pass 1: build freq map; Pass 2: find max          | O(n)      | O(u)   |
| One-Pass Hash Map   | Build freq map and track max simultaneously       | O(n)      | O(u)   |
| Sorting-Based       | Sort, count runs, track longest run               | O(n log n)| O(1)   |

> `u` = number of unique elements. All hash map approaches are O(n) time —
> the one-pass approach simply has a smaller constant factor (one loop vs two).

**Edge Cases to Handle**

| Input                  | Expected Behaviour                                           |
|------------------------|--------------------------------------------------------------|
| `n = 0`, `arr = []`    | No winner — output "Array is empty"                         |
| `n = 1`                | Single element wins with count = 1                          |
| All elements same      | That one element wins with count = n                        |
| All elements distinct  | First element wins (all tied at count=1; `>` keeps first)   |
| Tie between two        | Element whose count reached the maximum first wins           |
| Negative integers      | Hash map handles negative keys perfectly                     |

---

## 4. Pseudocode

### Brute Force — O(n²) Time, O(u) Space

```
FUNCTION highest_occurring_brute(arr):
    IF arr is empty:
        RETURN None

    max_count = 0
    winner    = None
    visited   = SET()

    FOR each element IN arr:
        IF element IN visited:
            CONTINUE                        # already counted this element

        visited.ADD(element)

        count = 0
        FOR each item IN arr:              # rescan full array
            IF item == element:
                count = count + 1

        IF count > max_count:             # strict: first to reach max wins
            max_count = count
            winner    = element

    RETURN winner
```

---

### Two-Pass Hash Map — O(n) Time, O(u) Space

```
FUNCTION highest_occurring_two_pass(arr):
    IF arr is empty:
        RETURN None

    # Pass 1: Build full frequency map
    freq = {}
    FOR each element IN arr:
        IF element IN freq:
            freq[element] = freq[element] + 1
        ELSE:
            freq[element] = 1

    # Pass 2: Find element with highest frequency
    max_count = 0
    winner    = None
    FOR each element, count IN freq:
        IF count > max_count:             # strict: preserves first-seen winner on tie
            max_count = count
            winner    = element

    RETURN winner
```

---

### One-Pass Hash Map — O(n) Time, O(u) Space (as given in code)

```
FUNCTION highest_occurring_one_pass(arr):
    IF arr is empty:
        RETURN None

    hash_map  = {}                         # frequency dictionary
    max_count = 0                          # current highest frequency seen
    winner    = None                       # element holding the current record

    FOR each element IN arr:
        IF element IN hash_map:
            hash_map[element] = hash_map[element] + 1
        ELSE:
            hash_map[element] = 1          # first occurrence

        IF hash_map[element] > max_count:  # new record set?
            max_count = hash_map[element]  # update the record
            winner    = element            # crown new champion

    RETURN winner
```

---

### Sorting-Based — O(n log n) Time, O(1) Space

```
FUNCTION highest_occurring_sorting(arr):
    IF arr is empty:
        RETURN None

    sorted_arr = SORT(arr)

    max_count     = 1
    current_count = 1
    winner        = sorted_arr[0]

    FOR i FROM 1 TO len(sorted_arr) - 1:
        IF sorted_arr[i] == sorted_arr[i-1]:
            current_count = current_count + 1    # extend current run
        ELSE:
            current_count = 1                    # reset for new element

        IF current_count > max_count:
            max_count = current_count
            winner    = sorted_arr[i]

    RETURN winner
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Highest Occurring Element in an Array
  Approach : Brute Force       → O(n²)      time, O(u) space
             Two-Pass Hash Map → O(n)       time, O(u) space
             One-Pass Hash Map → O(n)       time, O(u) space
             Sorting-Based     → O(n log n) time, O(1) space
  Author   : Study Notes
=============================================================
"""

import collections


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


def get_integer(prompt: str) -> int:
    """
    Repeatedly prompt until the user enters any valid integer.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        int: Any valid integer (positive, negative, or zero).
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a whole number.\n")


# ─────────────────────────────────────────────────────────────
# HELPER — Collect array elements from user
# ─────────────────────────────────────────────────────────────

def read_array(n: int) -> list[int]:
    """
    Read n integers from the user and return them as a list.

    Args:
        n (int): Number of elements to read.

    Returns:
        list[int]: The array entered by the user.
    """
    arr = []
    print(f"\n  Enter {n} element(s), one per line:")
    for i in range(n):
        element = get_integer(f"    arr[{i}] = ")
        arr.append(element)
    return arr


# ─────────────────────────────────────────────────────────────
# APPROACH 1 — Brute Force  O(n²) time, O(u) space
# ─────────────────────────────────────────────────────────────

def highest_occurring_brute(arr: list[int]) -> int | None:
    """
    Find the most frequent element using a nested loop.

    Strategy:
        For each unique element, rescan the entire array to count its
        occurrences. Track the element with the highest count seen so far.
        Uses a 'visited' set to avoid recounting the same element.
        Tie-breaking: the first element (by first-encounter order) to
        achieve the maximum count wins, because we use strict '>' for updates.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int | None: The most frequent element, or None if arr is empty.

    Time  Complexity: O(n²) — u unique elements × n inner scans = u×n ≤ n².
    Space Complexity: O(u)  — visited set and freq result, each of size u.
    """
    if not arr:
        return None

    max_count = 0
    winner    = None
    visited   : set[int] = set()

    for element in arr:
        if element in visited:
            continue                            # already counted; skip outer loop

        visited.add(element)                    # mark as counted

        count = 0
        for item in arr:                        # inner scan: count occurrences
            if item == element:
                count += 1

        if count > max_count:                   # strict: first to reach max wins
            max_count = count
            winner    = element

    return winner


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Two-Pass Hash Map  O(n) time, O(u) space
# ─────────────────────────────────────────────────────────────

def highest_occurring_two_pass(arr: list[int]) -> int | None:
    """
    Find the most frequent element using two separate passes.

    Strategy:
        Pass 1 — Build the complete frequency dictionary.
        Pass 2 — Iterate over the dictionary to find the key with max value.
        Using strict '>' preserves the first-seen winner on ties (since dict
        preserves insertion order in Python 3.7+ and we use strict >).

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int | None: The most frequent element, or None if arr is empty.

    Time  Complexity: O(n)  — two linear passes; each O(n) → O(n) total.
    Space Complexity: O(u)  — frequency dict holds u entries.
    """
    if not arr:
        return None

    # ── Pass 1: Build frequency map ───────────────────────
    freq: dict[int, int] = {}
    for element in arr:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1                   # initialise on first encounter

    # ── Pass 2: Find element with maximum frequency ───────
    max_count = 0
    winner    = None
    for element, count in freq.items():
        if count > max_count:                   # strict: first max wins
            max_count = count
            winner    = element

    return winner


# ─────────────────────────────────────────────────────────────
# APPROACH 3 — One-Pass Hash Map  O(n) time, O(u) space
# ─────────────────────────────────────────────────────────────

def highest_occurring_one_pass(arr: list[int]) -> int | None:
    """
    Find the most frequent element in a single pass with live max tracking.

    Strategy:
        Traverse the array once. After each frequency update, immediately
        check whether the updated element has broken the current record.
        If yes, crown it the new winner on the spot.

        This fuses the frequency-building and max-finding phases into a
        single O(n) loop — no second pass required.

        Tie-breaking: strict '>' means the first element to reach
        the maximum count retains the title if later elements tie it.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int | None: The most frequent element, or None if arr is empty.

    Time  Complexity: O(n) — exactly one pass; each dict op is O(1) average.
    Space Complexity: O(u) — hash_map holds u entries (u = unique elements).
    """
    if not arr:
        return None

    hash_map  : dict[int, int] = {}             # frequency store
    max_count : int             = 0             # highest count seen so far
    winner    : int | None      = None          # element holding the record

    for element in arr:
        # ── Update frequency ──────────────────────────────
        if element in hash_map:
            hash_map[element] += 1              # seen before → increment
        else:
            hash_map[element] = 1              # first time → initialise

        # ── Live max check ────────────────────────────────
        # Performed immediately after every update — no second pass needed
        if hash_map[element] > max_count:       # new record achieved?
            max_count = hash_map[element]       # update the record
            winner    = element                 # crown the new champion

    return winner


# ─────────────────────────────────────────────────────────────
# APPROACH 4 — Sorting-Based  O(n log n) time, O(1) space
# ─────────────────────────────────────────────────────────────

def highest_occurring_sorting(arr: list[int]) -> int | None:
    """
    Find the most frequent element by sorting and counting consecutive runs.

    Strategy:
        Sorting groups all duplicate values together into contiguous runs.
        A single left-to-right scan then finds the longest run.
        No hash map needed — O(1) extra space beyond the sorted copy.

        Tie-breaking: the element whose run appears first (lowest value,
        since sorted ascending) wins on a tie — different tie-breaking
        from the hash map approaches.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int | None: The most frequent element, or None if arr is empty.

    Time  Complexity: O(n log n) — sort dominates; the run-counting scan is O(n).
    Space Complexity: O(n) for sorted copy; O(1) extra working variables.
    """
    if not arr:
        return None

    sorted_arr    = sorted(arr)                 # sort a copy; original untouched

    max_count     = 1                           # best run length found
    current_count = 1                           # length of the current run
    winner        = sorted_arr[0]              # best element found so far

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i - 1]: # same as previous? extend run
            current_count += 1
        else:
            current_count = 1                  # new element; reset run counter

        if current_count > max_count:           # new record?
            max_count = current_count
            winner    = sorted_arr[i]

    return winner


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(
    arr     : list[int],
    winner  : int | None,
    label   : str
) -> None:
    """
    Pretty-print the result with frequency context and a visual bar chart.

    Args:
        arr    (list[int]) : The original input array.
        winner (int|None)  : The most frequent element found.
        label  (str)       : Approach label for display.
    """
    print(f"\n  [{label}]")

    if winner is None:
        print("  (Empty array — no result)")
        return

    # Rebuild freq for display (independent of which approach was used)
    freq = {}
    for element in arr:
        freq[element] = freq.get(element, 0) + 1

    print(f"\n  {'Element':>10}  {'Count':>7}  Bar")
    print(f"  {'-'*10}  {'-'*7}  {'-'*20}")
    for element, count in freq.items():
        marker = " ← 🏆 WINNER" if element == winner else ""
        bar    = "█" * count
        print(f"  {element:>10}  {count:>7}  {bar}{marker}")

    print(f"\n  Highest occurring element : {winner}")
    print(f"  Frequency                 : {freq[winner]} time(s) out of {len(arr)}")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to find the highest occurring element.

    Options:
        1 → Brute Force        (O(n²)      — nested loop scan)
        2 → Two-Pass Hash Map  (O(n)       — build map then find max)
        3 → One-Pass Hash Map  (O(n)       — live max tracking ✅ recommended)
        4 → Sorting-Based      (O(n log n) — sort then count runs)
        5 → All Four           — compare all approaches side by side
        6 → Exit
    """
    print("=" * 62)
    print("   HIGHEST OCCURRING ELEMENT — Study Program")
    print("=" * 62)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force       — O(n²)      nested loop")
        print("  [2] Two-Pass Hash Map — O(n)       build then find max")
        print("  [3] One-Pass Hash Map — O(n)       live max tracking ✅")
        print("  [4] Sorting-Based     — O(n log n) sort then count runs")
        print("  [5] All Four          — Compare side by side")
        print("  [6] Exit")
        print("-" * 62)

        choice = input("  Enter choice (1/2/3/4/5/6): ").strip()

        if choice == "6":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("  ⚠  Invalid choice. Enter 1–6.\n")
            continue

        # ── Get input ─────────────────────────────────────
        n = get_non_negative_integer("\n  Enter the number of elements (n): ")

        if n == 0:
            print("\n  [Result] Empty array → no highest occurring element.")
            print()
            continue

        arr = read_array(n)

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = highest_occurring_brute(arr)
            display_result(arr, result,
                           "Brute Force — O(n²)")

        elif choice == "2":
            result = highest_occurring_two_pass(arr)
            display_result(arr, result,
                           "Two-Pass Hash Map — O(n)")

        elif choice == "3":
            result = highest_occurring_one_pass(arr)
            display_result(arr, result,
                           "One-Pass Hash Map — O(n)")

        elif choice == "4":
            result = highest_occurring_sorting(arr)
            display_result(arr, result,
                           "Sorting-Based — O(n log n)")

        elif choice == "5":
            r1 = highest_occurring_brute(arr)
            r2 = highest_occurring_two_pass(arr)
            r3 = highest_occurring_one_pass(arr)
            r4 = highest_occurring_sorting(arr)

            display_result(arr, r1, "Brute Force       — O(n²)")
            display_result(arr, r2, "Two-Pass Hash Map — O(n)")
            display_result(arr, r3, "One-Pass Hash Map — O(n)")
            display_result(arr, r4, "Sorting-Based     — O(n log n)")

            # Note: sorting may produce different winner on ties
            hash_agree = (r1 == r2 == r3)
            print(f"\n  Hash-based approaches agree : "
                  f"{'✅ Yes' if hash_agree else '❌ No (tie-break differs)'}")
            print(f"  Sorting approach winner     : {r4}")
            print(f"  (Tie-break rule may differ between hash and sort approaches)")

        print()   # blank line before next menu


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

We use **arr = [1, 2, 2, 3, 3, 3, 1]** (n = 7) across all approaches,
and **arr = [4, 4, 2, 2, 2]** to demonstrate tie-breaking.

---

### Brute Force Dry Run — arr = [1, 2, 2, 3, 3, 3, 1]

#### Outer Loop — Unique Elements Encountered in Order: 1, 2, 3

**Pass 1 — Counting element `1`:**

| Inner i | arr[i] | arr[i]==1? | count | Action               |
|---------|--------|------------|-------|----------------------|
| 0       | 1      | ✅         | 1     | Match                |
| 1       | 2      | ❌         | 1     | —                    |
| 2       | 2      | ❌         | 1     | —                    |
| 3       | 3      | ❌         | 1     | —                    |
| 4       | 3      | ❌         | 1     | —                    |
| 5       | 3      | ❌         | 1     | —                    |
| 6       | 1      | ✅         | 2     | Match                |

> count=2 > max_count=0 ✅ → **max_count=2, winner=1**

**Pass 2 — Counting element `2`:**

| Inner i | arr[i] | arr[i]==2? | count |
|---------|--------|------------|-------|
| 0       | 1      | ❌         | 0     |
| 1       | 2      | ✅         | 1     |
| 2       | 2      | ✅         | 2     |
| 3–6     | —      | ❌         | 2     |

> count=2 > max_count=2? ❌ (equal, not greater) → **winner stays: 1**

**Pass 3 — Counting element `3`:**

| Inner i | arr[i] | arr[i]==3? | count |
|---------|--------|------------|-------|
| 0–2     | —      | ❌         | 0     |
| 3       | 3      | ✅         | 1     |
| 4       | 3      | ✅         | 2     |
| 5       | 3      | ✅         | 3     |
| 6       | 1      | ❌         | 3     |

> count=3 > max_count=2 ✅ → **max_count=3, winner=3**

#### Brute Force Final Summary

| Outer element | visited? | Inner scan | count | count > max? | max_count | winner |
|---------------|----------|------------|-------|--------------|-----------|--------|
| 1 (idx 0)     | New      | 7 ops      | 2     | 2>0 ✅       | 2         | 1      |
| 2 (idx 1)     | New      | 7 ops      | 2     | 2>2 ❌       | 2         | 1      |
| 2 (idx 2)     | Visited  | 0 ops      | —     | —            | 2         | 1      |
| 3 (idx 3)     | New      | 7 ops      | 3     | 3>2 ✅       | 3         | **3**  |
| 3 (idx 4,5)   | Visited  | 0 ops each | —     | —            | 3         | 3      |
| 1 (idx 6)     | Visited  | 0 ops      | —     | —            | 3         | 3      |

> Total inner scans: 3 unique elements × 7 = **21 operations**.
> **Final answer: 3** ✅

---

### Two-Pass Hash Map Dry Run — arr = [1, 2, 2, 3, 3, 3, 1]

#### Pass 1 — Build Frequency Map

| Step | i | element | element in freq? | Operation       | freq After                    |
|------|---|---------|------------------|-----------------|-------------------------------|
| 1    | 0 | 1       | ❌ No            | freq[1] = 1     | {1: 1}                        |
| 2    | 1 | 2       | ❌ No            | freq[2] = 1     | {1: 1, 2: 1}                  |
| 3    | 2 | 2       | ✅ Yes           | freq[2] += 1→2  | {1: 1, 2: 2}                  |
| 4    | 3 | 3       | ❌ No            | freq[3] = 1     | {1: 1, 2: 2, 3: 1}            |
| 5    | 4 | 3       | ✅ Yes           | freq[3] += 1→2  | {1: 1, 2: 2, 3: 2}            |
| 6    | 5 | 3       | ✅ Yes           | freq[3] += 1→3  | {1: 1, 2: 2, 3: 3}            |
| 7    | 6 | 1       | ✅ Yes           | freq[1] += 1→2  | {1: 2, 2: 2, 3: 3}            |

#### Pass 2 — Find Maximum

| Step | element | count | count > max_count? | max_count | winner     |
|------|---------|-------|--------------------|-----------|------------|
| Init | —       | —     | —                  | 0         | None       |
| 1    | 1       | 2     | 2 > 0 ✅           | 2         | 1          |
| 2    | 2       | 2     | 2 > 2 ❌           | 2         | 1 (stays)  |
| 3    | 3       | 3     | 3 > 2 ✅           | 3         | **3**      |

> **Final answer: 3** ✅ — 7 ops (pass 1) + 3 ops (pass 2) = **10 total operations**.

---

### One-Pass Hash Map Dry Run — arr = [1, 2, 2, 3, 3, 3, 1]

| Step | i | element | hash_map Before         | Op               | hash_map After          | hash_map[e] > max? | max_count | winner |
|------|---|---------|-------------------------|------------------|-------------------------|--------------------|-----------|--------|
| Init | — | —       | {}                      | —                | {}                      | —                  | 0         | None   |
| 1    | 0 | 1       | {}                      | freq[1]=1        | {1:1}                   | 1>0 ✅             | 1         | 1      |
| 2    | 1 | 2       | {1:1}                   | freq[2]=1        | {1:1, 2:1}              | 1>1 ❌             | 1         | 1      |
| 3    | 2 | 2       | {1:1, 2:1}              | freq[2]+=1→2     | {1:1, 2:2}              | 2>1 ✅             | 2         | 2      |
| 4    | 3 | 3       | {1:1, 2:2}              | freq[3]=1        | {1:1, 2:2, 3:1}         | 1>2 ❌             | 2         | 2      |
| 5    | 4 | 3       | {1:1, 2:2, 3:1}         | freq[3]+=1→2     | {1:1, 2:2, 3:2}         | 2>2 ❌             | 2         | 2      |
| 6    | 5 | 3       | {1:1, 2:2, 3:2}         | freq[3]+=1→3     | {1:1, 2:2, 3:3}         | 3>2 ✅             | 3         | **3**  |
| 7    | 6 | 1       | {1:1, 2:2, 3:3}         | freq[1]+=1→2     | {1:2, 2:2, 3:3}         | 2>3 ❌             | 3         | 3      |
| End  | — | —       | —                       | return winner    | —                       | —                  | 3         | **3** ✅|

> Only **7 steps** (one per element). Max updated at steps 1, 3, and 6.
> **Final answer: 3** ✅

---

### Tie-Breaking Dry Run — arr = [4, 4, 2, 2, 2] (One-Pass)

> Both 4 and 2 do NOT tie here (2 wins with count 3 vs 4's count 2).
> Use **arr = [4, 4, 4, 2, 2, 2]** to show a true tie:

| Step | i | element | Op           | hash_map          | [e] > max? | max | winner    |
|------|---|---------|--------------|-------------------|------------|-----|-----------|
| 1    | 0 | 4       | freq[4]=1    | {4:1}             | 1>0 ✅     | 1   | 4         |
| 2    | 1 | 4       | freq[4]+=1→2 | {4:2}             | 2>1 ✅     | 2   | 4         |
| 3    | 2 | 4       | freq[4]+=1→3 | {4:3}             | 3>2 ✅     | 3   | 4         |
| 4    | 3 | 2       | freq[2]=1    | {4:3, 2:1}        | 1>3 ❌     | 3   | 4 (stays) |
| 5    | 4 | 2       | freq[2]+=1→2 | {4:3, 2:2}        | 2>3 ❌     | 3   | 4 (stays) |
| 6    | 5 | 2       | freq[2]+=1→3 | {4:3, 2:3}        | 3>3 ❌     | 3   | **4** ✅  |

> Both 4 and 2 have count=3. Because `>` (not `>=`) is used, 4 keeps the title
> when 2 ties it at step 6. **First to reach the maximum wins.**

---

### Sorting-Based Dry Run — arr = [1, 2, 2, 3, 3, 3, 1]

#### Step 1 — Sort

```
Original : [1, 2, 2, 3, 3, 3, 1]
Sorted   : [1, 1, 2, 2, 3, 3, 3]
```

#### Step 2 — Count Runs

| i | sorted[i] | sorted[i-1] | Same? | current_count | current_count > max? | max_count | winner |
|---|-----------|-------------|-------|---------------|----------------------|-----------|--------|
| Init | —      | —           | —     | 1             | —                    | 1         | 1      |
| 1  | 1         | 1           | ✅    | 2             | 2>1 ✅               | 2         | 1      |
| 2  | 2         | 1           | ❌    | 1 (reset)     | 1>2 ❌               | 2         | 1      |
| 3  | 2         | 2           | ✅    | 2             | 2>2 ❌               | 2         | 1      |
| 4  | 3         | 2           | ❌    | 1 (reset)     | 1>2 ❌               | 2         | 1      |
| 5  | 3         | 3           | ✅    | 2             | 2>2 ❌               | 2         | 1      |
| 6  | 3         | 3           | ✅    | 3             | 3>2 ✅               | 3         | **3**  |

> **Final answer: 3** ✅

---

### Side-by-Side Comparison — arr = [1, 2, 2, 3, 3, 3, 1]

| Property               | Brute Force | Two-Pass Hash | One-Pass Hash | Sorting       |
|------------------------|-------------|---------------|---------------|---------------|
| Total operations       | 21          | 10            | 7             | n log n + n   |
| Passes through array   | u+1 = 4     | 2             | **1** ✅      | 1 sort + 1 scan|
| max_count updates      | 2           | 2             | 3             | 2             |
| Extra data structures  | dict + set  | dict          | dict          | none          |
| Tie-breaking rule      | First seen  | First seen    | First seen    | Lowest value (sorted order) |
| Final answer           | 3 ✅         | 3 ✅           | 3 ✅           | 3 ✅           |

---

## 7. Time & Space Complexity

### Brute Force — Nested Loop

| Case         | Time Complexity | Explanation                                                                  |
|--------------|-----------------|------------------------------------------------------------------------------|
| Best Case    | O(n)            | All elements identical → u=1 unique element → 1 inner scan of length n      |
| Worst Case   | O(n²)           | All elements distinct → u=n → n inner scans × n ops each = n²               |
| Average Case | O(n × u)        | u unique elements × n inner-loop ops each; u ≤ n so worst case is O(n²)     |

| Space Complexity | O(u) | `visited` set and tracking variables; u ≤ n entries. |
|---|---|---|

---

### Two-Pass Hash Map

| Case         | Time Complexity | Explanation                                                                 |
|--------------|-----------------|-----------------------------------------------------------------------------|
| Best Case    | O(n)            | Pass 1: n dict ops. Pass 2: u ≤ n dict iterations. Both O(n). Total O(n)  |
| Worst Case   | O(n)            | Same two-pass structure regardless of values; no variability                |
| Average Case | O(n)            | Always exactly n + u ≤ 2n operations → O(n)                               |

| Space Complexity | O(u) | Frequency dictionary holds u ≤ n entries. |
|---|---|---|

---

### One-Pass Hash Map

| Case         | Time Complexity | Explanation                                                                  |
|--------------|-----------------|------------------------------------------------------------------------------|
| Best Case    | O(n)            | Always traverses all n elements once; no early exit                          |
| Worst Case   | O(n)            | Exactly n dictionary operations regardless of array content                  |
| Average Case | O(n)            | Single pass; n updates; n max-checks; all O(1) each → O(n) total            |

| Space Complexity | O(u) | hash_map dictionary holds u entries; three scalar variables (O(1)). |
|---|---|---|

---

### Sorting-Based

| Case         | Time Complexity | Explanation                                                                 |
|--------------|-----------------|-----------------------------------------------------------------------------|
| Best Case    | O(n log n)      | Sort always costs O(n log n); run-counting scan is O(n) — absorbed          |
| Worst Case   | O(n log n)      | Sort dominates regardless of array content                                  |
| Average Case | O(n log n)      | Completely determined by the sort step                                       |

| Space Complexity | O(n) | `sorted()` creates a new array copy of size n. In-place `arr.sort()` would be O(1) extra but modifies the original. |
|---|---|---|

---

### Complete Head-to-Head Summary

| Property              | Brute Force | Two-Pass Hash | One-Pass Hash   | Sorting-Based  |
|-----------------------|-------------|---------------|-----------------|----------------|
| Time Complexity       | O(n²) ❌    | O(n) ✅       | **O(n)** ✅     | O(n log n)     |
| Space Complexity      | O(u)        | O(u)          | O(u)            | O(n)           |
| Number of passes      | u+1         | 2             | **1** ✅        | 1 sort + 1 scan|
| Loop count updated?   | After each full scan | After pass 1 | After each element ✅ | After each element |
| Tie-breaking rule     | First-seen  | First-seen    | First-seen      | Smallest value (sorted) |
| Safe for large n?     | ❌ Slow     | ✅ Yes        | ✅ Yes          | ✅ Yes         |
| Extra memory needed?  | dict + set  | dict          | dict            | sorted copy    |

---

### Why One-Pass Beats Two-Pass (Constant Factor)

```
Two-pass for n=1,000,000:
  Pass 1: 1,000,000 dict operations
  Pass 2: up to 1,000,000 dict iterations
  Total : ~2,000,000 operations

One-pass for n=1,000,000:
  1 pass: 1,000,000 dict updates + 1,000,000 max comparisons (fused)
  Total : ~1,000,000 operations (same loop body)

Both O(n), but one-pass has roughly half the constant factor.
For cache-sensitive workloads, one-pass also has better data locality.
```

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Running max = update and check in one place**: The one-pass approach is a
   masterclass in fusing two separate concerns — counting and maximising — into
   one loop body. Any time you find yourself computing a table then scanning it
   for a max/min, ask: *"Can I track the max live as I build the table?"*

2. **`>` vs `>=` controls tie-breaking entirely**: This single character determines
   which element wins when two elements share the same highest frequency:
```
   >  → first element to reach the max keeps the crown (given code's behaviour)
   >= → last element to reach the max wins (later arrivals steal the title)
```
   Always clarify tie-breaking rules in interviews before coding.

3. **Initialise `max_count = 0` and `winner = None`**: Starting at 0 guarantees
   the first element always triggers an update (`count=1 > 0`), correctly seeding
   the tracker. Starting at -1 also works for count but is less intuitive.

4. **Frequency problems are hash map problems**: Any problem asking for "most
   frequent", "least frequent", "k most common", or "first non-repeating" is
   almost certainly solved with a frequency dictionary as the first step.

5. **The answer is always in the hash map values**: After building `freq`, finding
   the most frequent element is `max(freq, key=freq.get)` — O(n) in one line.
   But understanding the manual one-pass approach is what interviewers want.

---

### ⚠️ Edge Case Reminders

| Input                   | Expected Result           | Common Mistake                                     |
|-------------------------|---------------------------|----------------------------------------------------|
| `n = 0`, `arr = []`     | None / "empty"            | Crashing on `sorted_arr[0]` or unguarded `None`    |
| `n = 1`                 | That element, count=1     | Works correctly — first update sets winner         |
| All elements same       | That element, count=n     | Works — one key updated n times                    |
| All elements distinct   | First element, count=1    | All tie at count=1; `>` keeps the first winner     |
| `[4, 4, 2, 2, 2]`       | 2 (count=3)               | Make sure 4 doesn't win — it's only count=2        |
| `[4, 4, 4, 2, 2, 2]`    | 4 (tie; first to reach 3) | 4 reaches count=3 first; 2 only ties later         |
| Negative elements       | Works correctly           | Dict handles negative integer keys perfectly        |

---

### 🔬 Four Ways to Find the Most Frequent Element

```python
arr = [1, 2, 2, 3, 3, 3]

# Method 1: One-pass manual (given code — most instructive)
hash_map, max_count, winner = {}, 0, None
for e in arr:
    hash_map[e] = hash_map.get(e, 0) + 1
    if hash_map[e] > max_count:
        max_count, winner = hash_map[e], e

# Method 2: Two-pass with max() on dict
from collections import Counter
freq   = Counter(arr)
winner = max(freq, key=freq.get)              # returns key with highest value

# Method 3: Counter.most_common(1) — most Pythonic
winner = Counter(arr).most_common(1)[0][0]    # [0]=first tuple, [0]=element

# Method 4: max with arr.count (O(n²) — worst)
winner = max(set(arr), key=arr.count)         # arr.count is O(n) per call

# All produce: 3  ✅
```

> `Counter.most_common(1)` is the production one-liner. The manual one-pass
> is what interviewers want to see — it proves you understand the algorithm.

---

### 🔬 The `max(freq, key=freq.get)` Idiom Explained

```python
freq = {1: 2, 2: 2, 3: 3}

# max() iterates over keys: 1, 2, 3
# For each key k, evaluates freq.get(k) as the sort key
# Returns the key k with the highest freq.get(k) value

winner = max(freq, key=freq.get)
# Evaluates: max over (freq.get(1)=2, freq.get(2)=2, freq.get(3)=3)
# → 3 wins  ✅

# On tie: max() returns the LAST tied key (opposite of the one-pass '>' rule)
freq = {1: 3, 2: 3}
max(freq, key=freq.get)   # → 2 (last key to tie wins with max())
# vs one-pass '>' → 1 (first to reach the max wins)
```

> **Critical insight**: `max(freq, key=freq.get)` has **different tie-breaking**
> from the one-pass approach. Always check which rule the problem requires.

---

### ⚖️ When To Use Which Approach

| Situation                                           | Recommended Approach                          |
|-----------------------------------------------------|-----------------------------------------------|
| Interview — show understanding of the pattern       | One-Pass Hash Map (manual, clear, O(n))       |
| Production Python code                              | `Counter(arr).most_common(1)[0][0]`           |
| Need sorted output by frequency                     | `Counter(arr).most_common()` (sorted desc)    |
| Memory is strictly constrained                      | Sorting-Based (O(1) extra, O(n log n) time)   |
| Teaching nested loops and O(n²)                     | Brute Force (demonstration only)              |
| Top-K most frequent (not just top-1)               | `Counter.most_common(k)` or min-heap          |
| Streaming data (can't store full array)             | One-Pass Hash Map (process element by element)|

---

### 📏 Rules of Thumb

- **One-pass = fuse the computation**: Whenever you find yourself writing
  "build a table, then scan the table", ask if you can maintain the answer
  as a running variable updated inside the first loop. This pattern reduces
  code, reduces passes, and reduces cache misses.

- **`max_count = 0` not `max_count = -1`**: Frequencies are always ≥ 1,
  so initialising to 0 correctly seeds the tracker — the first element
  always triggers `count=1 > 0` and becomes the initial winner.

- **`>` for "first wins", `>=` for "last wins"**: This is a universal rule
  in running-max trackers. Choose deliberately.

- **Generalise to k most frequent**: `Counter.most_common(k)` runs in O(n + k log u)
  time using a heap internally. For k=1, it's O(n) — same as the one-pass approach.

- **Frequency of frequencies**: Sometimes problems ask "how many elements appear
  exactly k times?" — build the frequency map, then build a second map of
  `{count: how_many_elements_have_that_count}`. This is a common pattern
  in problems like *Top K Frequent Elements* with bucket sort.

---

### 🔗 Related Problems to Practice Next

| Problem                                     | Key Concept Shared                                     |
|---------------------------------------------|--------------------------------------------------------|
| Top K Frequent Elements (LC 347)            | Frequency map + min-heap or bucket sort                |
| Majority Element (LC 169)                   | Most frequent element; Boyer-Moore Vote for O(1) space |
| Majority Element II (LC 229)               | Elements appearing > n/3 times; generalised voting     |
| First Unique Character in a String (LC 387) | Frequency map; find element with count = 1             |
| Sort Characters By Frequency (LC 451)       | Frequency map + sort by value descending               |
| Find All Anagrams in a String (LC 438)      | Sliding window + frequency map comparison              |
| Frequency Count of Array Elements           | Direct prerequisite — builds the freq map              |
| Least Frequent Element                      | Same approach; use `min(freq, key=freq.get)`           |
| Word Frequency in a Paragraph               | Same pattern; tokenise string first                    |

---

*End of Study Notes — Highest Occurring Element in an Array*