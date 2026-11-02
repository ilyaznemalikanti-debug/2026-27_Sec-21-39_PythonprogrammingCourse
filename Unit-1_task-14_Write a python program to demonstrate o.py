#Write a python program to demonstrate operator precedence and associativity
a = 10
b = 5
c = 2

# Operator Precedence
result1 = a + b * c
print("Operator Precedence:", result1)

# Operator Associativity
result2 = a - b - c
print("Operator Associativity:", result2)

# Parentheses
result3 = (a + b) * c
print("Using Parentheses:", result3)