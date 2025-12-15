import random
diem = 0
print("=== Trò chơi Săn kho báu ===")
for luot in range(1,7):
    if random.random() < 0.6:  
        diem_thang = random.randint(5, 30)
        diem += diem_thang
        print(f"Lượt {luot}: Tìm thấy kho báu! +{diem_thang} điểm. Tổng: {diem}")
    else:
        diem = max(diem - 2,0 )
        print(f"Lượt {luot}: Không tìm thấy. -2 điểm. Tổng: {diem}")
    
    if diem >= 80:
        print("Chúc mừng! Bạn thắng trò chơi!")
        break
else:
    print(f"Hết 6 lượt, tổng điểm {diem}. Bạn thua rồi!")