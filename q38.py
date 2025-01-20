def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Find the transpose
transposed_matrix = transpose(matrix)

# Print the transposed matrix
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)