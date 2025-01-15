file_name = input("Enter the file name: ")
substring = input("Enter the substring to search for: ")

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            if substring in line:
                print(f"Substring found on line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
