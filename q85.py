import csv

file_name = input("Enter the CSV file name: ")

try:
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
