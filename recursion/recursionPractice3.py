# Recursion Practice 3 - Extra Short & Simple
# Quick bite-sized recursion problems

# --- 1. Sum of 1 to N ---
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

# --- 2. Product of Array ---
def product(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * product(arr[1:])

# --- 3. Is Array Sorted ---
def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted(arr[1:])

# --- 4. Remove Duplicates from String ---
def remove_duplicates(s, index=0, seen=""):
    if index == len(s):
        return seen
    if s[index] not in seen:
        return remove_duplicates(s, index + 1, seen + s[index])
    return remove_duplicates(s, index + 1, seen)

# --- 5. Pair Star (add * between same adjacent) ---
def pair_star(s):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + "*" + pair_star(s[1:])
    return s[0] + pair_star(s[1:])

# --- 6. Multiply Without * Operator ---
def multiply(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -multiply(a, -b)
    return a + multiply(a, b - 1)

# --- 7. Check Balanced Parentheses ---
def is_balanced(s, count=0):
    if not s:
        return count == 0
    if s[0] == "(":
        return is_balanced(s[1:], count + 1)
    if s[0] == ")":
        if count == 0:
            return False
        return is_balanced(s[1:], count - 1)
    return is_balanced(s[1:], count)

# --- 8. Find Position of Element ---
def find_index(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return find_index(arr, target, index + 1)

if __name__ == "__main__":
    print("=== 1. Sum of 1 to N ===")
    print("  sum_n(10) =", sum_n(10))
    print("  sum_n(100) =", sum_n(100))

    print("\n=== 2. Product of Array ===")
    nums = [2, 3, 4, 5]
    print("  [2,3,4,5] ->", product(nums))

    print("\n=== 3. Is Array Sorted ===")
    print("  [1,2,3,4,5] ->", is_sorted([1, 2, 3, 4, 5]))
    print("  [1,3,2,4,5] ->", is_sorted([1, 3, 2, 4, 5]))

    print("\n=== 4. Remove Duplicates ===")
    print("  'abracadabra' ->", remove_duplicates("abracadabra"))
    print("  'programming' ->", remove_duplicates("programming"))

    print("\n=== 5. Pair Star ===")
    print("  'hello'     ->", pair_star("hello"))
    print("  'aaaa'      ->", pair_star("aaaa"))
    print("  'xxyyzz'    ->", pair_star("xxyyzz"))

    print("\n=== 6. Multiply Without * ===")
    print("  5 x 3  =", multiply(5, 3))
    print("  7 x 10 =", multiply(7, 10))

    print("\n=== 7. Balanced Parentheses ===")
    print("  '(())'     ->", is_balanced("(())"))
    print("  '(()'      ->", is_balanced("(()"))
    print("  ')(()'     ->", is_balanced(")(()"))
    print("  '(()())()' ->", is_balanced("(()())()"))

    print("\n=== 8. Find Index ===")
    arr = [10, 20, 30, 40, 50]
    print("  Array:", arr)
    print("  Find 30 -> index", find_index(arr, 30))
    print("  Find 99 -> index", find_index(arr, 99))
