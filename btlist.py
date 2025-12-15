import hambtlist
Diem = [7.5, 8.0, 6.0, 9.0, 5.5, 8.5, 7.0, 6.5]
print(f"Điểm trung bình là {hambtlist.dtb(Diem)}")
print(f"Điểm cao nhất là {hambtlist.dcn(Diem)}")
lon,nho=hambtlist.cl(Diem)
print(f"số điểm lớn hơn hoặc bằng 8 là: {lon} và số điểm nhỏ hơn 8 là: {nho}")
print(f"Danh sách tăng dần là: {hambtlist.tang(Diem)}")