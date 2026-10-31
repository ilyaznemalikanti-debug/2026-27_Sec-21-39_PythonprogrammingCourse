#Continue Statement
#by using for loop 
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#by using while loop
i = 0

while i < 5:
    i = i + 1
    if i == 3:
        continue
    print(i)