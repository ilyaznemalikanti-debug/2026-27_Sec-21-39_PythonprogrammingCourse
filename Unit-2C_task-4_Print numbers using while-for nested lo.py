#Print numbers using while-for nested loop
i = 0
n = 1

while i < 3:
    for j in range(3):
        print(n, end=" ")
        n += 1
    print()
    i += 1