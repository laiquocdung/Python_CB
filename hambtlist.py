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
    for i in range(len(Diem)-1):
        for j in range(i+1,len(Diem)):
            if (Diem[i]>Diem[j]):
                Diem[i],Diem[j]=Diem[j],Diem[i]
    return Diem



