try:
    van= float(input("Nhập điểm môn văn"))
    toan=float(input("Nhập điểm môn toán"))
    anh=float(input("Nhập điểm môn Anh"))
except ValueError:
    print("Lỗi nhập liệu")
else:
     dtb=(van+toan+anh)/3
     if(van <0 or van >10 or toan <0 or toan >10 or anh <0 or anh >10):
        print("Sai nhập liệu")
     elif(dtb>=9):
        print("Học sinh xuất sắc")
     elif(dtb>=8):
        print("Học sinh giỏi")
     elif(dtb>=7):
        print("Học sinh khá")
     elif(dtb>=5):
        print("Học sinh trung bình")
     else:
        print("Học sinh yếu")