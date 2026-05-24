# 🪞 Palindrome Check — String

---

## 1. Name of the Problem

**Palindrome Check (String)**

> Also known as: *"String Palindrome Verification"* — a classic problem that teaches
> **recursion**, the **two-pointer technique**, and **string manipulation** all at once.
> It appears in coding interviews, compiler design (syntax trees), bioinformatics (DNA
> sequence matching), and as the foundation for harder problems like *Longest Palindromic
> Substring* and *Palindrome Partitioning*.

---

## 2. Problem Statement

### What the Code Solves

Given a string `s`, determine whether it reads the **same forwards and backwards**.

A string is a **palindrome** if every character at position `i` from the left matches
the character at position `i` from the right:

```
s[0] == s[n-1]
s[1] == s[n-2]
s[2] == s[n-3]
...and so on toward the centre.
```

The given code solves this **recursively**: it compares the outermost characters first,
then calls itself on the inner substring, shrinking inward until the pointers meet.

---

### Formal Definition

```
Input  : A string s
Output : "Palindrome"     if s reads the same forwards and backwards
         "Not Palindrome" otherwise
```

---

### Example 1

```
Input  : s = "racecar"
Output : The string is a palindrome.
```

**Why?**
```
r a c e c a r
↑           ↑   →  r == r ✅
  ↑       ↑     →  a == a ✅
    ↑   ↑       →  c == c ✅
      ↑         →  centre 'e' — no partner needed ✅
```

---

### Example 2

```
Input  : s = "hello"
Output : The string is not a palindrome.
```

**Why?**
```
h e l l o
↑       ↑   →  h != o ❌  →  stop immediately
```

---

### Example 3

```
Input  : s = "madam"
Output : The string is a palindrome.
```

```
m a d a m
↑       ↑   →  m == m ✅
  ↑   ↑     →  a == a ✅
    ↑       →  centre 'd' ✅
```

---

### Example 4 — Edge Cases

```
Input  : s = ""          →  Palindrome   (empty string — vacuously true)
Input  : s = "a"         →  Palindrome   (single character — trivially true)
Input  : s = "ab"        →  Not Palindrome
Input  : s = "aa"        →  Palindrome
Input  : s = "abcba"     →  Palindrome
Input  : s = "abcde"     →  Not Palindrome
```

---

### Quick Reference Table

| String      | Palindrome? | First Mismatch (if any) |
|-------------|-------------|--------------------------|
| `"racecar"` | ✅ Yes      | —                        |
| `"madam"`   | ✅ Yes      | —                        |
| `"level"`   | ✅ Yes      | —                        |
| `"noon"`    | ✅ Yes      | —                        |
| `"hello"`   | ❌ No       | h ≠ o (index 0 vs 4)    |
| `"world"`   | ❌ No       | w ≠ d (index 0 vs 4)    |
| `"abcba"`   | ✅ Yes      | —                        |
| `"abcde"`   | ❌ No       | a ≠ e (index 0 vs 4)    |
| `""`        | ✅ Yes      | empty — trivially true   |
| `"z"`       | ✅ Yes      | single char              |

---

## 3. Logic Behind the Solution

### Part A — Intuition

#### The Reversal Way (Brute Force Thinking)

The simplest mental model: **reverse the string and check if it equals the original**.

```
s         = "racecar"
reversed  = "racecar"    ← same → Palindrome ✅

s         = "hello"
reversed  = "olleh"      ← different → Not a Palindrome ❌
```

This is clean and readable but creates a new string in memory — O(n) extra space.

---

#### The Two-Pointer Way (Iterative Optimised Thinking)

Instead of reversing, use two indices — one starting at the left end, one at the right —
and march them inward, comparing one pair of characters at a time:

```
s = "r a c e c a r"
     0 1 2 3 4 5 6

Step 1: left=0, right=6  →  s[0]='r' == s[6]='r' ✅  →  move inward
Step 2: left=1, right=5  →  s[1]='a' == s[5]='a' ✅  →  move inward
Step 3: left=2, right=4  →  s[2]='c' == s[4]='c' ✅  →  move inward
Step 4: left=3, right=3  →  left >= right → PALINDROME ✅
```

