# 🔄 Reverse an Array

---

## 1. Name of the Problem

**Reverse an Array**

> Also known as: *"Array Reversal"* or *"In-Place Array Reversal"* — a foundational
> problem in data structures that introduces the **two-pointer technique**, one of the
> most reusable patterns in all of algorithmic problem solving. It appears as a
> building block inside sorting algorithms, palindrome checks, string manipulation,
> and sliding window problems.

---

## 2. Problem Statement

### What the Code Solves

Given an array of `n` integers, **reverse the order of its elements** — the first
element becomes the last, the last becomes the first, and every element in between
swaps symmetrically toward the centre.

```
Original : [1, 2, 3, 4, 5]
Reversed : [5, 4, 3, 2, 1]
```

The given code achieves this **in-place** (no extra array created) using the
**two-pointer technique**: one pointer starts at the left end, one at the right end,
and they march toward each other, swapping elements at each step until they meet.

---

### Formal Definition

```
Input  : An integer n (size), followed by n integers forming array arr
Output : arr with all elements in reversed order
```

---

### Example 1

```
Input  : n = 5,  arr = [1, 2, 3, 4, 5]
Output : Reversed array: [5, 4, 3, 2, 1]
```

**Why?**
```
Swap index 0 and 4 → [5, 2, 3, 4, 1]
Swap index 1 and 3 → [5, 4, 3, 2, 1]
Index 2 is the centre → no swap needed, done.
```

---

### Example 2

```
Input  : n = 4,  arr = [10, 20, 30, 40]
Output : Reversed array: [40, 30, 20, 10]
```

**Why?**
```
Swap index 0 and 3 → [40, 20, 30, 10]
Swap index 1 and 2 → [40, 30, 20, 10]
Pointers meet → done.
```

---

### Example 3 — Even vs Odd Length

```
Odd  length: [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]   (middle element 3 never moves)
Even length: [1, 2, 3, 4]    → [4, 3, 2, 1]       (all elements swap)
```

---

### Example 4 — Edge Cases

```
Input  : n = 1,  arr = [42]
Output : Reversed array: [42]          (single element; nothing to swap)

Input  : n = 0,  arr = []
Output : Reversed array: []            (empty array; nothing to reverse)
```

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Extra-Array Way (Brute Force Thinking)

The simplest mental model: read the array from right to left and write into a new array.

```
Original : [1, 2, 3, 4, 5]
           ← ← ← ← ←         (read backwards)
New array: [5, 4, 3, 2, 1]
```

This is clear and easy to code but uses **O(n) extra space** for the new array.

---

#### The Two-Pointer Way (Optimised Thinking)

Instead of using a new array, swap elements **symmetrically from the outside in**:

```
[1, 2, 3, 4, 5]
 ↑           ↑
start        end     → swap → [5, 2, 3, 4, 1]

[5, 2, 3, 4, 1]
    ↑       ↑
  start    end       → swap → [5, 4, 3, 2, 1]

[5, 4, 3, 2, 1]
       ↑
   start=end         → start < end is FALSE → stop
```

Key observations:
- Two pointers always move **symmetrically** — start moves right (+1), end moves left (-1).
- They meet in the **middle** — for odd-length arrays at the exact centre element
  (which needs no swap), for even-length arrays when they cross each other.
- The condition `start < end` prevents swapping any element with itself or
  re-swapping already-processed pairs.
- **No extra space needed** — swaps happen inside the original array.

---

### Part B — Approaches

| Approach       | Strategy                                       | Time  | Space |
|----------------|------------------------------------------------|-------|-------|
| Brute Force    | Copy elements in reverse into a new array      | O(n)  | O(n)  |
| Two-Pointer    | Swap elements in-place using two indices       | O(n)  | O(1)  |

**Edge Cases to Handle**

| Input              | Expected Result    | Reason                                              |
|--------------------|--------------------|-----------------------------------------------------|
| `n = 0`, `arr = []`| `[]`               | Empty array; no swaps; return immediately           |
| `n = 1`            | Same single element| Only one element; `start == end`; condition false   |
| `n = 2`            | Elements swapped   | One swap only; pointers cross after first iteration |
| All same elements  | Same array         | Swaps happen but output looks identical             |
| Negative numbers   | Reversal works     | Sign of elements is irrelevant to reversal logic    |

---

## 4. Pseudocode

### Brute Force — O(n) Time, O(n) Space

