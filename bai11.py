while True:
    try:
        n=int(input("Nhập 1 số : "))
        if n >0 :
            break
    except ValueError:
        print("Lỗi nhập liệu!")

tong=0
for i in range(1,n):
    if n%i==0:
        tong+=i
if tong == n:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")
    