The moment any pair mismatches, you stop immediately — **early exit** saves time for
non-palindromes.

---

#### The Recursive Way (as given in the code)

The recursive approach mirrors the two-pointer logic exactly, but expresses it through
the **call stack** instead of a loop:

```
is_palindrome("racecar", 0, 6)
    ↳ 'r' == 'r' ✅  →  is_palindrome("racecar", 1, 5)
            ↳ 'a' == 'a' ✅  →  is_palindrome("racecar", 2, 4)
                    ↳ 'c' == 'c' ✅  →  is_palindrome("racecar", 3, 3)
                                ↳ left(3) >= right(3)  →  return True ← base case

Unwinding:
                    return True
            return True
    return True
return True  →  "racecar" is a palindrome ✅
```

Each call reduces the problem to a **strictly smaller subproblem** (the inner substring),
until the base case is reached. This is the textbook definition of structural recursion.

---

### Part B — Approaches

| Approach        | Strategy                                           | Time  | Space              |
|-----------------|----------------------------------------------------|-------|--------------------|
| Brute Force     | Reverse string; compare with original              | O(n)  | O(n) — new string  |
| Iterative       | Two-pointer loop; compare pairs inward             | O(n)  | O(1)               |
| Recursive       | Recursive two-pointer; shrink substring each call  | O(n)  | O(n) — call stack  |

**Edge Cases to Handle**

| Input            | Expected | Reason                                                     |
|------------------|----------|------------------------------------------------------------|
| `""` (empty)     | True     | Empty string is vacuously a palindrome                     |
| `"a"` (1 char)   | True     | Single character always equals itself                      |
| `"aa"` (2 chars) | True     | Both characters match; left=0, right=1 → swap once         |
| `"ab"` (2 chars) | False    | First (and only) pair mismatches immediately               |
| All same chars   | True     | Every pair matches (`"aaaa"`, `"zzzz"`)                    |
| Case sensitivity | Varies   | `"Racecar"` is NOT a palindrome unless lowercased first    |
| Spaces/punctuation | Varies | `"race car"` fails unless whitespace is stripped first     |

---

## 4. Pseudocode

### Brute Force — Reverse and Compare, O(n) Time, O(n) Space

```
FUNCTION is_palindrome_brute(s):
    IF s is empty:
        RETURN True                         # empty string is trivially a palindrome

    reversed_s = REVERSE of s              # create new reversed string

    IF s == reversed_s:
        RETURN True
    ELSE:
        RETURN False
```

---

### Iterative Two-Pointer — O(n) Time, O(1) Space

```
FUNCTION is_palindrome_iterative(s):
    IF s is empty:
        RETURN True

    left  = 0                              # pointer starting at leftmost character
    right = LENGTH(s) - 1                 # pointer starting at rightmost character

    WHILE left < right:
        IF s[left] != s[right]:
            RETURN False                   # mismatch found → not a palindrome; early exit
        left  = left  + 1                 # move left pointer inward (rightward)
        right = right - 1                 # move right pointer inward (leftward)

    RETURN True                            # all pairs matched → palindrome
```

---

### Recursive — O(n) Time, O(n) Space (Call Stack)

```
FUNCTION is_palindrome_recursive(s, left, right):

    # Base case 1: pointers have met or crossed — all pairs matched
    IF left >= right:
        RETURN True

    # Base case 2: current outer characters don't match — not a palindrome
    IF s[left] != s[right]:
        RETURN False

    # Recursive case: outer pair matched; check the inner substring
    RETURN is_palindrome_recursive(s, left + 1, right - 1)
```

---

## 5. Refined Clean Structured Code

