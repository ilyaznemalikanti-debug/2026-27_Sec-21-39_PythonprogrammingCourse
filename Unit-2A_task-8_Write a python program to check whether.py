#Write a python program to check whether a given number is prime or not (assume the input number is between 1 and 100)

n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")