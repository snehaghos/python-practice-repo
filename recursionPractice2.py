# Recursion Practice 2 - Short & Focused
# Covers: count occurrences, decimal to binary, print numbers,
#         array sum, max element, string length, list reversal

# --- 1. Count Digits ---
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

# --- 2. Decimal to Binary ---
def to_binary(n):
    if n <= 1:
        return str(n)
    return to_binary(n // 2) + str(n % 2)

# --- 3. Print 1 to N ---
def print_1_to_n(n):
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

# --- 4. Print N to 1 ---
def print_n_to_1(n):
    if n < 1:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

# --- 5. Sum of Array ---
def array_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + array_sum(arr, index + 1)

# --- 6. Max in Array ---
def array_max(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    rest_max = array_max(arr, index + 1)
    return arr[index] if arr[index] > rest_max else rest_max

# --- 7. String Length (without len) ---
def str_length(s):
    if s == "":
        return 0
    return 1 + str_length(s[1:])

# --- 8. Reverse List ---
def reverse_list(arr):
    if len(arr) <= 1:
        return arr
    return [arr[-1]] + reverse_list(arr[:-1])

# --- 9. Count Vowels ---
def count_vowels(s):
    if not s:
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])

# --- 10. Collatz Steps ---
def collatz_steps(n, steps=0):
    if n == 1:
        return steps
    if n % 2 == 0:
        return collatz_steps(n // 2, steps + 1)
    return collatz_steps(3 * n + 1, steps + 1)

if __name__ == "__main__":
    print("=== 1. Count Digits ===")
    print("  12345 ->", count_digits(12345))
    print("  9     ->", count_digits(9))

    print("\n=== 2. Decimal to Binary ===")
    print("  10 ->", to_binary(10))
    print("  25 ->", to_binary(25))
    print(" 255 ->", to_binary(255))

    print("\n=== 3. Print 1 to N ===")
    print("  1 to 10: ", end="")
    print_1_to_n(10)
    print()

    print("\n=== 4. Print N to 1 ===")
    print("  10 to 1: ", end="")
    print_n_to_1(10)
    print()

    print("\n=== 5. Array Sum ===")
    nums = [3, 7, 2, 9, 4]
    print("  Array:", nums)
    print("  Sum:", array_sum(nums))

    print("\n=== 6. Max in Array ===")
    print("  Array:", nums)
    print("  Max:", array_max(nums))

    print("\n=== 7. String Length ===")
    print("  'Python' ->", str_length("Python"))
    print("  ''       ->", str_length(""))

    print("\n=== 8. Reverse List ===")
    lst = [1, 2, 3, 4, 5]
    print("  Original:", lst)
    print("  Reversed:", reverse_list(lst))

    print("\n=== 9. Count Vowels ===")
    print("  'Hello World' ->", count_vowels("Hello World"))
    print("  'Programming' ->", count_vowels("Programming"))

    print("\n=== 10. Collatz Steps ===")
    print("  (3n+1 problem: if even n/2, if odd 3n+1, until 1)")
    print("  Steps to reach 1:")
    for n in [6, 11, 27, 100]:
        print(f"    {n} -> {collatz_steps(n)} steps")
