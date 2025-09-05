import re
import string
def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]+", password):
        return False
    if not re.search(r"[a-z]+", password):
        return False
    if not re.search(r"[0-9]+", password):
        return False
    if not re.search(f"[{re.escape(string.punctuation)}]", password):
        return False
    return True

input_password = input("Enter a password to check its strength: ")
if is_strong_password(input_password):
    print("The password is strong.")
else:
    print("The password is weak.")