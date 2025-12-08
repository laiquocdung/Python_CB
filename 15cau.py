#Câu 1
import ham15cau
c=(input("Nhập chuỗi: "))
print(f"Độ dài chuỗi là: {ham15cau.chieudai(c)}")
#Câu 2
s = "Python Programming"
print({ham15cau.chuoi(s)})
#Câu 3
a=input("Nhập chuỗi")
dau,cuoi=ham15cau.chuoi1(a)
print(f"3 ký tự đầu là :{dau}")
print(f"3 ký tự cuối là :{cuoi}")
#Câu 4
ten=input("Nhập tên 1 người: ")
hoa,thuong=ham15cau.ten(ten)
print(f"in hoa hết là : {hoa}")
print(f"in thường hết là : {thuong}")
#Câu 5
ho=input("Nhập họ: ")
dem=input("Nhập tên đệm: ")
ten=input("Nhập tên: ")
ho_ten=ham15cau.hodemten(ho,dem,ten)
print(f"Tên đầy đủ là: {ho_ten}")