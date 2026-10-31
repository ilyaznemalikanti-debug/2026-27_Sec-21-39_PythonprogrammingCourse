#Remove Duplicate Elements from a List

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original list:", numbers)
print("List without duplicates:", unique)