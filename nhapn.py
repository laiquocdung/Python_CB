dk=True
while dk :
    try:
        n=int(input("nhập n"))
        
        if n>0:
            break
        else:
            print("Vui lòng nhập số nguyên lớn hơn 0!")
    except ValueError:
        print("Lỗi nhập liệu !")
i = 1
while i <= n:
    print(i, end=" ")
    i += 1 