import random
nangluong=0
print("=====TRO CHOI NAP NANG LUONG=====")
for nap in range(1,6):
    if random.random() < 0.6:
        nangluongthang= random.randint(15,40)
        nangluong += nangluongthang
        print(f"Nạp năng lượng thành công . Tăng {nangluongthang} năng lượng . Tổng năng lượng : {nangluong}")
    else:
        giamnangluong=random.randint(5,15)
        nangluong =max(0,nangluong-giamnangluong)
        print(f"Nạp năng lượng thất bại . Giảm {giamnangluong} năng lượng . Tổng năng lượng : {nangluong}")
    if nangluong >= 120 :
        print ("Chúc mừng bạn đã thắng (>=120) ")
        break
else:
    print("Bạn thua rồi ! (<120)")