# URL validation program
# Must start with http:// or https://
# Must contain a domain name (at least one dot)
# Domain cannot start or end with a dot or hyphen
# No spaces allowed
# Path部分 can contain letters, digits, /, -, _, ., ~, %
# Port number if present must be between 1 and 65535

def is_valid_url(url):
    if not url:
        return False, "URL required"
    
    if " " in url:
        return False, "Invalid URL !! Spaces are not allowed"
    
    if not url.startswith("http://") and not url.startswith("https://"):
        return False, "Invalid URL !! Must start with http:// or https://"
    
    without_protocol = url[7:] if url.startswith("http://") else url[8:]
    
    if "/" in without_protocol:
        domain_and_path = without_protocol.split("/", 1)
        domain_part = domain_and_path[0]
    else:
        domain_part = without_protocol
    
    if ":" in domain_part:
        domain_pieces = domain_part.split(":")
        domain_name = domain_pieces[0]
        port_str = domain_pieces[1]
        if not port_str.isdigit():
            return False, "Invalid URL !! Port must be a number"
        port = int(port_str)
        if port < 1 or port > 65535:
            return False, f"Invalid URL !! Port must be between 1 and 65535 (got {port})"
    else:
        domain_name = domain_part
    
    if not domain_name:
        return False, "Invalid URL !! Domain name cannot be empty"
    
    if "." not in domain_name:
        return False, "Invalid URL !! Domain must contain at least one dot"
    
    if domain_name.startswith(".") or domain_name.startswith("-"):
        return False, "Invalid URL !! Domain cannot start with a dot or hyphen"
    
    if domain_name.endswith(".") or domain_name.endswith("-"):
        return False, "Invalid URL !! Domain cannot end with a dot or hyphen"
    
    return True, "OK"

user_input = input("Enter your URL: ")
valid, reason = is_valid_url(user_input)
if valid:
    print("Valid URL")
else:
    print("Invalid URL:", reason)
