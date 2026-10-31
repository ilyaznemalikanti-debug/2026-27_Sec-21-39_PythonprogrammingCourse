#Remove Duplicates from a List Using Sets
# Create a list
numbers = [10, 20, 10, 30, 20, 40, 30]

print("Original list:", numbers)

# Convert list into set
unique = set(numbers)

# Convert set back into list
result = list(unique)

print("List without duplicates:", result)