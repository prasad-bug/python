import statistics

# Example list of numbers
numbers = [1, 2, 2, 3, 4, 5, 5]

# Compute mean, median, and mode
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
