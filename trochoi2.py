import random
diem = 0
for luot in range(1,8):
    if random.random() < 0.7:
        diemthang=random.randint(10,25)
        diem+=diemthang
        print(f"Lượt {luot} bắn thành công + thêm {diemthang} , tổng điểm hiện tại {diem} ")
    else:
        print(f"Lượt {luot} bắn không thành công , tổng điểm hiện tại {diem} ")
    if diem >=90:
        print("Chúc mừng bạn đã thắng trò chơi")
        break
else:
     diem<90
     print(f"Hết 7 lượt , tổng điểm {diem} Bạn đã thua rồi !")