```python
"""
=============================================================
  Problem  : Palindrome Check — String
  Approach : Brute Force  → O(n) time, O(n) space
             Iterative    → O(n) time, O(1) space
             Recursive    → O(n) time, O(n) space (call stack)
  Author   : Study Notes
=============================================================
"""

import sys


# ─────────────────────────────────────────────────────────────
# HELPER — String normalisation (optional: case-insensitive mode)
# ─────────────────────────────────────────────────────────────

def normalise(s: str, ignore_case: bool, ignore_spaces: bool) -> str:
    """
    Optionally normalise a string before the palindrome check.

    Args:
        s             (str)  : The original input string.
        ignore_case   (bool) : If True, convert to lowercase first.
        ignore_spaces (bool) : If True, strip all whitespace first.

    Returns:
        str: The normalised string ready for palindrome checking.
    """
    if ignore_spaces:
        s = s.replace(" ", "")     # remove all spaces
    if ignore_case:
        s = s.lower()              # convert to lowercase
    return s


# ─────────────────────────────────────────────────────────────
# APPROACH 1 — Brute Force  O(n) time, O(n) space
# ─────────────────────────────────────────────────────────────

def is_palindrome_brute(s: str) -> bool:
    """
    Check if s is a palindrome by comparing it with its reverse.

    Strategy:
        Create a reversed copy of the string using slice notation [::-1].
        If the original and reversed strings are identical, s is a palindrome.

    Args:
        s (str): The string to check (after any normalisation).

    Returns:
        bool: True if s is a palindrome, False otherwise.

    Time  Complexity: O(n) — reversal visits all n characters once.
    Space Complexity: O(n) — a second string of length n is created in memory.
    """
    # Edge case: empty string and single character are always palindromes
    if len(s) <= 1:
        return True

    reversed_s = s[::-1]           # create a new reversed copy of the string

    return s == reversed_s         # compare original with reversed; True if equal


# ─────────────────────────────────────────────────────────────
# APPROACH 2 — Iterative Two-Pointer  O(n) time, O(1) space
# ─────────────────────────────────────────────────────────────

def is_palindrome_iterative(s: str) -> bool:
    """
    Check if s is a palindrome using two pointers moving inward in a loop.

    Strategy:
        Place one pointer at each end of the string.
        Compare the characters they point to — if they ever differ, return False.
        Move both pointers one step inward and repeat.
        If pointers meet without a mismatch, the string is a palindrome.

    Args:
        s (str): The string to check (after any normalisation).

    Returns:
        bool: True if s is a palindrome, False otherwise.

    Time  Complexity: O(n) — at most n//2 comparisons; early exit on mismatch.
    Space Complexity: O(1) — only two integer index variables used.
    """
    if len(s) <= 1:
        return True

    left  = 0             # left pointer starts at first character
    right = len(s) - 1   # right pointer starts at last character

    while left < right:
        if s[left] != s[right]:       # mismatch found
            return False              # early exit — definitely not a palindrome

        left  += 1                    # move left pointer one step inward (rightward)
        right -= 1                    # move right pointer one step inward (leftward)

    return True                       # all pairs matched → palindrome


# ─────────────────────────────────────────────────────────────
# APPROACH 3 — Recursive  O(n) time, O(n) space
# ─────────────────────────────────────────────────────────────

def is_palindrome_recursive(s: str, left: int, right: int) -> bool:
    """
    Check if s[left..right] is a palindrome using recursion.

    Recurrence Relation:
        is_palindrome(s, left, right)
            = True                                    if left >= right  (base case)
            = False                                   if s[left] != s[right]
            = is_palindrome(s, left+1, right-1)       otherwise (check inner substring)

    Each call reduces the problem to the inner substring (left+1 to right-1),
    shrinking by one character from each end, until the base case is reached.

    Args:
        s     (str) : The string to check.
        left  (int) : Left boundary of the current substring (inclusive).
        right (int) : Right boundary of the current substring (inclusive).

    Returns:
        bool: True if s[left..right] is a palindrome, False otherwise.

    Time  Complexity: O(n) — at most n//2 recursive calls, each O(1) work.
    Space Complexity: O(n) — at most n//2 stack frames alive simultaneously.
    """
    # Base case 1: pointers have met (odd length) or crossed (even length)
    # → all outer pairs matched; the substring is a palindrome
    if left >= right:
        return True

    # Base case 2: outermost characters don't match → not a palindrome; unwind
    if s[left] != s[right]:
        return False

    # Recursive case: outer pair matched; check the inner substring
    return is_palindrome_recursive(s, left + 1, right - 1)


# ─────────────────────────────────────────────────────────────
# DISPLAY HELPER
# ─────────────────────────────────────────────────────────────

def display_result(s: str, result: bool, label: str) -> None:
    """
    Pretty-print the palindrome check result with context.

    Args:
        s      (str)  : The string that was checked.
        result (bool) : True if palindrome, False otherwise.
        label  (str)  : Approach label for display.
    """
    verdict = "PALINDROME ✅" if result else "NOT A PALINDROME ❌"
    print(f"\n  [{label}]")
    print(f"  Input string : \"{s}\"")
    print(f"  Result       : {verdict}")

    # Extra contextual notes
    if len(s) == 0:
        print("  Note: Empty string is vacuously a palindrome.")
    elif len(s) == 1:
        print("  Note: A single character is always a palindrome.")
    elif result and len(s) % 2 == 1:
        mid = len(s) // 2
        print(f"  Note: Odd-length palindrome; centre character is '{s[mid]}' "
              f"(index {mid}) — never moved.")
    elif not result:
        # Find and highlight the first mismatched pair for learning purposes
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                print(f"  First mismatch: s[{i}]='{s[i]}' ≠ s[{j}]='{s[j]}'")
                break


# ─────────────────────────────────────────────────────────────
# MAIN — Menu-driven entry point
# ─────────────────────────────────────────────────────────────

def main() -> None:
    """
    Menu-driven program to check whether a string is a palindrome.

    Options:
        1 → Brute Force   (O(n) time, O(n) space — reverse and compare)
        2 → Iterative     (O(n) time, O(1) space — two-pointer loop)
        3 → Recursive     (O(n) time, O(n) space — call stack)
        4 → All Three     — compare all approaches side by side
        5 → Exit
    """
    # Increase recursion limit for very long strings
    sys.setrecursionlimit(100_000)

    print("=" * 58)
    print("   PALINDROME CHECK — Study Program")
    print("=" * 58)

    while True:
        # ── Menu ──────────────────────────────────────────
        print("\n  Choose an approach:")
        print("  [1] Brute Force  — O(n) time, O(n) space (reverse & compare)")
        print("  [2] Iterative    — O(n) time, O(1) space (two-pointer loop)")
        print("  [3] Recursive    — O(n) time, O(n) space (call stack)")
        print("  [4] All Three    — Compare side by side")
        print("  [5] Exit")
        print("-" * 58)

        choice = input("  Enter choice (1/2/3/4/5): ").strip()

        if choice == "5":
            print("\n  Goodbye! Happy studying. 👋\n")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  ⚠  Invalid choice. Enter 1, 2, 3, 4, or 5.\n")
            continue

        # ── Get string input ──────────────────────────────
        raw = input("\n  Enter a string: ")

        # ── Optional normalisation ─────────────────────────
        print("\n  Normalisation options (press Enter to skip both):")
        ci = input("    Ignore case? (y/n): ").strip().lower() == "y"
        is_ = input("    Ignore spaces? (y/n): ").strip().lower() == "y"

        s = normalise(raw, ignore_case=ci, ignore_spaces=is_)

        if s != raw:
            print(f"\n  Normalised string: \"{s}\"")

        # Warn before deep recursion
        if choice in ("3", "4") and len(s) > 5000:
            print(f"  ⚠  String length {len(s)} may hit recursion limits. "
                  f"Use Iterative for very long strings.\n")

        # ── Run selected approach ──────────────────────────
        if choice == "1":
            result = is_palindrome_brute(s)
            display_result(s, result, "Brute Force — O(n) space")

        elif choice == "2":
            result = is_palindrome_iterative(s)
            display_result(s, result, "Iterative Two-Pointer — O(1) space")

        elif choice == "3":
            try:
                result = is_palindrome_recursive(s, 0, len(s) - 1)
                display_result(s, result, "Recursive — O(n) stack space")
            except RecursionError:
                print("  ❌ RecursionError: string too long for recursive approach.")
                print("     Use the Iterative approach for very long strings.")

        elif choice == "4":
            bf_result   = is_palindrome_brute(s)
            iter_result = is_palindrome_iterative(s)
            display_result(s, bf_result,
                           "Brute Force      — O(n) space")
            display_result(s, iter_result,
                           "Iterative        — O(1) space")
            try:
                rec_result = is_palindrome_recursive(s, 0, len(s) - 1)
                display_result(s, rec_result,
                               "Recursive        — O(n) stack space")
                all_match = bf_result == iter_result == rec_result
                match = "✅ All Match" if all_match else "❌ Mismatch!"
                print(f"\n  Consistency check : {match}")
            except RecursionError:
                print("\n  ❌ Recursive approach hit stack limit for this string length.")
                match = "✅ Match" if bf_result == iter_result else "❌ Mismatch!"
                print(f"  Brute Force vs Iterative : {match}")

        print()   # blank line before next menu


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
```

