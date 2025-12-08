#Câu 1
def chieudai(c):
    return len(c)
#Câu 2
def chuoi(s):
    print(f"ký tự đầu tiên là: {s[0]} ")
    print(f"ký tự cuối cùng là: {s[-1]}")
    print(f"ký tự ở giữa vị trí chuỗi là: {s[len(s)//2]}")
#Câu 3 
def chuoi1(a):
    badau={a[:3]}
    bacuoi={a[-3:]}
    return badau,bacuoi
#Câu 4 
def ten(t):
   viethoa=t.upper()
   vietthuong=t.lower() 
   return viethoa,vietthuong
   
