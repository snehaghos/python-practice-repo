# Email validation program
# Must contain exactly one @ symbol
# Username part must not be empty
# Domain part must not be empty
# Domain must contain at least one dot
# No spaces allowed
# Username can contain letters, digits, dots, underscores, hyphens
# Domain can contain letters, digits, dots, hyphens

def is_valid_email(email):
    if not email:
        return False, "Email required"
    
    if " " in email:
        return False, "Invalid Email !! Spaces are not allowed"
    
    if email.count("@") != 1:
        return False, "Invalid Email !! Must contain exactly one @ symbol"
    
    username, domain = email.split("@")
    
    if not username:
        return False, "Invalid Email !! Username part cannot be empty"
    
    if not domain:
        return False, "Invalid Email !! Domain part cannot be empty"
    
    if "." not in domain:
        return False, "Invalid Email !! Domain must contain at least one dot"
    
    allowed_username = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
    for char in username:
        if char not in allowed_username:
            return False, f"Invalid Email !! Username contains invalid character '{char}'"
    
    allowed_domain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
    for char in domain:
        if char not in allowed_domain:
            return False, f"Invalid Email !! Domain contains invalid character '{char}'"
    
    if domain.startswith(".") or domain.endswith("."):
        return False, "Invalid Email !! Domain cannot start or end with a dot"
    
    if domain.count(".") < 1:
        return False, "Invalid Email !! Domain must have at least one dot"
    
    tld = domain.split(".")[-1]
    if len(tld) < 2:
        return False, "Invalid Email !! Top-level domain must be at least 2 characters"
    
    return True, "OK"

user_input = input("Enter your email: ")
valid, reason = is_valid_email(user_input)
if valid:
    print("Valid email address")
else:
    print("Invalid email:", reason)