---

## 6. Dry Run

We use **s = "racecar"** (palindrome, odd length) and **s = "hello"** (not a palindrome)
across all three approaches.

---

### Brute Force Dry Run — s = "racecar"

| Step | Operation                          | Result          | Explanation                               |
|------|------------------------------------|-----------------|-------------------------------------------|
| 1    | s = "racecar"                      | —               | Original string                           |
| 2    | reversed_s = s[::-1]               | "racecar"       | Reversed string created in new memory     |
| 3    | s == reversed_s → "racecar" == "racecar" | True      | Strings are identical character by character |
| End  | return True                        | **PALINDROME ✅**| Both strings match → palindrome confirmed |

---

### Brute Force Dry Run — s = "hello"

| Step | Operation                          | Result           | Explanation                          |
|------|------------------------------------|------------------|--------------------------------------|
| 1    | s = "hello"                        | —                | Original string                      |
| 2    | reversed_s = s[::-1]               | "olleh"          | Reversed copy created                |
| 3    | s == reversed_s → "hello" == "olleh"| False           | Strings differ → not a palindrome    |
| End  | return False                       | **NOT PALINDROME ❌** | Mismatch detected                |

---

### Iterative Two-Pointer Dry Run — s = "racecar" (n = 7)

| Step | left | right | s[left] | s[right] | Match? | left After | right After | Explanation                         |
|------|------|-------|---------|----------|--------|------------|-------------|-------------------------------------|
| Init | 0    | 6     | —       | —        | —      | —          | —           | Pointers placed at both ends        |
| 1    | 0    | 6     | 'r'     | 'r'      | ✅     | 1          | 5           | Outer pair matches; move inward     |
| 2    | 1    | 5     | 'a'     | 'a'      | ✅     | 2          | 4           | Second pair matches; move inward    |
| 3    | 2    | 4     | 'c'     | 'c'      | ✅     | 3          | 3           | Third pair matches; move inward     |
| 4    | 3    | 3     | —       | —        | —      | —          | —           | left(3) < right(3) is FALSE → exit  |
| End  | —    | —     | —       | —        | —      | —          | —           | **PALINDROME ✅**                   |

