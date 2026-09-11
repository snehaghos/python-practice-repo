import sys



def is_palindrome(s: str) -> bool:
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        try:
            text = input("Enter text: ")
        except EOFError:
            return
    print("Palindrome" if is_palindrome(text) else "Not a palindrome")

if __name__ == "__main__":
    main()