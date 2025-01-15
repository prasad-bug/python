file_name = "example.txt"
with open(file_name, "r") as file:
    lines = file.readlines()
    print(f"Number of lines in {file_name}: {len(lines)}")
