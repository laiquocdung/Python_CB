try:
    So= int(input("nhap so "))
except:print("loi nhap lieu")
else:
    if So%2 ==0 :
        print(f"{So} la so chan")
    else:
        print(f"{So} la so le")