while True :
    try:
        n=int(input("nhập n"))
        if (n>=0):
            break
    except ValueError:
        print("Lỗi nhập liệu !")
dem=0
N=n
while(n!=0):
    n=n//10
    dem+=1
print(f"số {N} có {dem} chữ số")
print(reversed(N))