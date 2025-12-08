def tinhcvdt(cd,cr):
        dt= cd*cr
        cv=(cd+cr)*2
        return cv,dt
try:
    cd=int(input("nhap chieu dai"))
    cr=int(input("nhap chieu rong"))
except ValueError:
    print("Loi nhap lieu")
    
cvdt=tinhcvdt(cd,cr)

print(f"chu vi la {cvdt[0]} va dien tich la {cvdt[1]}")