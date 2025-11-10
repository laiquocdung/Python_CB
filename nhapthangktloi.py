try:
    thang= int(input("nhap thang"))
except:print("loi nhap lieu")
else:
    if thang <1 or thang >12:
        print("thang chi tu 1 toi 12")
    elif thang in (1,3,5,7,8,10,12):
        print(f"thang {thang} co 31 ngay")
    elif thang == 2:
        print(f"thang {thang} co 28 ngay")
    elif thang in (4,6,9,11):
        print(f"thang {thang}co 30 ngay")

    