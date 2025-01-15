source_file = "example.txt"
destination_file = "copy_example.txt"

with open(source_file, "r") as source:
    data = source.read()

with open(destination_file, "w") as destination:
    destination.write(data)

print(f"Contents copied from {source_file} to {destination_file}.")
