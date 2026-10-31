#Print a 5×5 grid of stars using user input
n = int(input("Enter grid size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()