```
FUNCTION reverse_brute_force(arr, n):
    IF n == 0:
        RETURN []

    reversed_arr = []                           # allocate new array

    FOR i FROM n-1 DOWN TO 0 (inclusive):
        APPEND arr[i] TO reversed_arr           # read original from right to left

    RETURN reversed_arr
```

---

### Two-Pointer In-Place — O(n) Time, O(1) Space

```
FUNCTION reverse_two_pointer(arr, n):
    IF n == 0:
        RETURN arr                              # nothing to reverse

    start = 0                                   # left pointer begins at first index
    end   = n - 1                              # right pointer begins at last index

    WHILE start < end:                          # continue while pointers haven't crossed
        SWAP arr[start] AND arr[end]            # exchange the two outer elements
        start = start + 1                       # move left pointer inward (rightward)
        end   = end   - 1                      # move right pointer inward (leftward)

    RETURN arr                                  # array is now reversed in-place
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Reverse an Array
  Approach : Brute Force    → O(n) time, O(n) space
             Two-Pointer    → O(n) time, O(1) space (in-place)
  Author   : Study Notes
=============================================================
"""


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
# APPROACH 1 — Brute Force  O(n) time, O(n) space
# ─────────────────────────────────────────────────────────────

def reverse_brute_force(arr: list[int]) -> list[int]:
    """
    Reverse an array by reading it backwards into a brand-new list.

    Strategy:
        Iterate from the last index down to 0, appending each element
        into a fresh list. The original array is left untouched.

    Args:
        arr (list[int]): The input array (not modified).

    Returns:
        list[int]: A new list containing arr's elements in reverse order.

    Time  Complexity: O(n) — one pass from index n-1 to 0.
    Space Complexity: O(n) — a second array of size n is allocated.
    """
    # Edge case: empty array reverses to itself
    if not arr:
        return []

    reversed_arr = []                               # allocate a new list

    for i in range(len(arr) - 1, -1, -1):          # iterate from last index to 0
        reversed_arr.append(arr[i])                 # append element in reverse order

    return reversed_arr


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Two-Pointer In-Place  O(n) time, O(1) space
# ─────────────────────────────────────────────────────────────

def reverse_two_pointer(arr: list[int]) -> list[int]:
    """
    Reverse an array in-place using the two-pointer technique.

    Strategy:
        Place one pointer at each end of the array.
        Swap the elements they point to, then move both pointers one
        step toward the centre. Stop when they meet or cross.

    Why this works:
        Each swap correctly positions two elements (one near the start,
        one near the end). After n//2 swaps, all elements are in their
        final reversed positions. The middle element of an odd-length
        array is never touched — it's already in the right place.

    Args:
        arr (list[int]): The input array (modified in-place).

    Returns:
        list[int]: The same list, now reversed in-place.

    Time  Complexity: O(n) — exactly n//2 swaps; proportional to n.
    Space Complexity: O(1) — only two index variables; no extra array.
    """
    # Edge cases: empty or single-element arrays need no work
    if len(arr) <= 1:
        return arr

    start = 0               # left pointer starts at the first element
    end   = len(arr) - 1   # right pointer starts at the last element

    while start < end:
        # Swap the elements at the two pointers using Python's tuple swap
        # (no temporary variable needed — Python evaluates the right side fully first)
        arr[start], arr[end] = arr[end], arr[start]

        start += 1          # left pointer moves one step right (inward)
        end   -= 1          # right pointer moves one step left (inward)

    return arr              # the same list object, now reversed


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(
    original : list[int],
    result   : list[int],
    label    : str
) -> None:
    """
    Pretty-print the reversal result with before/after context.

    Args:
        original (list[int]): The array before reversal.
        result   (list[int]): The array after reversal.
        label    (str)       : Approach label for display.
    """
    print(f"\n  [{label}]")
    print(f"  Original : {original}")
    print(f"  Reversed : {result}")

    # Extra contextual notes
    if len(result) == 0:
        print("  Note: Empty array — nothing to reverse.")
    elif len(result) == 1:
        print("  Note: Single element — trivially its own reverse.")
    elif result == original:
        print("  Note: Array is a palindrome — identical before and after reversal.")


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to reverse an array.

    Options:
        1 → Brute Force   (O(n) time, O(n) space — new array)
        2 → Two-Pointer   (O(n) time, O(1) space — in-place)
        3 → Both          — compare side by side
        4 → Exit
    """
    print("=" * 56)
    print("   REVERSE AN ARRAY — Study Program")
    print("=" * 56)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force  — O(n) time, O(n) space (new array)")
        print("  [2] Two-Pointer  — O(n) time, O(1) space (in-place)")
        print("  [3] Both         — Compare side by side")
        print("  [4] Exit")
        print("-" * 56)

        choice = input("  Enter choice (1/2/3/4): ").strip()

        if choice == "4":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, or 4.\n")
            continue

        # ── Get array input ───────────────────────────────
        n = get_non_negative_integer("\n  Enter the number of elements (n): ")

        if n == 0:
            print("\n  [Result] Empty array → []")
            print()
            continue

        original = read_array(n)

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = reverse_brute_force(original)
            display_result(original, result, "Brute Force — O(n) space")

        elif choice == "2":
            # Work on a copy so the display can show the original
            arr_copy = original.copy()
            result   = reverse_two_pointer(arr_copy)
            display_result(original, result, "Two-Pointer — O(1) space (in-place)")

        elif choice == "3":
            bf_result = reverse_brute_force(original)

            arr_copy  = original.copy()
            tp_result = reverse_two_pointer(arr_copy)

            display_result(original, bf_result,
                           "Brute Force  — O(n) space")
            display_result(original, tp_result,
                           "Two-Pointer  — O(1) space (in-place)")

            match = "✅ Match" if bf_result == tp_result else "❌ Mismatch!"
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

We use **arr = [1, 2, 3, 4, 5]** (odd length, n = 5) for the two-pointer approach and
**arr = [10, 20, 30, 40]** (even length, n = 4) for the brute force, showing every step.

---

### Brute Force Dry Run — arr = [10, 20, 30, 40], n = 4

#### Reading Backwards Pass

| Step | i (index) | arr[i] Read | reversed_arr After Append | Explanation                     |
|------|-----------|-------------|----------------------------|---------------------------------|
| Init | —         | —           | []                         | New empty list created          |
| 1    | 3         | 40          | [40]                       | Last element appended first     |
| 2    | 2         | 30          | [40, 30]                   | Second-to-last appended         |
| 3    | 1         | 20          | [40, 30, 20]               | Third-to-last appended          |
| 4    | 0         | 10          | [40, 30, 20, 10]           | First element appended last     |
| End  | —         | —           | **[40, 30, 20, 10]**       | **Final Answer ✅**             |

> Loop ran **4 iterations** (n iterations). Original array unchanged.
> A second array of size 4 lives in memory simultaneously.

---

### Two-Pointer Dry Run — arr = [1, 2, 3, 4, 5], n = 5

#### Pointer Positions and Swaps

| Step | start | end | arr Before Swap      | Operation              | arr After Swap       | start < end? | Explanation                        |
|------|-------|-----|----------------------|------------------------|----------------------|--------------|------------------------------------|
| Init | 0     | 4   | [1, 2, 3, 4, 5]     | —                      | [1, 2, 3, 4, 5]     | ✅ (0 < 4)   | Pointers placed at both ends       |
| 1    | 0     | 4   | [1, 2, 3, 4, 5]     | Swap idx 0 ↔ idx 4     | [5, 2, 3, 4, 1]     | ✅ (1 < 3)   | Outer pair swapped; pointers move  |
| 2    | 1     | 3   | [5, 2, 3, 4, 1]     | Swap idx 1 ↔ idx 3     | [5, 4, 3, 2, 1]     | ✅ (2 < 2)?  | Second pair swapped; pointers move |
| 3    | 2     | 2   | [5, 4, 3, 2, 1]     | Check: 2 < 2 → FALSE   | No swap              | ❌ (2 < 2)   | Pointers met at centre; loop exits |
| End  | —     | —   | —                    | return arr             | **[5, 4, 3, 2, 1]** | —            | **Final Answer ✅**                |

> Only **2 swaps** for n = 5 — exactly `n // 2` swaps always.
> Centre element (index 2, value 3) was never touched — already in its correct position.

