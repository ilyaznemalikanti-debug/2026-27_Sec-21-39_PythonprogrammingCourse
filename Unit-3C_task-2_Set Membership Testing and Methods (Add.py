#Set Membership Testing and Methods (Add, Remove, Discard)
# Create a set
s = {10, 20, 30, 40}

print("Original set:", s)

# Membership testing
print("Is 20 present?", 20 in s)
print("Is 50 present?", 50 in s)

# Add element
s.add(50)
print("After add:", s)

# Remove element
s.remove(20)
print("After remove:", s)

# Discard element
s.discard(60)
print("After discard:", s)