#password checkinng 
#first charecter should be Capital 
# last Charecter should be small
# length should be 8
#numeric value should be there
#Consecutive charetcters are not accepted
#User input should be there

def is_valid_password(password):
    if not password:
        return False, "Password required"
    if len(password) < 8:
        return False, "Weak Password !! Password must be at least 8 characters"
    if not password[0].isupper():
        return False, "Weak Password !! First character must be uppercase"
    if not password[-1].islower():
        return False, "Weak Password !! Last character must be lowercase"
    if not any(char.isdigit() for char in password):
        return False, "Weak Password !! Must include at least one digit"
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False, "Weak Password !! Three consecutive identical characters are not allowed"
    return True, "OK"

user_input = input("Enter your password: ")
valid, reason = is_valid_password(user_input)
if valid:
    print("Valid password")
else:
    print("Weak password:", reason)
