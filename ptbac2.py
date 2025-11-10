import math
A= float(input("Nhap A"))
B= float(input("Nhap B"))
C= float(input("Nhap C"))
D=B**2-4*A*C
X=-B /(2*A)
if (D<0):
    print("vo nghiem")
elif(D==0):
    print(f"x={X}")
else:
    X1=(-B+math.sqrt(D))/(2*A)
    X2=(-B-math.sqrt(D))/(2*A)
    print(f"x1={X1}")
    print(f"x2={X2}")
    
