def tamgiac(n):
    for i in range(1,n+1):
        print("*"*i)
while True:
    try:
        n=int(input("Nhập số dòng sao : "))
        if (n > 0) :
          break
    except ValueError:
        print("Lỗi nhập liệu")
sodongsao= tamgiac(n)
print(f"{sodongsao}")