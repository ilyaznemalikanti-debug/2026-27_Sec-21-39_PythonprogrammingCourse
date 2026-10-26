marks=int(input("enter the marks: "))
if marks<0 or marks>100:
  print("invalid marks")
elif marks>=90:
    grade="A"
elif marks>=80:
    grade="B"
elif marks>=70:
    grade="C"
elif marks>=60:
    grade="D"
else:
    grade="F"
if 0<=marks<100:
    print(f"the student's grade is :{grade}")