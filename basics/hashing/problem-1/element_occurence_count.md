# 📊 Frequency Count of Array Elements

---

## 1. Name of the Problem

**Frequency Count of Array Elements**

> Also known as: *"Element Frequency Counter"*, *"Character/Element Occurrence Count"*,
> or *"Counting with a Hash Map"* — a foundational problem in data structures that
> introduces the **hash map / dictionary pattern**: one of the single most reusable
> techniques in all of programming. It is the direct building block for solving
> anagram detection, majority element, top-K frequent elements, group anagrams,
> two-sum, and hundreds of other problems.

---

## 2. Problem Statement

### What the Code Solves

Given an array of `n` integers, find how many times **each unique element appears**
in the array and report the count for every element.

```
Input  : An array arr of n integers (may contain duplicates)
Output : For each unique element, print the element and how many times it appears
```

The code uses a **dictionary (hash map)** where:
- Each **key** is a unique element from the array
- Each **value** is the number of times that element appears

---

### Formal Definition

```
Input  : n integers forming array arr
Output : For every unique value v in arr,
         the count c such that arr[i] == v for exactly c indices i
```

---

### Example 1

```
Input  : n = 7,  arr = [1, 2, 2, 3, 3, 3, 4]
Output :
  Element 1 occurs 1 times.
  Element 2 occurs 2 times.
  Element 3 occurs 3 times.
  Element 4 occurs 1 times.
```

**Why?**
```
1 → appears at index 0              → count: 1
2 → appears at indices 1, 2         → count: 2
3 → appears at indices 3, 4, 5      → count: 3
4 → appears at index 6              → count: 1
```

---

### Example 2

```
Input  : n = 5,  arr = [4, 4, 4, 4, 4]
Output :
  Element 4 occurs 5 times.
```

> All elements are the same — only one unique key in the dictionary.

---

### Example 3

```
Input  : n = 6,  arr = [5, 3, 5, 8, 3, 5]
Output :
  Element 5 occurs 3 times.
  Element 3 occurs 2 times.
  Element 8 occurs 1 times.
```

> Output order follows **insertion order** (Python 3.7+ guarantees dict insertion order).
> 5 is first seen before 3, which is first seen before 8.

---

### Example 4 — Edge Cases

```
Input  : n = 1,  arr = [42]
Output : Element 42 occurs 1 times.

Input  : n = 0,  arr = []
Output : (no output — empty array, empty frequency map)
```

---

### What the Frequency Map Looks Like Internally

For `arr = [1, 2, 2, 3, 3, 3, 4]`:

```
After processing each element:

Process 1 → freq = {1: 1}
Process 2 → freq = {1: 1, 2: 1}
Process 2 → freq = {1: 1, 2: 2}
Process 3 → freq = {1: 1, 2: 2, 3: 1}
Process 3 → freq = {1: 1, 2: 2, 3: 2}
Process 3 → freq = {1: 1, 2: 2, 3: 3}
Process 4 → freq = {1: 1, 2: 2, 3: 3, 4: 1}
```

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Brute Force Way (Nested Loop Thinking)

The most literal approach: for every unique element, scan the entire array and count
how many times it appears.

```
arr = [1, 2, 2, 3, 3, 3, 4]

Count 1: scan full array → found at index 0          → 1 time
Count 2: scan full array → found at indices 1, 2     → 2 times
Count 3: scan full array → found at indices 3, 4, 5  → 3 times
Count 4: scan full array → found at index 6          → 1 time
```

This works but requires scanning the array **once per unique element** — leading to
O(n²) time in the worst case (all elements distinct).

---

#### The Hash Map Way (Optimised Thinking)

Instead of rescanning for each element, make a **single pass** through the array.
As you visit each element, immediately record it in a dictionary:

```
"Have I seen this element before?"
    YES → increment its count by 1
    NO  → create a new entry with count 1
```

A dictionary lookup and update are both **O(1) average time** — so one pass through
n elements gives O(n) total time.

