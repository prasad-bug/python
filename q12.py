def is_palindrome(s):
    # Remove any spaces and convert to lowercase
    s = s.replace(" ","").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
