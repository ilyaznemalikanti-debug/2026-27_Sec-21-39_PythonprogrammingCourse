#Centered pyramid pattern of stars
n = int(input("Enter rows: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* " * i)