Think of the dictionary as a **tally sheet**: every time you encounter a number,
you add one mark to its row. At the end, every row's marks tell you the frequency.

```
arr = [3, 1, 3, 2, 1, 3]

Tally as you go:
  see 3 → sheet: {3: |||  }
  see 1 → sheet: {3: |||  , 1: |    }
  see 3 → sheet: {3: ||||  , 1: |    }
  see 2 → sheet: {3: ||||  , 1: |    , 2: |    }
  see 1 → sheet: {3: ||||  , 1: ||   , 2: |    }
  see 3 → sheet: {3: |||||, 1: ||   , 2: |    }

Read off: 3→3, 1→2, 2→1
```

---

### Part B — Approaches

| Approach           | Strategy                                        | Time   | Space  |
|--------------------|-------------------------------------------------|--------|--------|
| Brute Force        | For each unique element, scan full array        | O(n²)  | O(u)   |
| Hash Map (given)   | Single pass; update dictionary on each visit    | O(n)   | O(u)   |
| Sorting-Based      | Sort array; count consecutive equal elements    | O(n log n) | O(1) or O(n) |

> `u` = number of unique elements in arr (1 ≤ u ≤ n).

**Edge Cases to Handle**

| Input                  | Expected Behaviour                                         |
|------------------------|------------------------------------------------------------|
| `n = 0`, `arr = []`    | Empty dict; no output — graceful handling required         |
| `n = 1`                | Single element; count = 1                                  |
| All elements same      | One key in dict with count = n                             |
| All elements distinct  | n keys in dict, each with count = 1                        |
| Negative integers      | Dictionary handles negatives as keys perfectly             |
| Very large numbers     | Python integers are arbitrary-precision; no overflow risk  |

---

## 4. Pseudocode

### Brute Force — O(n²) Time, O(u) Space

```
FUNCTION frequency_brute(arr):
    IF arr is empty:
        RETURN {}

    freq    = {}                            # result dictionary
    visited = SET()                         # track elements already counted

    FOR each element IN arr:
        IF element NOT IN visited:
            visited.ADD(element)            # mark as seen
            count = 0
            FOR each item IN arr:           # rescan entire array
                IF item == element:
                    count = count + 1
            freq[element] = count           # store final count

    RETURN freq
```

---

### Hash Map (Optimised) — O(n) Time, O(u) Space

```
FUNCTION frequency_hashmap(arr):
    IF arr is empty:
        RETURN {}

    freq = {}                               # empty dictionary

    FOR each element IN arr:               # single pass — visit each element once
        IF element IS IN freq:
            freq[element] = freq[element] + 1   # seen before → increment count
        ELSE:
            freq[element] = 1              # first time seen → initialise to 1

    RETURN freq
```

---

### Sorting-Based — O(n log n) Time, O(1) Extra Space

