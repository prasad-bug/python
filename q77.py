file_name = "output.txt"
text = input("Enter a line of text: ")
with open(file_name, "w") as file:
    file.write(text)
print(f"Text written to {file_name}.")
