# Credit card number validation program
# Uses the Luhn algorithm (used by banks worldwide)
# Supports card numbers from 13 to 19 digits
# Detects card type: Visa, MasterCard, Amex, Discover
# Must contain only digits (spaces and dashes are allowed)

def get_card_type(number):
    if number.startswith("4"):
        return "Visa"
    elif number.startswith("51") or number.startswith("52") or number.startswith("53") or number.startswith("54") or number.startswith("55"):
        return "MasterCard"
    elif number.startswith("34") or number.startswith("37"):
        return "American Express"
    elif number.startswith("6011") or number.startswith("65"):
        return "Discover"
    else:
        return "Unknown"

def luhn_check(number):
    digits = [int(d) for d in number]
    digits.reverse()
    
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    return total % 10 == 0

def is_valid_credit_card(card):
    if not card:
        return False, "Card number required"
    
    cleaned = card.replace(" ", "").replace("-", "")
    
    if not cleaned.isdigit():
        return False, "Invalid Card !! Must contain only digits"
    
    if len(cleaned) < 13:
        return False, f"Invalid Card !! Too short ({len(cleaned)} digits, need at least 13)"
    
    if len(cleaned) > 19:
        return False, f"Invalid Card !! Too long ({len(cleaned)} digits, max is 19)"
    
    if not luhn_check(cleaned):
        return False, "Invalid Card !! Failed Luhn checksum"
    
    card_type = get_card_type(cleaned)
    return True, f"OK ({card_type})"

user_input = input("Enter your credit card number: ")
valid, reason = is_valid_credit_card(user_input)
if valid:
    print("Valid credit card", reason)
else:
    print("Invalid credit card:", reason)