```
FUNCTION frequency_sorting(arr):
    IF arr is empty:
        RETURN {}

    sorted_arr = SORT(arr)                 # sort brings duplicates together
    freq       = {}

    current = sorted_arr[0]                # first element
    count   = 1

    FOR i FROM 1 TO len(sorted_arr) - 1:
        IF sorted_arr[i] == current:
            count = count + 1             # same element continues
        ELSE:
            freq[current] = count         # element block ended — store count
            current = sorted_arr[i]       # move to new element
            count   = 1                   # reset counter

    freq[current] = count                 # store the final element's count

    RETURN freq
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Frequency Count of Array Elements
  Approach : Brute Force     → O(n²)      time, O(u) space
             Hash Map        → O(n)       time, O(u) space
             Sorting-Based   → O(n log n) time, O(1) extra space
  Author   : Study Notes
=============================================================
"""

import collections


# ─────────────────────────────────────────────────────────────
# HELPER — Validated integer input
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

def frequency_brute(arr: list[int]) -> dict[int, int]:
    """
    Count the frequency of each element using a nested loop.

    Strategy:
        For every unique element encountered, perform a complete scan of
        the array to count how many times it appears. Use a 'visited' set
        to skip elements that have already been counted.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        dict[int, int]: Maps each unique element to its frequency count.

    Time  Complexity: O(n²) — for each of up to n unique elements, the inner
                              loop rescans all n elements: n × n = n² steps.
    Space Complexity: O(u)  — freq dict and visited set each hold u entries
                              where u = number of unique elements (u ≤ n).
    """
    if not arr:
        return {}                                # empty input → empty result

    freq    : dict[int, int] = {}               # result: element → count
    visited : set[int]       = set()            # track already-processed elements

    for element in arr:
        if element in visited:
            continue                            # already counted this element; skip

        visited.add(element)                    # mark as now being counted

        count = 0
        for item in arr:                        # inner loop: rescan entire array
            if item == element:
                count += 1                      # found a match → increment

        freq[element] = count                   # store the final count

    return freq


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Hash Map (Single Pass)  O(n) time, O(u) space
# ─────────────────────────────────────────────────────────────

def frequency_hashmap(arr: list[int]) -> dict[int, int]:
    """
    Count the frequency of each element in a single pass using a dictionary.

    Strategy:
        Traverse the array once. For each element:
          - If it already exists as a key in freq, increment its value by 1.
          - If it does not exist, create a new key initialised to 1.
        Dictionary lookup and assignment are both O(1) average time.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        dict[int, int]: Maps each unique element to its frequency count.

    Time  Complexity: O(n)  — one pass; each dict operation is O(1) average.
    Space Complexity: O(u)  — dictionary holds one entry per unique element.
    """
    if not arr:
        return {}

    freq: dict[int, int] = {}

    for element in arr:                         # single pass through the array
        if element in freq:
            freq[element] += 1                  # seen before → increment count
        else:
            freq[element] = 1                   # first time seen → initialise to 1

    return freq


# ─────────────────────────────────────────────────────────────
# APPROACH 2b — Hash Map using collections.Counter (Pythonic)
# ─────────────────────────────────────────────────────────────

def frequency_counter(arr: list[int]) -> dict[int, int]:
    """
    Count frequencies using Python's built-in collections.Counter.

    Counter is a specialised dictionary subclass that counts hashable objects.
    It is implemented in optimised C and is the fastest option in Python.
    The result behaves exactly like a regular dict.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        dict[int, int]: Maps each unique element to its frequency count.

    Time  Complexity: O(n)  — Counter iterates the list once internally.
    Space Complexity: O(u)  — one entry per unique element.
    """
    return dict(collections.Counter(arr))


# ─────────────────────────────────────────────────────────────
# APPROACH 3 — Sorting-Based  O(n log n) time, O(1) extra space
# ─────────────────────────────────────────────────────────────

def frequency_sorting(arr: list[int]) -> dict[int, int]:
    """
    Count frequencies by sorting the array first, then counting runs.

    Strategy:
        Sorting brings all duplicate elements together into contiguous runs.
        A single scan of the sorted array then counts each run's length.
        This avoids a hash map entirely — useful when space is constrained.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        dict[int, int]: Maps each unique element to its frequency count.
                        Note: Output order is sorted ascending (not insertion order).

    Time  Complexity: O(n log n) — dominated by the sort step.
    Space Complexity: O(1) extra — sorted() creates a copy (O(n)) but no
                                   additional data structures are used;
                                   in-place sort with arr.sort() is O(1) extra.
    """
    if not arr:
        return {}

    sorted_arr = sorted(arr)                    # sort a copy; preserves original
    freq: dict[int, int] = {}

    current = sorted_arr[0]                     # track the element of the current run
    count   = 1                                 # count elements in the current run

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == current:
            count += 1                          # same element continues the run
        else:
            freq[current] = count              # run ended → store count
            current = sorted_arr[i]            # start a new run
            count   = 1                        # reset run counter

    freq[current] = count                       # store the final run (loop doesn't catch it)

    return freq


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(
    arr   : list[int],
    freq  : dict[int, int],
    label : str
) -> None:
    """
    Pretty-print the frequency count result with summary statistics.

    Args:
        arr   (list[int])    : The original input array.
        freq  (dict[int,int]): The computed frequency dictionary.
        label (str)          : Approach label for display.
    """
    print(f"\n  [{label}]")

    if not freq:
        print("  (No elements to display — empty array)")
        return

    print(f"  {'Element':>10}  {'Count':>8}  {'Bar Chart'}")
    print(f"  {'-'*10}  {'-'*8}  {'-'*20}")

    for element, count in freq.items():
        bar = "█" * count                       # visual bar proportional to count
        print(f"  {element:>10}  {count:>8}  {bar}")

    # Summary statistics
    total_elements  = len(arr)
    unique_elements = len(freq)
    most_common     = max(freq, key=freq.get)
    least_common    = min(freq, key=freq.get)

    print(f"\n  Total elements   : {total_elements}")
    print(f"  Unique elements  : {unique_elements}")
    print(f"  Most frequent    : {most_common}  (appears {freq[most_common]} times)")
    print(f"  Least frequent   : {least_common}  (appears {freq[least_common]} times)")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to count element frequencies in an array.

    Options:
        1 → Brute Force    (O(n²)      time — nested loops)
        2 → Hash Map       (O(n)       time — single pass dictionary)
        3 → Sorting-Based  (O(n log n) time — sort then count runs)
        4 → All Three      — compare all approaches side by side
        5 → Exit
    """
    print("=" * 60)
    print("   FREQUENCY COUNT OF ARRAY ELEMENTS — Study Program")
    print("=" * 60)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force   — O(n²)      nested loop scan")
        print("  [2] Hash Map      — O(n)       single pass ✅ recommended")
        print("  [3] Sorting-Based — O(n log n) sort then count runs")
        print("  [4] All Three     — Compare side by side")
        print("  [5] Exit")
        print("-" * 60)

        choice = input("  Enter choice (1/2/3/4/5): ").strip()

        if choice == "5":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, 4, or 5.\n")
            continue

        # ── Get array input ───────────────────────────────
        n = get_non_negative_integer("\n  Enter the number of elements (n): ")

        if n == 0:
            print("\n  [Result] Empty array → no frequency data.")
            print()
            continue

        arr = read_array(n)

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = frequency_brute(arr)
            display_result(arr, result,
                           "Brute Force — O(n²) time, O(u) space")

        elif choice == "2":
            result = frequency_hashmap(arr)
            display_result(arr, result,
                           "Hash Map — O(n) time, O(u) space")

        elif choice == "3":
            result = frequency_sorting(arr)
            display_result(arr, result,
                           "Sorting-Based — O(n log n) time, O(1) extra space")

        elif choice == "4":
            bf_result   = frequency_brute(arr)
            hm_result   = frequency_hashmap(arr)
            sort_result = frequency_sorting(arr)

            display_result(arr, bf_result,
                           "Brute Force   — O(n²)")
            display_result(arr, hm_result,
                           "Hash Map      — O(n)")
            display_result(arr, sort_result,
                           "Sorting-Based — O(n log n)")

            # Consistency check — all three must agree on every count
            all_match = (
                set(bf_result.items()) == set(hm_result.items()) ==
                set(sort_result.items())
            )
            verdict = "✅ All Match" if all_match else "❌ Mismatch!"
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

We use **arr = [3, 1, 3, 2, 1, 3]** (n = 6) across all three approaches.

---

### Brute Force Dry Run — arr = [3, 1, 3, 2, 1, 3]

#### Outer Loop Pass (element being counted) × Inner Loop Scan

**Pass 1 — Counting element `3`:**

| Inner i | arr[i] | arr[i] == 3? | count | visited         |
|---------|--------|--------------|-------|-----------------|
| 0       | 3      | ✅ Yes       | 1     | {3}             |
| 1       | 1      | ❌ No        | 1     | {3}             |
| 2       | 3      | ✅ Yes       | 2     | {3}             |
| 3       | 2      | ❌ No        | 2     | {3}             |
| 4       | 1      | ❌ No        | 2     | {3}             |
| 5       | 3      | ✅ Yes       | 3     | {3}             |
> **freq after pass 1: {3: 3}**

**Pass 2 — Element `1` encountered (not in visited):**

| Inner i | arr[i] | arr[i] == 1? | count | visited       |
|---------|--------|--------------|-------|---------------|
| 0       | 3      | ❌ No        | 0     | {3, 1}        |
| 1       | 1      | ✅ Yes       | 1     | {3, 1}        |
| 2       | 3      | ❌ No        | 1     | {3, 1}        |
| 3       | 2      | ❌ No        | 1     | {3, 1}        |
| 4       | 1      | ✅ Yes       | 2     | {3, 1}        |
| 5       | 3      | ❌ No        | 2     | {3, 1}        |
> **freq after pass 2: {3: 3, 1: 2}**

**Pass 3 — Element `3` at index 2 (already in visited → SKIP)**
**Pass 4 — Element `2` encountered (not in visited):**

| Inner i | arr[i] | arr[i] == 2? | count | visited       |
|---------|--------|--------------|-------|---------------|
| 0       | 3      | ❌ No        | 0     | {3, 1, 2}    |
| 1       | 1      | ❌ No        | 0     | {3, 1, 2}    |
| 2       | 3      | ❌ No        | 0     | {3, 1, 2}    |
| 3       | 2      | ✅ Yes       | 1     | {3, 1, 2}    |
| 4       | 1      | ❌ No        | 1     | {3, 1, 2}    |
| 5       | 3      | ❌ No        | 1     | {3, 1, 2}    |
> **freq after pass 4: {3: 3, 1: 2, 2: 1}**

**Passes 5 and 6 — Elements `1` and `3` (both in visited → SKIP)**

#### Brute Force Summary

| Outer Element | Action                     | Inner Scans | freq State            |
|---------------|----------------------------|-------------|------------------------|
| 3 (index 0)   | New → full scan            | 6           | {3: 3}                |
| 1 (index 1)   | New → full scan            | 6           | {3: 3, 1: 2}          |
| 3 (index 2)   | In visited → **SKIP**      | 0           | {3: 3, 1: 2}          |
| 2 (index 3)   | New → full scan            | 6           | {3: 3, 1: 2, 2: 1}   |
| 1 (index 4)   | In visited → **SKIP**      | 0           | {3: 3, 1: 2, 2: 1}   |
| 3 (index 5)   | In visited → **SKIP**      | 0           | {3: 3, 1: 2, 2: 1}   |
| **Total**     |                            | **18 ops**  | **Final ✅**           |

> 3 unique elements × 6 inner scans = **18 inner loop operations**.

---

### Hash Map Dry Run — arr = [3, 1, 3, 2, 1, 3]

| Step | i | element | element in freq? | Operation            | freq After                  | Explanation                        |
|------|---|---------|------------------|----------------------|-----------------------------|------------------------------------|
| Init | — | —       | —                | freq = {}            | {}                          | Empty dictionary created           |
| 1    | 0 | 3       | ❌ No            | freq[3] = 1          | {3: 1}                      | First time seeing 3 → set to 1     |
| 2    | 1 | 1       | ❌ No            | freq[1] = 1          | {3: 1, 1: 1}                | First time seeing 1 → set to 1     |
| 3    | 2 | 3       | ✅ Yes           | freq[3] += 1 → 2     | {3: 2, 1: 1}                | 3 seen again → increment           |
| 4    | 3 | 2       | ❌ No            | freq[2] = 1          | {3: 2, 1: 1, 2: 1}          | First time seeing 2 → set to 1     |
| 5    | 4 | 1       | ✅ Yes           | freq[1] += 1 → 2     | {3: 2, 1: 2, 2: 1}          | 1 seen again → increment           |
| 6    | 5 | 3       | ✅ Yes           | freq[3] += 1 → 3     | {3: 3, 1: 2, 2: 1}          | 3 seen a 3rd time → increment      |
| End  | — | —       | —                | return freq          | **{3: 3, 1: 2, 2: 1}** ✅  | Single pass complete               |

> Only **6 steps** (one per element) — no rescanning, no wasted work.

---

### Sorting-Based Dry Run — arr = [3, 1, 3, 2, 1, 3]

#### Step 1 — Sort the array

```
Original : [3, 1, 3, 2, 1, 3]
Sorted   : [1, 1, 2, 3, 3, 3]     ← duplicates now grouped together
```

#### Step 2 — Scan sorted array, count runs

| i | sorted_arr[i] | current | count Before | sorted[i] == current? | Action                      | count After | freq State        |
|---|---------------|---------|--------------|------------------------|-----------------------------|-------------|-------------------|
| Init | —          | 1       | 1            | —                      | First element initialised   | 1           | {}                |
| 1  | 1             | 1       | 1            | ✅ Yes                  | Extend current run          | 2           | {}                |
| 2  | 2             | 1       | 2            | ❌ No                   | Store {1:2}; new run starts | 1           | {1: 2}            |
| 3  | 3             | 2       | 1            | ❌ No                   | Store {2:1}; new run starts | 1           | {1: 2, 2: 1}      |
| 4  | 3             | 3       | 1            | ✅ Yes                  | Extend current run          | 2           | {1: 2, 2: 1}      |
| 5  | 3             | 3       | 2            | ✅ Yes                  | Extend current run          | 3           | {1: 2, 2: 1}      |
| End| —             | 3       | 3            | —                      | Store final run {3:3}       | —           | {1:2, 2:1, 3:3}✅ |

> Output order is **sorted ascending** (1, 2, 3) — unlike the hash map which preserves
> insertion order (3, 1, 2). The counts are identical.

---

### Side-by-Side Comparison — arr = [3, 1, 3, 2, 1, 3] (n = 6, u = 3)

| Property                  | Brute Force | Hash Map  | Sorting-Based   |
|---------------------------|-------------|-----------|-----------------|
| Steps / operations        | 18          | 6         | 6 + O(n log n) sort |
| Passes through array      | u + 1 = 4   | 1         | 1 sort + 1 scan |
| Extra data structures     | dict + set  | dict only | none (in-place) |
| Output order              | Insertion   | Insertion | Sorted ascending|
| Final freq for 3          | 3 ✅         | 3 ✅       | 3 ✅             |
| Final freq for 1          | 2 ✅         | 2 ✅       | 2 ✅             |
| Final freq for 2          | 1 ✅         | 1 ✅       | 1 ✅             |

---

## 7. Time & Space Complexity

### Brute Force — Nested Loop

| Case         | Time Complexity | Explanation                                                                     |
|--------------|-----------------|---------------------------------------------------------------------------------|
| Best Case    | O(n)            | All elements identical → only 1 unique element → inner loop runs once: 1 × n   |
| Worst Case   | O(n²)           | All elements distinct → u = n unique elements → inner loop runs n times: n × n |
| Average Case | O(n × u)        | u unique elements, each triggering a full n-length inner scan: u × n           |

| Space Complexity | O(u) | `freq` dictionary and `visited` set each hold at most u entries where u = number of unique elements (1 ≤ u ≤ n). |
|---|---|---|

---

### Hash Map — Single Pass

| Case         | Time Complexity | Explanation                                                                    |
|--------------|-----------------|--------------------------------------------------------------------------------|
| Best Case    | O(n)            | Every element processed once; all dict lookups and inserts are O(1) average    |
| Worst Case   | O(n)            | Same single pass regardless of array content — no variability                  |
| Average Case | O(n)            | Always exactly n dictionary operations; hash collisions are O(1) amortised     |

| Space Complexity | O(u) | Dictionary holds exactly u entries — one per unique element. In the worst case (all distinct), u = n, so space is O(n). In the best case (all same), u = 1, so O(1). |
|---|---|---|

---

### Sorting-Based — Sort Then Count Runs

| Case         | Time Complexity | Explanation                                                                      |
|--------------|-----------------|----------------------------------------------------------------------------------|
| Best Case    | O(n log n)      | Even if all elements are identical, the sort step always costs O(n log n)        |
| Worst Case   | O(n log n)      | Sort dominates; the subsequent linear scan adds only O(n) — absorbed             |
| Average Case | O(n log n)      | Completely determined by the sort; the counting scan is always O(n)              |

| Space Complexity | O(1) extra | In-place sort (arr.sort()) uses O(1) extra space. Using sorted() (as in the code) creates a copy: O(n). The freq dict adds O(u). If space is critical, sort in-place on a copy to keep it O(u). |
|---|---|---|

---

### Complete Complexity Table

| Approach       | Time           | Space (extra) | When to Use                                     |
|----------------|----------------|---------------|-------------------------------------------------|
| Brute Force    | O(n²)          | O(u)          | Never in production; only for teaching O(n²)   |
| Hash Map       | **O(n)**       | O(u)          | Default choice — best time, simple code         |
| Sorting-Based  | O(n log n)     | O(1) extra    | When extra memory is forbidden and O(n log n) is acceptable |

---

### Why Hash Map Lookup is O(1)

A Python dictionary uses a **hash table** internally:

```
Hash table mechanics:
  1. Compute hash(key)          → integer fingerprint of the key
  2. Map hash to a bucket index → hash(key) % table_size
  3. Store / retrieve at that bucket