> Only **3 comparisons** for a 7-character string — exactly `n // 2` comparisons.
> Centre character `'e'` (index 3) was never compared — it has no pair.

---

### Iterative Two-Pointer Dry Run — s = "hello" (n = 5)

| Step | left | right | s[left] | s[right] | Match? | Action                                |
|------|------|-------|---------|----------|--------|---------------------------------------|
| Init | 0    | 4     | —       | —        | —      | Pointers placed at both ends          |
| 1    | 0    | 4     | 'h'     | 'o'      | ❌     | Mismatch → return False immediately   |
| End  | —    | —     | —       | —        | —      | **NOT PALINDROME ❌ (early exit)**     |

> Only **1 comparison** needed — the two-pointer approach exits the moment a
> mismatch is found, saving all remaining comparisons.

---

### Recursive Dry Run — s = "racecar"

#### Winding Phase (calls descending into the stack)

| Call Depth | Function Call                        | left | right | s[left] | s[right] | Check           |
|------------|--------------------------------------|------|-------|---------|----------|-----------------|
| 1          | is_palindrome("racecar", 0, 6)       | 0    | 6     | 'r'     | 'r'      | Match ✅ → recur |
| 2          | is_palindrome("racecar", 1, 5)       | 1    | 5     | 'a'     | 'a'      | Match ✅ → recur |
| 3          | is_palindrome("racecar", 2, 4)       | 2    | 4     | 'c'     | 'c'      | Match ✅ → recur |
| 4          | is_palindrome("racecar", 3, 3)       | 3    | 3     | —       | —        | left >= right ✅ → **BASE CASE** → return True |