---

### Two-Pointer Dry Run — arr = [10, 20, 30, 40], n = 4 (Even Length)

| Step | start | end | arr Before Swap         | Operation          | arr After Swap          | start < end? | Explanation                     |
|------|-------|-----|-------------------------|--------------------|-------------------------|--------------|---------------------------------|
| Init | 0     | 3   | [10, 20, 30, 40]       | —                  | [10, 20, 30, 40]       | ✅ (0 < 3)   | Pointers at both ends           |
| 1    | 0     | 3   | [10, 20, 30, 40]       | Swap idx 0 ↔ idx 3 | [40, 20, 30, 10]       | ✅ (1 < 2)   | Outer pair swapped              |
| 2    | 1     | 2   | [40, 20, 30, 10]       | Swap idx 1 ↔ idx 2 | [40, 30, 20, 10]       | ❌ (2 < 1)   | Inner pair swapped; pointers cross |
| End  | —     | —   | —                       | return arr         | **[40, 30, 20, 10]**   | —            | **Final Answer ✅**             |

> Exactly **2 swaps** for n = 4 — `n // 2 = 2` always.
> For even-length arrays, pointers cross each other (start > end) rather than meeting.

---

### Pointer Movement Visualised — n = 5

```
Initial:
  Index:  0    1    2    3    4
  Array: [1,   2,   3,   4,   5]
          ↑                   ↑
        start                end

After swap 1:
  Array: [5,   2,   3,   4,   1]
               ↑         ↑
             start       end

After swap 2:
  Array: [5,   4,   3,   2,   1]
                    ↑
              start = end = 2   ← loop exits (not start < end)

Final: [5, 4, 3, 2, 1]  ✅
```