For key = 3:
  hash(3) = 3  →  bucket_index = 3 % table_size
  arr[bucket_index] → direct memory access → O(1)
```

Collisions (two different keys mapping to the same bucket) are resolved via open
addressing or chaining — but with a good hash function, the average case remains
O(1). Python's dict is extremely well optimised for integer keys.

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Dictionary = tally sheet**: Think of the frequency map as a physical tally sheet
   where each row is a unique element and each mark is one occurrence. One pass through
   the data fills out the entire sheet — O(n), not O(n²).

2. **"If key in dict, else"** is the fundamental hash map pattern. Memorise it:
```python
   if element in freq:
       freq[element] += 1
   else:
       freq[element] = 1
```
   This appears in dozens of problems: anagram detection, two-sum, group anagrams,
   first non-repeating character, majority element, and more.

3. **`get()` as a one-liner shortcut**:
```python
   freq[element] = freq.get(element, 0) + 1
```
   `dict.get(key, default)` returns the value if key exists, or `default` if not.
   This collapses the if-else into one line — equally readable, commonly used
   in interviews.

4. **Frequencies always sum to n**: The sum of all values in the frequency dictionary
   must equal the total number of elements in the array:
```python
   assert sum(freq.values()) == len(arr)   # always true ✅
```
   Use this as a quick sanity check during debugging.

5. **Sorting destroys insertion order**: The sorting-based approach outputs frequencies
   in sorted key order (ascending). The hash map preserves the order in which elements
   were first encountered (insertion order, Python 3.7+). Choose based on what the
   problem requires.

---

### ⚠️ Edge Case Reminders

| Input                   | Expected Behaviour                                              |
|-------------------------|-----------------------------------------------------------------|
| `n = 0`, `arr = []`     | Empty dict `{}` — handle gracefully; no output lines            |
| `n = 1`                 | One key with value 1                                            |
| All elements same       | One key with value n; `{"x": n}`                               |
| All elements distinct   | n keys, each with value 1                                       |
| Negative numbers        | Dict keys can be negative — works perfectly                     |
| Very large numbers      | Python integers are arbitrary-precision — no overflow           |
| Repeated negative nums  | Same logic — `{-3: 2, -1: 1}` etc.                            |

---

### 🔬 Four Equivalent Ways to Build a Frequency Map

```python
arr = [3, 1, 3, 2, 1, 3]

