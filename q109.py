import re

# Example string
text = "Contact us at support@example.com or sales@mywebsite.org."

# Extract all email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Email addresses found:", emails)