> Stack at deepest point: **4 frames** simultaneously in memory.

#### Unwinding Phase (True bubbling back up)

| Call Depth | Receives | Computes         | Returns to Depth |
|------------|----------|------------------|------------------|
| 4          | —        | return True      | Depth 3          |
| 3          | True     | return True      | Depth 2          |
| 2          | True     | return True      | Depth 1          |
| 1          | True     | return True      | Caller (main)    |

> **Final Answer: True ✅** — "racecar" is a palindrome.

---

### Recursive Dry Run — s = "hello"

#### Winding Phase

| Call Depth | Function Call                   | left | right | s[left] | s[right] | Check              |
|------------|---------------------------------|------|-------|---------|----------|--------------------|
| 1          | is_palindrome("hello", 0, 4)    | 0    | 4     | 'h'     | 'o'      | Mismatch ❌ → **BASE CASE** → return False immediately |

> Stack never grows beyond **1 frame** — the mismatch is caught at the outermost call.
> No further recursion occurs.

> **Final Answer: False ❌** — "hello" is not a palindrome.

---

### Full Recursive Call Tree — s = "racecar"

```
is_palindrome("racecar", 0, 6)            depth 1
└── 'r' == 'r' ✅
    └── is_palindrome("racecar", 1, 5)    depth 2
        └── 'a' == 'a' ✅
            └── is_palindrome("racecar", 2, 4)    depth 3
                └── 'c' == 'c' ✅
                    └── is_palindrome("racecar", 3, 3)    depth 4
                        └── left(3) >= right(3)
                            └── return True  ← BASE CASE

Unwind:
                    return True   ↑
            return True           ↑
    return True                   ↑
return True ──────────────────────↑  ← final answer
```

---

### Comparison Across All Three — s = "racecar" (n = 7)