# Method 1: Explicit if-else (as in the original code — most transparent)
freq = {}
for element in arr:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1

# Method 2: dict.get() — one-liner, no if-else needed
freq = {}
for element in arr:
    freq[element] = freq.get(element, 0) + 1

# Method 3: collections.defaultdict — auto-initialises missing keys to 0
from collections import defaultdict
freq = defaultdict(int)
for element in arr:
    freq[element] += 1          # no KeyError — missing key auto-set to 0

# Method 4: collections.Counter — one-liner, most Pythonic
from collections import Counter
freq = Counter(arr)             # {3: 3, 1: 2, 2: 1}

# All four produce equivalent results:
# {3: 3, 1: 2, 2: 1}
```

> In interviews: know all four. Use Method 1 or 2 to show you understand the
> logic. Use `Counter` in production for brevity and speed.

---

### 🔬 The `dict.get()` Default Trap

```python
# ❌ Wrong — KeyError if element not yet in dict
freq[element] += 1              # crashes on first occurrence of new element

# ✅ Correct — provide default 0 before incrementing
freq[element] = freq.get(element, 0) + 1

# ✅ Also correct — explicit guard with 'in'
if element in freq:
    freq[element] += 1
else:
    freq[element] = 1
```

> A KeyError is the single most common mistake when building frequency maps
> manually. Always initialise before incrementing.

---

### ⚖️ When To Use Which Approach

| Situation                                          | Recommended Approach                            |
|----------------------------------------------------|-------------------------------------------------|
| General purpose — default choice                   | Hash Map (`dict` or `Counter`)                  |
| Interview — show understanding of the technique    | Hash Map with explicit if-else                  |
| Need sorted output by key                          | Sorting-Based, or `sorted(freq.items())`        |
| Extra memory forbidden (embedded systems, etc.)    | Sorting-Based with in-place sort                |
| Quick prototype / competitive programming          | `collections.Counter(arr)`                      |
| Teaching nested loops and O(n²) cost              | Brute Force (demonstration only)                |
| Finding most/least frequent element                | Hash Map + `max(freq, key=freq.get)`            |

---

### 📏 Rules of Thumb

- **Hash map = O(n) frequency counting**: Anytime a problem asks you to count,
  group, or track occurrences of elements — reach for a dictionary first.
  This is the single most common pattern in medium-difficulty interview problems.

- **Sum of all frequencies = n** (always):
```python
  sum(freq.values()) == len(arr)     # invariant — use this to verify your logic
