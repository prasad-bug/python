def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

# Example usage
text = input("Enter a string: ")
print(f"The length of the string is: {string_length(text)}")
