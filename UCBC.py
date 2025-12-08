import hamUCBC
while True:
    try:
        a=int(input("nhập A "))
        b=int(input("nhập B "))
        if a>0 and b>0:
            break
    except ValueError:
        print("lỗi nhập liệu")
print(f"USCLN của {a} và {b} là {hamUCBC .USCLN(a,b)}")

