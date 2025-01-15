file_name = input("Enter the file name: ")
text = input("Enter the text to append: ")

try:
    with open(file_name, "a") as file:
        file.write(text + "\n")
        print("Text appended successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
