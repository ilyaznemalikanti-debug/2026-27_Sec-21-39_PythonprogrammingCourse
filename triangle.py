#a triangle is valid given its three angles
Angle_a=int(input("enter the angle a: "))
Angle_b=int(input("enter the angle b: "))
Angle_c=int(input("enter the angle c: "))
if Angle_a>0 and Angle_b>0 and Angle_c>0:
    if Angle_a>0 and Angle_b>0 and Angle_c>0 and Angle_a+Angle_b+Angle_c==180:
        print("The triangle is valid")
    else:
     print("The triangle is not valid")