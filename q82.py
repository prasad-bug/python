file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        print(f"The longest word is '{longest_word}' with length {len(longest_word)}.")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
