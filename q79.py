file_name = "example.txt"
with open(file_name, "r") as file:
    contents = file.read()
    words = contents.split()
    print(f"Number of words in {file_name}: {len(words)}")
