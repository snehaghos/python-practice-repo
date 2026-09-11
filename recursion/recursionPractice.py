# Recursion in Python
# Covers: factorial, fibonacci, power, sum of digits, reverse string,
#         tower of hanoi, GCD, binary search, palindrome check, flood fill

# --- 1. Factorial ---
# n! = n * (n-1)!
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# --- 2. Fibonacci ---
# fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_list(count):
    result = []
    for i in range(count):
        result.append(fibonacci(i))
    return result

# --- 3. Power ---
# x^n = x * x^(n-1)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# --- 4. Sum of Digits ---
def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

# --- 5. Reverse String ---
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# --- 6. Check Palindrome ---
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# --- 7. GCD (Euclid's Algorithm) ---
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# --- 8. Tower of Hanoi ---
def tower_of_hanoi(n, source, auxiliary, target, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return moves
    tower_of_hanoi(n - 1, source, target, auxiliary, moves)
    moves.append(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target, moves)
    return moves

# --- 9. Binary Search (Recursive) ---
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

# --- 10. Flatten Nested List ---
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# --- 11. Power Set (all subsets) ---
def power_set(items):
    if not items:
        return [[]]
    first = items[0]
    rest = power_set(items[1:])
    with_first = [[first] + subset for subset in rest]
    return rest + with_first

# --- 12. Count Permutations ---
def count_permutations(n):
    if n <= 1:
        return 1
    return n * count_permutations(n - 1)

if __name__ == "__main__":
    print("=== 1. Factorial ===")
    for i in range(1, 8):
        print(f"  {i}! = {factorial(i)}")

    print("\n=== 2. Fibonacci (first 10) ===")
    print(" ", fibonacci_list(10))

    print("\n=== 3. Power ===")
    print("  2^10 =", power(2, 10))
    print("  3^5  =", power(3, 5))

    print("\n=== 4. Sum of Digits ===")
    print("  sum_of_digits(12345) =", sum_of_digits(12345))
    print("  sum_of_digits(999)   =", sum_of_digits(999))

    print("\n=== 5. Reverse String ===")
    print("  reverse('hello') =", reverse_string("hello"))
    print("  reverse('Python') =", reverse_string("Python"))

    print("\n=== 6. Palindrome Check ===")
    print("  'racecar' palindrome?", is_palindrome("racecar"))
    print("  'madam' palindrome?", is_palindrome("madam"))
    print("  'hello' palindrome?", is_palindrome("hello"))

    print("\n=== 7. GCD ===")
    print("  gcd(12, 8)  =", gcd(12, 8))
    print("  gcd(100, 75) =", gcd(100, 75))

    print("\n=== 8. Tower of Hanoi (3 disks) ===")
    for move in tower_of_hanoi(3, "A", "B", "C"):
        print(" ", move)

    print("\n=== 9. Binary Search ===")
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 67, 91]
    print("  Array:", arr)
    print("  Search 23 -> index:", binary_search(arr, 23, 0, len(arr) - 1))
    print("  Search 50 -> index:", binary_search(arr, 50, 0, len(arr) - 1))

    print("\n=== 10. Flatten Nested List ===")
    nested = [1, [2, 3], [4, [5, 6, [7, 8]]], 9]
    print("  Input:", nested)
    print("  Flat: ", flatten(nested))

    print("\n=== 11. Power Set ===")
    items = ["a", "b", "c"]
    print("  Items:", items)
    subsets = power_set(items)
    print(f"  Subsets ({len(subsets)}):")
    for s in subsets:
        print("   ", s)

    print("\n=== 12. Count Permutations ===")
    for i in range(1, 8):
        print(f"  {i} items can be arranged in {count_permutations(i)} ways")