```

- **Counter's most_common(k)**: Returns the k most frequent elements in O(n) time:
```python
  from collections import Counter
  Counter(arr).most_common(3)        # top-3 most frequent elements
```

- **Insertion order (Python 3.7+)**: Regular `dict` preserves insertion order.
  `Counter` also preserves insertion order as of Python 3.7. If you need sorted
  order, use `sorted(freq.items())` explicitly.

- **u ≤ n always**: The number of unique elements u can never exceed the array size n.
  Space for the frequency map is O(u) ≤ O(n).

- **Generalise to strings**: The exact same pattern works for strings —
  just replace `arr` with the string and each character is an element:
```python
  freq = Counter("aabbccc")    # {'c': 3, 'a': 2, 'b': 2}
```

---

### 🔗 Related Problems to Practice Next

| Problem                                    | Key Concept Shared                                     |
|--------------------------------------------|--------------------------------------------------------|
| First Non-Repeating Character              | Frequency map; find first element with count == 1      |
| Anagram Detection                          | Frequency maps of two strings must be equal            |
| Group Anagrams (LC 49)                     | Sort each word as key; group by frequency signature    |
| Top K Frequent Elements (LC 347)           | Frequency map + heap or bucket sort                    |
| Majority Element (LC 169)                  | Frequency map; find element with count > n/2           |
| Two Sum (LC 1)                             | Hash map to check complement existence in O(n)         |
| Longest Substring Without Repeating Chars  | Sliding window + frequency map for char counts         |
| Valid Anagram (LC 242)                     | Counter equality check on two strings                  |
| Find All Duplicates in an Array (LC 442)   | Frequency map; elements with count == 2                |
| Subarray Sum Equals K (LC 560)             | Prefix sum + hash map for count of valid subarrays     |

---

*End of Study Notes — Frequency Count of Array Elements*