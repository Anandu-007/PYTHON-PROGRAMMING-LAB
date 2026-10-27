import re

# Email validation
email = input("Enter email address: ")

if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
    print("Valid email")
else:
    print("Invalid email")

# Phone number validation (10 digits)
phone = input("Enter 10-digit phone number: ")

if re.fullmatch(r"[6-9][0-9]{9}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

# Extract transaction IDs from logs
log = input("Enter log message: ")

ids = re.findall(r"TXN[0-9]+", log)

print("Transaction IDs:", ids)