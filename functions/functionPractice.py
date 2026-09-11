# Functions in Python
# Covers: basic functions, default args, *args, **kwargs, return values,
#         nested functions, lambda, higher-order functions

# --- 1. Basic Function ---
def greet(name):
    return "Hello, " + name + "!"

# --- 2. Function with Default Arguments ---
def power(base, exp=2):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# --- 3. Multiple Return Values ---
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

# --- 4. *args - Variable number of positional arguments ---
def total(*args):
    sum_val = 0
    for num in args:
        sum_val += num
    return sum_val

# --- 5. **kwargs - Variable number of keyword arguments ---
def build_profile(name, **kwargs):
    profile = {"name": name}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

# --- 6. Nested Function ---
def outer(msg):
    def inner():
        print("  Inner says:", msg)
    print("  Outer says:", msg)
    inner()

# --- 7. Function as Argument (Higher Order Function) ---
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

# --- 8. Lambda Functions ---
square = lambda x: x * x
add = lambda a, b: a + b

# --- 9. Map and Filter ---
def double_list(numbers):
    return list(map(lambda x: x * 2, numbers))

def even_only(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# --- 10. Recursive Function ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# --- 11. Function with Docstring ---
def is_palindrome(text):
    """Check if a given text is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print("=== 1. Basic Function ===")
    print(greet("Alice"))

    print("\n=== 2. Default Arguments ===")
    print("power(3):", power(3))
    print("power(2, 5):", power(2, 5))

    print("\n=== 3. Multiple Return Values ===")
    nums = [4, 2, 9, 1, 7]
    low, high = min_max(nums)
    print("Numbers:", nums)
    print("Min:", low, "Max:", high)

    print("\n=== 4. *args ===")
    print("total(1,2,3,4,5):", total(1, 2, 3, 4, 5))

    print("\n=== 5. **kwargs ===")
    profile = build_profile("Bob", age=25, city="Mumbai", job="Developer")
    print("Profile:", profile)

    print("\n=== 6. Nested Function ===")
    outer("Hi there!")

    print("\n=== 7. Higher Order Function ===")
    print("apply_twice(double, 3):", apply_twice(double, 3))

    print("\n=== 8. Lambda Functions ===")
    print("square(7):", square(7))
    print("add(10, 20):", add(10, 20))

    print("\n=== 9. Map and Filter ===")
    numbers = [1, 2, 3, 4, 5, 6]
    print("Original:", numbers)
    print("Doubled:", double_list(numbers))
    print("Even only:", even_only(numbers))

    print("\n=== 10. Recursion (Factorial) ===")
    for i in range(1, 8):
        print(f"  {i}! = {factorial(i)}")

    print("\n=== 11. Docstring ===")
    print("Is 'racecar' palindrome?", is_palindrome("racecar"))
    print("Is 'hello' palindrome?", is_palindrome("hello"))