---

### Swap Count Formula

| n (array size) | Swaps performed (n // 2) | Reason                                     |
|----------------|--------------------------|--------------------------------------------|
| 1              | 0                        | Single element; condition false immediately|
| 2              | 1                        | One pair to swap                           |
| 3              | 1                        | One outer pair; middle untouched           |
| 4              | 2                        | Two pairs; pointers cross                  |
| 5              | 2                        | Two outer pairs; centre untouched          |
| 10             | 5                        | Five pairs                                 |
| n              | n // 2                   | Always exactly half, rounded down          |

---

## 7. Time & Space Complexity

### Brute Force — New Array

| Case         | Time Complexity | Explanation                                                               |
|--------------|-----------------|---------------------------------------------------------------------------|
| Best Case    | O(n)            | Must always read every element once to build the new array; no shortcut  |
| Worst Case   | O(n)            | Same single pass regardless of values or array content                    |
| Average Case | O(n)            | Exactly n append operations — completely deterministic                    |

| Space Complexity | O(n) | A second array of size n is allocated and populated. Both the original and reversed arrays exist in memory simultaneously. |
|---|---|---|

---

### Two-Pointer — In-Place

| Case         | Time Complexity | Explanation                                                                          |
|--------------|-----------------|--------------------------------------------------------------------------------------|
| Best Case    | O(1)            | n = 0 or n = 1 — condition `start < end` is false immediately; zero iterations      |
| Worst Case   | O(n)            | General case: exactly n // 2 swap iterations, each O(1) → total O(n)                |
| Average Case | O(n)            | Always n // 2 swaps for any array of size n — no variability based on content       |

| Space Complexity | O(1) | Only two integer variables (`start` and `end`) regardless of n. Python's tuple swap `a, b = b, a` uses a temporary under the hood but it is O(1) — a single fixed-size register, not a growing structure. |
|---|---|---|

---

### Why Exactly n // 2 Swaps?

```
Each swap simultaneously fixes TWO elements:
  - arr[start] moves to its final position
  - arr[end]   moves to its final position

So n elements need only n/2 operations.
Integer division: n // 2 (the middle element of odd arrays needs no swap).

n = 6 → 3 swaps  (pairs: (0,5), (1,4), (2,3))
n = 7 → 3 swaps  (pairs: (0,6), (1,5), (2,4) — index 3 stays)
```

---

### Head-to-Head Summary

| Property              | Brute Force           | Two-Pointer (In-Place)     |
|-----------------------|-----------------------|----------------------------|
| Time Complexity       | O(n)                  | O(n)                       |
| Space Complexity      | **O(n)**              | **O(1)** ← winner          |
| Modifies original?    | No (safe copy)        | Yes (mutates input)        |
| Extra array needed?   | Yes                   | No                         |
| Swap operations       | 0 (copies instead)    | n // 2                     |
| Best used when        | Original must be kept | Memory efficiency matters  |

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Two-pointer = mirror symmetry**: Think of the array as a palindrome to check —
   position 0 mirrors position n-1, position 1 mirrors position n-2, and so on.
   Reversal just forces that symmetry to be true by swapping.

2. **The middle element is free**: For odd-length arrays, the exact centre element is
   always already in its correct reversed position. The loop condition `start < end`
   naturally handles this — when they meet at centre, no swap occurs.

3. **n // 2 is the magic number**: No matter what, you always do exactly `n // 2`
   swaps. If n = 1000, only 500 swaps happen. Each swap does the work of two.

4. **Python's tuple swap is atomic**: `a, b = b, a` — Python evaluates the right-hand
   side **entirely** before assigning. There is no moment where both variables hold the
   same value. No temporary variable is needed.

5. **In-place = mutates the original**: If you need to keep the original array for
   later use, work on a **copy** (`arr.copy()`) before passing it to the in-place
   function — or use the brute-force approach which creates a new array.

---

### ⚠️ Edge Case Reminders

| Input                   | Expected Result     | Common Mistake                                      |
|-------------------------|---------------------|-----------------------------------------------------|
| `n = 0`, `arr = []`     | `[]`                | Crashing on `arr[0]` when array is empty            |
| `n = 1`                 | Same element        | Swapping index 0 with itself — harmless but wasteful; condition blocks it |
| `n = 2`                 | Two elements swapped| One swap only; after that `start (1) < end (0)` is false |
| All identical elements  | Same array          | Reversal is "correct" — visually looks unchanged    |
| `[1, 2, 1]` (palindrome)| `[1, 2, 1]`        | Reverse of a palindrome equals itself               |
| Mixed negatives         | Reversed normally   | Sign of elements has no effect on the swap logic    |

---

### 🔬 The Swap Without a Temp Variable

```python
# ❌ Old-school (requires a temporary variable)
temp         = arr[start]
arr[start]   = arr[end]
arr[end]     = temp

# ✅ Pythonic (tuple unpacking — no temp variable)
arr[start], arr[end] = arr[end], arr[start]

# Both produce identical results; the Pythonic version is preferred.
```

> **Why does the Pythonic version work?**
> Python evaluates the entire right-hand side `(arr[end], arr[start])` as a tuple
> first, then unpacks and assigns. The two values are captured simultaneously
> before any assignment overwrites either.

---

### 🔬 Python's Built-in Options

```python
arr = [1, 2, 3, 4, 5]

# Option 1: list.reverse() — in-place, O(1) space, returns None
arr.reverse()
print(arr)          # [5, 4, 3, 2, 1]

# Option 2: reversed() — returns an iterator, original untouched
print(list(reversed(arr)))    # [5, 4, 3, 2, 1]

# Option 3: slicing — creates a new reversed list
print(arr[::-1])    # [5, 4, 3, 2, 1]
```

> Know these exist — but always understand the manual implementation first.
> Interviewers will ask you to implement reversal, not call a library function.

---

### ⚖️ When To Use Which Approach

| Situation                                        | Recommended Approach                        |
|--------------------------------------------------|---------------------------------------------|
| Learning / first exposure to two-pointer         | Two-pointer (canonical introduction)        |
| Must preserve the original array                 | Brute force (creates a new array)           |
| Memory is constrained                            | Two-pointer (O(1) space)                   |
| Production Python code                           | `arr.reverse()` or `arr[::-1]`             |
| Interview / competitive programming              | Two-pointer (shows algorithmic awareness)   |
| Reversing only a sub-array [i..j]                | Two-pointer on the subrange `[i, j]`       |

---

### 📏 Rules of Thumb

- **Two-pointer pattern recognition**: Anytime a problem works symmetrically from both
  ends toward the middle — reversal, palindrome check, container with most water,
  trapping rainwater — reach for two pointers.

- **In-place vs out-of-place**: In-place (O(1) space) is generally preferred in
  interviews unless the problem explicitly requires the original to be preserved.

- **`start < end` not `start <= end`**: Using `<=` would cause the middle element
  of an odd-length array to be swapped with itself — harmless but unnecessary.
  `<` is the correct termination condition.

- **Slice reversal `arr[::-1]`**: Python's slice notation with step `-1` creates a
  reversed copy in O(n) time and O(n) space — equivalent to brute force internally.

- **Index arithmetic**: `end = n - 1`, not `end = n` — arrays are 0-indexed.
  This is the most common off-by-one error in reversal problems.

---

### 🔗 Related Problems to Practice Next

| Problem                                   | Key Concept Shared                               |
|-------------------------------------------|--------------------------------------------------|
| Check if a string/array is a palindrome   | Same two-pointer from both ends toward centre    |
| Rotate an array by k positions            | Reversal algorithm (reverse sub-arrays)          |
| Move all zeroes to end                    | Two-pointer variant (slow and fast pointer)      |
| Container with most water                 | Two-pointer shrinking from both ends             |
| Reverse words in a sentence               | Reverse full string, then reverse each word      |
| Reverse a linked list                     | Same idea; prev/current/next pointers            |
| Sort colours (Dutch National Flag)        | Three-pointer generalisation of two-pointer      |

---

*End of Study Notes — Reverse an Array*