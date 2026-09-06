# Phone number validation program
# Supports formats: 10 digits, +country code, with dashes or spaces
# Must contain only digits, +, -, and spaces
# After removing +, -, spaces, must be 10 to 15 digits
# Cannot start with 0 after country code
# No special characters like letters or symbols

def is_valid_phone(phone):
    if not phone:
        return False, "Phone number required"
    
    cleaned = phone.replace(" ", "").replace("-", "")
    
    if cleaned.startswith("+"):
        cleaned = cleaned[1:]
    
    if not cleaned.isdigit():
        return False, "Invalid Phone !! Must contain only digits (and +, -, spaces)"
    
    if len(cleaned) < 10:
        return False, f"Invalid Phone !! Too short ({len(cleaned)} digits, need at least 10)"
    
    if len(cleaned) > 15:
        return False, f"Invalid Phone !! Too long ({len(cleaned)} digits, max is 15)"
    
    if cleaned[0] == "0":
        return False, "Invalid Phone !! Number cannot start with 0"
    
    if phone[0] == "+" and len(cleaned) < 11:
        return False, "Invalid Phone !! Country code number seems too short"
    
    if phone.count("+") > 1:
        return False, "Invalid Phone !! Cannot contain more than one +"
    
    return True, "OK"

user_input = input("Enter your phone number: ")
valid, reason = is_valid_phone(user_input)
if valid:
    print("Valid phone number")
else:
    print("Invalid phone:", reason)
