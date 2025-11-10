import math
A=float(input("Nhap canh A "))
B=float(input("Nhap canh B "))
C=float(input("Nhap canh C "))
if(A>0 and B>0 and C>0 and A+B>C and B+C>A and A+C>B):
    cv=A+B+C
    p=cv/2
    dt= math.sqrt(p*(p-A)*(p-B)*(p-C))
    print(f"Chu vi la {cv}-Dien tich la {dt} ")
else:
    print("Cac canh k thoa dk de lam tam giac")
    