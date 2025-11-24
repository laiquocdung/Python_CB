dk=True
while dk :
    try:
        n=int(input("nhập n"))
        
        if n>=0:
            break
        else:
            print("Vui lòng nhập số nguyên lớn hơn 0!")
    except ValueError:
        print("Lỗi nhập liệu !")

print("----Cau 1----")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("----Cau 2----")
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")

print("----Cau 3----")
for i in range (1,n+1):
    if i%3==0:
        print(i,end=" ")
        
print("----Cau 4----")
soam=0
print("Nhập 10 số: ")

for i in range(10):
    while True:
        try:
            n = int(input(f"Số thứ {i+1}: "))
            break
        except ValueError:
            print("Lỗi! Vui lòng nhập số hợp lệ.")

    if n < 0:
        soam += 1

print("Số lượng số âm là:", soam)

print("----Cau 5----")
while True :
    try:
        n=int(input("nhập n"))
        
        if n>=0:
            break
        else:
            print("Vui lòng nhập số nguyên lớn hơn 0!")
    except ValueError:
        print("Lỗi nhập liệu !")
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")

print("----Cau 6----")
while True :
    try:
        n=int(input("nhập n"))
        
        if n>=0:
            break
        else:
            print("Vui lòng nhập số nguyên lớn hơn 0!")
    except ValueError:
        print("Lỗi nhập liệu !")
for i in range (1,n+1):
    if i ==5:
        continue
    else:
        print(i,end=" ")

#print("----Cau 7----")
print("----Cau 8 ----")
while True :
    try:
        n=int(input("nhập n"))
        
        if n>=0:
            break
    except ValueError:
        print("Lỗi nhập liệu !")
i=1
max=-1000
min=1000
while (i<=n):
    try:
        so=int(input(f"Nhập số thứ {i}"))
        i+=1
        if(so>max):
            max=so
        if(so<min):
            min=so
    except ValueError:
        print("Sai kiểu dữ liệu")
print(f"Giá trị lớn nhất là {max},Giá trị nhỏ nhất là {min}")







