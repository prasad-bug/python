import json

# Example JSON file
file_path = "data.json"

# Read JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Modify a value
data['key'] = 'new_value'

# Write updated data back to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully!")