| Property             | Brute Force         | Iterative           | Recursive           |
|----------------------|---------------------|---------------------|---------------------|
| New string created?  | Yes ("racecar")     | No                  | No                  |
| Comparisons made     | 7 (full == check)   | 3 (n // 2)          | 3 (n // 2)          |
| Stack frames used    | 1                   | 1                   | 4 (n//2 + 1)        |
| Early exit?          | No (always compares all) | ✅ Yes         | ✅ Yes              |
| Final answer         | True ✅             | True ✅             | True ✅             |

---

## 7. Time & Space Complexity

### Brute Force — Reverse and Compare

| Case         | Time Complexity | Explanation                                                              |
|--------------|-----------------|--------------------------------------------------------------------------|
| Best Case    | O(n)            | Reversal always visits all n characters, even for obvious non-palindromes|
| Worst Case   | O(n)            | Identical process regardless of string content                           |
| Average Case | O(n)            | Always n steps to reverse + n steps for equality check = 2n = O(n)      |

| Space Complexity | O(n) | A completely new reversed string of length n is allocated. Both the original and reversed strings occupy memory simultaneously. |
|---|---|---|

---

### Iterative Two-Pointer

| Case         | Time Complexity | Explanation                                                                        |
|--------------|-----------------|------------------------------------------------------------------------------------|
| Best Case    | O(1)            | First pair mismatches (e.g., "ab") → returns False after 1 comparison; early exit |
| Worst Case   | O(n)            | String is a palindrome → all n//2 pairs must be checked; no early exit possible    |
| Average Case | O(n)            | For random strings, mismatch found somewhere in the first half on average          |

| Space Complexity | O(1) | Only two integer variables (`left` and `right`) regardless of string length. No new strings, no recursion stack. |
|---|---|---|

---

### Recursive Approach

| Case         | Time Complexity | Explanation                                                                      |
|--------------|-----------------|----------------------------------------------------------------------------------|
| Best Case    | O(1)            | First call catches mismatch (base case 2) → returns immediately, zero further calls |
| Worst Case   | O(n)            | String is a palindrome → n//2 recursive calls made before base case 1 triggers  |
| Average Case | O(n)            | Proportional to how deep the first mismatch (or centre) is                       |

| Space Complexity | O(n) | Each recursive call adds one frame to the call stack. At maximum depth (palindrome case), n//2 + 1 frames exist simultaneously. Stack only unwinds after the base case returns. |
|---|---|---|

---

### Why Recursive Space is O(n) — Visualised

```
Call stack at maximum depth for s = "racecar":

┌─────────────────────────────────────────┐  ← Top of stack
│  is_palindrome("racecar", 3, 3) → True  │  Frame 4  (base case)
├─────────────────────────────────────────┤
│  is_palindrome("racecar", 2, 4)         │  Frame 3
├─────────────────────────────────────────┤
│  is_palindrome("racecar", 1, 5)         │  Frame 2
├─────────────────────────────────────────┤
│  is_palindrome("racecar", 0, 6)         │  Frame 1  (original call)
└─────────────────────────────────────────┘  ← Bottom

4 frames deep for n=7 → O(n) stack space
```

---

### Head-to-Head Summary

| Property              | Brute Force       | Iterative          | Recursive             |
|-----------------------|-------------------|--------------------|-----------------------|
| Time Complexity       | O(n)              | O(n)               | O(n)                  |
| Space Complexity      | **O(n)**          | **O(1)** ← winner  | **O(n)** — call stack |
| Early exit on mismatch| ❌ No             | ✅ Yes             | ✅ Yes                |
| Mutates input?        | No                | No                 | No                    |
| Easiest to read?      | ✅ Very clear     | Clear              | Mirrors maths exactly |
| Safe for large input? | ✅ Yes            | ✅ Yes             | ⚠️ Stack limit risk   |
| Best used when        | Quick prototype   | Production code    | Teaching recursion    |

---

## 8. Beginner Tips

### 🧠 Core Intuition Hacks

1. **Mirror symmetry**: A palindrome is a string that is its own mirror. Every character
   at distance `k` from the left must equal the character at distance `k` from the right.
   Two-pointer directly encodes this — one pointer on each side of the mirror.

2. **n // 2 comparisons is the ceiling**: You never need more than `n // 2` comparisons
   to decide. Each comparison simultaneously verifies two positions. The centre element
   (for odd-length strings) needs no partner.

3. **Early exit is your friend**: For non-palindromes, the first mismatch terminates
   immediately. Brute force has no early exit — it always reverses the full string
   before checking. The iterative and recursive approaches both exploit this.

4. **Recursion = loop on the call stack**: The recursive palindrome check is logically
   identical to the iterative version — both compare the same pairs in the same order.
   The only difference is *where* the state (left, right pointers) lives: in variables
   (iterative) or in stack frames (recursive).

5. **`left >= right` not `left == right`**: Using `>=` handles both odd-length
   (pointers meet at centre: `left == right`) and even-length (pointers cross:
   `left > right`) strings. Using `==` would miss the even-length termination case.

---

### ⚠️ Edge Case Reminders

| Input            | Expected  | Common Mistake                                              |
|------------------|-----------|-------------------------------------------------------------|
| `""` (empty)     | True      | Returning False or crashing on `s[0]` access               |
| `"a"` (1 char)   | True      | `left=0, right=0` → `left >= right` triggers immediately ✅ |
| `"aa"` (2 chars) | True      | One comparison: s[0]==s[1]; then left(1) < right(0) → done |
| `"ab"` (2 chars) | False     | One comparison: s[0]!=s[1] → False ✅                      |
| `"Racecar"`      | False*    | Case-sensitive by default; normalise with `.lower()` first  |
| `"race car"`     | False*    | Space at index 3 breaks symmetry; strip spaces if needed    |
| `"A man a plan a canal Panama"` | True* | Only after `.lower().replace(" ", "")` |

> *Depends on whether case/space normalisation is applied.

---

### 🔬 The `left >= right` Base Case — Both Parities Covered

```python
# Odd length:  "racecar" (n=7)
# Pointers meet at centre: left=3, right=3 → left >= right (==) → True ✅

# Even length: "noon" (n=4)
# Pointers cross each other: left=2, right=1 → left >= right (>) → True ✅

# Using left == right would MISS the even-length case:
# left=2 > right=1 → condition left == right is False → would enter the body
# wrongly → incorrect comparison of s[2] and s[1] which are already processed!

# ✅ Always use >= in the recursive/iterative palindrome base case.
```

---

### 🔬 Python's Built-in Options

```python
s = "racecar"

# Option 1: Slice reversal — clearest one-liner
print(s == s[::-1])           # True

# Option 2: reversed() with join
print(s == "".join(reversed(s)))   # True

# Option 3: Manual iterative (shown in this document)
# — preferred in interviews; shows you understand the algorithm
```

> Know all three exist — but interviewers want to see the manual implementation.
> `s == s[::-1]` is the production one-liner; two-pointer is the interview answer.

---

### 🔬 Case-Insensitive and Space-Stripped Palindrome

```python
s = "A man a plan a canal Panama"

# Step 1: normalise
cleaned = s.lower().replace(" ", "")
# cleaned = "amanaplanacanalpanama"

# Step 2: check
print(cleaned == cleaned[::-1])   # True ✅
```

> Many real-world palindrome problems (LeetCode 125) require this preprocessing step.
> Always clarify with the interviewer: *"Should I ignore case and non-alphanumeric characters?"*

---

### ⚖️ When To Use Which Approach

| Situation                                       | Recommended Approach                         |
|-------------------------------------------------|----------------------------------------------|
| Learning palindrome / first exposure            | Brute force (clearest logic)                 |
| Learning recursion as a concept                 | Recursive (textbook example of structural recursion) |
| Any production or interview code                | Iterative two-pointer (O(1) space, no stack risk) |
| Very long strings (n > 10,000)                  | Iterative only (recursion hits Python's limit)|
| Quick one-liner in Python                       | `s == s[::-1]`                               |
| Checking palindrome in a subarray or substring  | Iterative with custom `left`, `right` bounds |

---

### 📏 Rules of Thumb

- **Two-pointer = symmetric problems**: Anytime a problem has mirror/symmetric structure
  — palindromes, two-sum in sorted arrays, container with most water — reach for two
  pointers. This is one of the most versatile patterns in all of competitive programming.

- **Recursion depth limit**: Python's default is 1000 frames. For strings longer than
  ~998 characters, the recursive approach will raise `RecursionError` unless you call
  `sys.setrecursionlimit()`. The iterative approach has no such constraint.

- **Odd vs Even**: For odd-length palindromes, the centre character is **never** involved
  in any comparison — it's always in the right place. For even-length palindromes, all
  characters pair up perfectly. Your code must handle both — `left >= right` does this.

- **Preprocessing matters**: Strip, lowercase, and remove non-alphanumeric characters
  *before* the palindrome check whenever the problem is about natural language strings.
  Do this as a separate step to keep the core logic clean.

- **Recursion mirrors the mathematical definition**: `is_palindrome(s) = s[0]==s[-1]
  AND is_palindrome(s[1:-1])`. The recursive code is essentially this definition
  written in Python — elegant but at a space cost.

---

### 🔗 Related Problems to Practice Next

| Problem                              | Key Concept Shared                                    |
|--------------------------------------|-------------------------------------------------------|
| Valid Palindrome II (delete one char)| Two-pointer with one allowed skip                     |
| Longest Palindromic Substring        | Expand-around-centre; two-pointer from middle out     |
| Palindrome Partitioning              | Recursion + palindrome check at each split            |
| Reverse a String / Array             | Same two-pointer swap logic                           |
| Check if Linked List is Palindrome   | Two-pointer (slow/fast) + reverse second half         |
| Count Palindromic Substrings         | Expand-around-centre for every index                  |
| Shortest Palindrome (add prefix)     | KMP / string hashing on palindrome structure          |

---

*End of Study Notes — Palindrome Check (String)*