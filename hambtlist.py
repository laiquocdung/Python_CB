def dtb(Diem):
    tong=0
    for value in Diem:
        tong += value
    Diemtb=tong/len(Diem)
    return Diemtb
def dcn(Diem):
    max=Diem[0]
    for value in Diem:
        if value > max:
            max = value 
    return max
def cl(Diem):
    diemlonhon8=0
    diemnhohon8=0
    for value in Diem:
        if value >=8:
            diemlonhon8+=1
        else:
            diemnhohon8+=1
    return diemlonhon8,diemnhohon8
def tang(Diem):
    i=Diem
    while i ==10:
        print (i,end=' ')
        i+=1
    return i



